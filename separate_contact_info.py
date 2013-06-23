#!/usr/bin/env python

import json
import re

# this worked emperically, it's not robust
PHONE_PAT = re.compile('\(\d{3}\) ?\d{3}-\d{4}')

def main():
    with open('apartments.json') as f:
        apartments = json.load(f)

    to_email = []
    for apartment in apartments:
        link, page, emails = apartment['link'], apartment['page'], apartment['emails']
        if not emails:
            print 'No email found for'
            print link
            print 'but found these phone numbers:',
            print PHONE_PAT.findall(page)
            print
            continue
        elif len(emails) > 2:
            print "Whoa,", link, "had", emails
            print "This script doesn't deal with that. Good luck though."

        apartment['email'] = emails.pop()
        to_email.append(apartment)

    with open('emails.json', 'w') as f:
        f.write(json.dumps(to_email))

if __name__ == '__main__':
    main()
