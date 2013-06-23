Some simple scripts for scraping Craig's List posts and then opening the email
client with an email ready for the user to send off.

Usage: apartment_links.txt has Craig's List URLs. You would run
scrape_phone_numbers.py which generates apartments.json and then run
separate_contact_info.py to create emails.json, and then run do_emails.py to
open your mail client. You must push enter after each email to go onto the
next once, since opening them at all once could be too much.
Just justdoit to automate all this, and cleanup to delete the JSON files.

More could be done with this. I could export much of the hard-coded content to
config files but didn't need to for my purposes.
