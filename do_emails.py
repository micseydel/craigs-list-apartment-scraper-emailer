#!/usr/bin/env python

from urllib import quote, urlopen
from webbrowser import open as browseropen
import re
import json

# i know it's HTML, but if this broke for what i was doing, that would be ok
TITLE_PAT = re.compile('var postingTitle = "(.+)";')

BODY_TEMPLATE = '''\
<Your message>

Regarding {}
'''

CC = ['micseydel@gmail.com']

with open('emails.json') as f:
    apartments = json.load(f)

for apartment in apartments:
    to = apartment['email']
    cc = ','.join(CC)
    title = quote(TITLE_PAT.findall(apartment['page'])[0])
    title = title.replace('ft&sup2;', 'sqft')
    body = quote(BODY_TEMPLATE.format(apartment['link']))

    url = 'mailto:{to}?cc={cc}&subject={title}&body={body}'.format(
        **locals()
    )
    browseropen(url)
    raw_input()
