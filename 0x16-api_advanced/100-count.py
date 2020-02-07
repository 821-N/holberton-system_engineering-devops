#!/usr/bin/python3
"""
    everyone who uses reddit is a loser lol
"""
import requests


def recurse(r, words, counts={}, after=None):
    """ search words """
    if type(words) == str:
        words = words.lower().split(" ")
    response = requests.get(
        "https://reddit.com/r/"+r+"/hot.json",
        headers={"User-Agent": "Mozzila/5.0"},
        params={"after": after}
    )
    data = response.json().get("data", {})
    for word in words:
        count = sum(
            post["data"]["title"].lower().count(word)
            for post in data.get("children", [])
        )
        if count:
            counts[word] = counts.get(word, 0) + count
    after = data.get("after", None)
    if after:
        return recurse(r, words, counts, after)
    for word, num in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(word+":", num)
