import requests
import progressbar
from time import sleep

lookup_url = "https://api.twitter.com/1.1/users/show.json"

max_loop = 900

# loop
