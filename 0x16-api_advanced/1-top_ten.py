#!/usr/bin/python3
"""
    everyone who uses reddit is a loser lol
"""
import requests


def top_ten(r):
    """ get top 10 HOT POSTS :fire: :fire: :fire: """
    response = requests.get(
        "https://reddit.com/r/"+r+"/hot.json",
        headers={"User-Agent": "Mozzila/5.0"},
        params={"limit": 10}
    )
    posts = response.json().get("data", {}).get("children")
    if posts:
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
