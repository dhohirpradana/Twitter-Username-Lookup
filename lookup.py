import requests
import progressbar
from time import sleep
import random

lookup_url = "https://api.twitter.com/1.1/users/show.json"
token = "AAAAAAAAAAAAAAAAAAAAAD5wagEAAAAAGGbmEmGhBJ511DURtHFgwdp6uQ8%3DqiH42x8UeZezBf3qRknLYGWrnssv6nMA3mHTZoXxmiqJiGEBCy"

unusedFile = open("unused.txt", "a+")
usedFile = open("used.txt", "a+")

used = []
unused = []

max_loop = 900
usn = "dp"

bar = progressbar.ProgressBar(maxval=max_loop,
                              widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

# loop max loop times
for i in range(max_loop):
    # update progress bar
    bar.update(i + 1)
    sleep(0.1)
    
    # rand 3 digit number
    randNum= random.randint(100, 599)

    # random 5 length word
    rand = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(2))
    username = usn + str(randNum)

    # make request to lookup_url
    r = requests.get(lookup_url, headers={
                     "Authorization": "Bearer " + token}, params={"screen_name": username})

    if r.status_code == 404:
        print("Unused: ", username)
        unused.append(username)
        unusedFile.write(username + "\n")
    else:
        print("Used: ", username)
        used.append(username)
        usedFile.write(username + "\n")

bar.finish()

# print("Used: ", used)
# print("Unused: ", unused)
