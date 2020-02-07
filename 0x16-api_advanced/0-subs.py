#!/usr/bin/python3
"""
    everyone who uses reddit is a loser lol
"""
import requests
from sys import argv


def number_of_subscribers(r):
    """ get number of subscribers to a subreddit """
    response = requests.get(
        "https://reddit.com/r/"+r+"/about.json",
        headers={"User-Agent": "Mozzila/5.0"}
    )
    return response.json().get("data", {}).get("subscribers", 0)
