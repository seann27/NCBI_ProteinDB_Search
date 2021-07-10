# NCBI_ProteinDB_Search

DESCRIPTION:
- This script runs get requests to the Entrez API to get
a full list of human protein accession numbers from NCBI's protein database
- Stores the accession numbers in a list and writes to a pickle file

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
