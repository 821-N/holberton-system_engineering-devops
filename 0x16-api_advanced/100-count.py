#!/usr/bin/python3
"""
    everyone who uses reddit is a loser lol
"""
import requests


def recurse(r, words, counts={}, after=None):
    """ search words """
    if type(words) == str:
        words = " ".split(words.lower())
    response = requests.get(
        "https://reddit.com/r/"+r+"/hot.json",
        headers={"User-Agent": "Mozzila/5.0"},
        params={"after": after}
    )
    data = response.json().get("data", {})
    for word in words:
        counts[word] = counts.get(word, 0) + sum(
            post["data"]["title"].lower().count(word)
            for post in data.get("children", [])
        )
    after = data.get("after", None)
    if not after:
        return counts or None

    return recurse(r, words, counts, after)
