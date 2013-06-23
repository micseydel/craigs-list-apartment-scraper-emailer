#!/usr/bin/env python

from urllib import urlopen
import sys
import re
import json

EMAILS_PAT = re.compile('[a-z0-9\.\-]+@[a-z0-9\.\-]+\.[a-z]{2,4}', re.IGNORECASE)
APARTMENT_LINKS = 'apartment_links.txt'

def main():
    links_filename = APARTMENT_LINKS if len(sys.argv) < 2 else sys.argv[1]
    with open(links_filename) as links:
        pages = {link.strip(): urlopen(link.strip()).read() for link in links}

    entries = []

    for link, page in pages.iteritems():
        if 'This posting has been deleted by its author.' in page:
            print link, 'deleted'
            continue

        emails = list(set(EMAILS_PAT.findall(page)))
        entries.append(
                {
                    'link': link,
                    # damn non-ascii
                    'page': filter(lambda c: ord(c) < 128, page),
                    'emails': emails
                }
            )

    with open('apartments.json', 'w') as f:
        f.write(json.dumps(entries))

if __name__ == '__main__':
    main()
