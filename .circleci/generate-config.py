#!/usr/bin/env python3

# fetch latest release number for each OS and populate "releases" key in matrix.yml
# with current and previous release numbers (building for last two major)

print(lastversion.latest('fedora'))