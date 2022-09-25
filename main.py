from telethon.sync import TelegramClient
from telethon import functions
from time import sleep
import sys

try:
    import config
except ImportError:
    print('Please go to https://my.telegram.org/ and get your api_id and api_hash, and then put them in config.py')
    sys.exit(1)

installed_stickers = []

with TelegramClient('sessionfile', config.api_id, config.api_hash) as client:
    while True:
        # get currently installed stickers and save to currently_installed
        currently_installed = client(functions.messages.GetAllStickersRequest(hash=0)).sets

        # if length of currently_installed is different from installed_stickers, then update installed_stickers
        if len(currently_installed) != len(installed_stickers):
            installed_stickers = currently_installed

        # if there are no stickers installed, exit
        if len(installed_stickers) == 0:
            print('No stickers installed')
            sys.exit(0)

        # iterate over currently_installed
        sort_needed = False
        for idx, sticker in enumerate(currently_installed):
            if installed_stickers[idx] != sticker:
                sort_needed = True
                break

        # if sort_needed is True, then sort stickers to be same as installed_stickers
        if sort_needed:
            print('Sorting stickers')
            # for idx, sticker in enumerate(installed_stickers):
            client(functions.messages.ReorderStickerSetsRequest(
                masks=False,
                order=[sticker.id for sticker in installed_stickers]
            ))

        sleep(3)
