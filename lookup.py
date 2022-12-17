import os
import random
from io import open
from time import sleep

import progressbar
import requests

LOOKUP_URL = "https://api.twitter.com/1.1/users/show.json"
token = os.environ.get("TWITTER_BEARER_TOKEN")

unusedFile = open("unused.txt", "a+", encoding="utf-8")
usedFile = open("used.txt", "a+", encoding="utf-8")

used = []
unused = []

MAX_LOOP = 900
USN = "dp"

bar = progressbar.ProgressBar(
    maxval=MAX_LOOP,
    widgets=[progressbar.Bar("=", "[", "]"), " ", progressbar.Percentage()],
)
bar.start()

# loop max loop times
for i in range(MAX_LOOP):
    # update progress bar
    bar.update(i + 1)
    sleep(0.1)

    # rand 3 digit number
    randNum = random.randint(100, 599)

    # random 5 length word
    RAND = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(2))
    USERNAME = USN + str(randNum)

    # make request to lookup_url
    r = requests.get(
        LOOKUP_URL,
        headers={"Authorization": "Bearer " + token},
        params={"screen_name": USERNAME},
    )

    if r.status_code == 404:
        print("Unused: ", USERNAME)
        unused.append(USERNAME)
        unusedFile.write(USERNAME + "\n")
    else:
        print("Used: ", USERNAME)
        used.append(USERNAME)
        usedFile.write(USERNAME + "\n")

bar.finish()

# print("Used: ", used)
# print("Unused: ", unused)
