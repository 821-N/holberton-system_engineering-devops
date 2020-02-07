#!/usr/bin/python3
"""
    everyone who uses reddit is a loser lol
"""
import requests


def recurse(r, hot_list=[], after=None):
    """ get top 10 HOT POSTS :fire: :fire: :fire: """
    response = requests.get(
        "https://reddit.com/r/"+r+"/hot.json",
        headers={"User-Agent": "Mozzila/5.0"},
        params={"after": after}
    )
    data = response.json().get("data", {})
    hot_list = hot_list + [
        post["data"]["title"] for post in data.get("children", [])
    ]

    after = data.get("after", None)
    if not after:
        return hot_list or None

    return recurse(r, hot_list, after)
