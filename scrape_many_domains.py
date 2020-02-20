import pandas
import os
import time
from urllib.request import urlopen, Request
from tld import get_tld, get_fld

if not os.path.exists("domain_html"):
	os.mkdir("domain_html")

df = pandas.read_csv("domains.csv")

for link in df.domain_name:
	print(f"Downloading: {link}")
	fileName = "domain_html/" + link
	if not os.path.exists(fileName):
		f = open(fileName, "wb")
		try:
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}
			requestLink = get_fld("https://www." + link)
			req = Request(url = "https://www." + requestLink, headers=headers)
			response = urlopen(req)
			f.write(response.read())
		except:
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}
			requestLink = get_fld("https://" + link)
			req = Request(url = "https://" + requestLink, headers=headers)
			response = urlopen(req)
			f.write(response.read())
		f.close()
		time.sleep(10)
