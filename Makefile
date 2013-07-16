PYTHON = python2.6
all: done

# Poorly documented and unexplained other than this:
#
# The order to run them is:
# scrape_phone_numbers.py (requires apartment_links.txt) - generates apartments.json
apartments.json: scrape_phone_numbers.py apartment_links.txt
	$(PYTHON) $<
# separate_contact_info.py (requires apartments.json) - 
# you can ignore the stdout, that's for me. it generates emails.json, needed below
emails.json: separate_contact_info.py apartments.json
	$(PYTHON) $<
# do_emails.py (requires emails.json) - with all the files downloaded, 
# or just emails.json, this is all you need to run. 
done: do_emails.py emails.json
	$(PYTHON) $<
# will open an email in your browser that you can just send off, one at a time, 
# and you push enter in the terminal window to tell it that you've completed an email. 
# You can modify the script if you want the email to be different at all, and tweak individual ones in the browser.
#
# You only need to run all the scripts if you change apartments_links.txt. 
# It only handles Craig's List link too, since everyone else is stupid fancy and hard to deal with.
#
# P.S. if you get a syntax error, upgrade Python!



clean:
	rm -f apartments.json emails.json
