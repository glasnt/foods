#!/usr/bin/env python

"""
Take all the non-README markdown files in this directory, and index them on the
README

Generates something okay for the page to generate
"""

import glob

README = "README.md"
listing = []
MAGIC_LINE = "[//]: <> (generated)\n"

for f in glob.glob("*.md"):
    if f != README:
        with open(f) as fc:
            h = fc.readline()
            h1 = h.split("#")[1].strip()

        listing.append(" * [%s](%s)\n" % (h1, f))

data = []
with open(README) as f:
    data = f.readlines()

rewrite = data.index(MAGIC_LINE) + 1

with open(README, 'w') as f:
    f.writelines(data[0:rewrite])
    f.writelines(listing)

