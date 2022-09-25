# telegram-keep-stickers-sorted

Telegram recently introduced a change that causes your most recently used sticker packs to move to the top, ignoring any organization you might've had. This Python project will keep your Telegram stickers sorted regardless of this change. This is done by comparing a locally stored cache of your sticker packs and reorganizing them if the order has changed.

## Installation

* Download and install Python 3
* Clone the repository to your disk (or download as ZIP using the green Code button on github.com)
* Open a terminal window in the folder where you've saved this repository
* Run these commands (substitute **pip3** and **python3** for **pip** and **python** if you're on Windows):

```shell
pip3 install -r requirements.txt
python3 main.py
```

Enter your phone number, code and password when asked, and keep the script running in the background. Your stickers will be kept organized as long as the script is still running.
