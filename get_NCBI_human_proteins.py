'''
DESCRIPTION:
- This script runs get requests to the Entrez API to get
a full list of human protein accession numbers from NCBI's protein database
- Writes the accession numbers to a pickle file
	-> pickled files are python data structures that can be written to files
	-> this script writes a list
	-> to load pickle file, execute the following python code:

		>>> mylist = []
		>>> with open('protein_gis.pkl', 'rb') as pickle_file:
		>>>    mylist = pickle.load(pickle_file)

REQUIREMENTS:
Python 3
- Python Packages -
requests, pickle, math, time, xml.etree.ElementTree, tqdm

- installing external packages -
$ pip install requests
$ pip install tqdm

NOTES:
- The Entrez API has a limit of 3 calls per second. With an API key, this is increased to 10 calls per second
- The Entrez API returns responses in XML format, not in JSON

LICENSING:
Copyright 2021 Sean Black

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import requests, pickle, math, time
import xml.etree.ElementTree as ET
from tqdm import tqdm

# globals
baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=protein&term=human[orgn]"
accession_nums = []

def parse_ids(content):
	ids = []
	root = ET.fromstring(content)
	for child in root:
		if child.tag == 'IdList':
			for c in child.iter():
				if c.tag == 'Id':
					accession_nums.append(int(c.text))

def main():
	total_count = 0
	# batch number is the number of results per page for the get request
	batch_num = 10000

	# get total number of protein records
	response = requests.get(baseurl)
	root = ET.fromstring(response.content)
	for child in root:
	    if child.tag == 'Count':
	        total_count = int(child.text)
	num_loops = math.ceil(total_count/batch_num)

	# grab protein accession numbers
	for i in tqdm(range(num_loops)):
		if i % 3 == 0:
			# pause between requests, needs more time if batch size is substantially increased
			time.sleep(1.5)
		idx = batch_num * i
		url = f"{baseurl}&retstart={idx}&retmax={batch_num}"
		response = requests.get(url)
		parse_ids(response.content.decode())

	# write the list to pickle file
	with open('protein_gis.pkl', 'wb') as pickle_file:
		pickle.dump(accession_nums, pickle_file)

if __name__ == '__main__':
	main()
