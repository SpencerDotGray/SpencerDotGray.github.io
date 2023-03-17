
from redbox import EmailBox
from redbox.query import UNSEEN, SUBJECT
from redbox import gmail
from bs4 import BeautifulSoup
from pprint import pprint
import os
import json

if os.environ.get('GMAIL_EMAIL') is not None and os.environ["GMAIL_APP_CODE"] is not None:
    gmail.username = os.environ["GMAIL_EMAIL"]
    gmail.password = os.environ["GMAIL_APP_CODE"]
else:
    with open("./keys/keys.json", 'r') as json_file:
        keys = json.load(json_file)
        gmail.username = keys['email']
        gmail.password = keys['app_code']


search_subject = "Climb Youth Devotional Response"

inbox = gmail['INBOX']

tags = ['First Name', 'Last Name', 'Day', 'Reflection']

for msg in inbox.search(SUBJECT(search_subject)):

    print('START\n\n')

    html = msg.html_body
    parsed_html = BeautifulSoup(html, features="html.parser")
    #print(parsed_html.prettify())
    #print(parsed_html.find_all('br'))

    export_info = {}

    take_next = False
    take_tag = ''
    for string in parsed_html.strings:
        
        string = string.replace('=', '').strip()

        if string == '':
            continue

        if take_next:
            export_info[take_tag] = string
            take_next = False
        elif string in tags:
            take_next = True
            take_tag = string

    pprint(export_info)
