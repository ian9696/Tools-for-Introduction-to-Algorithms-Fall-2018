## Tools for *Introduction to Algorithms (Fall 2018)*
Tools for grading and downloading/uploading assignment on [NCTU OJ](https://oj.nctu.edu.tw/) for undergraduate course *Introduction to Algorithms (Fall 2018)*, implemented using Python and [OpenPyXL](https://pypi.org/project/openpyxl/).

## List of tools
### download.py, upload.py
- Download/Upload assignment on NCTU OJ, which includes text files for title, description, input, output, hint, and source sections (PDF format is also supported).

- Testdata are also downloaded/uploaded along with their constraints, which include JSON files for time limit, memory limit, output limit, score, and sample.

### genConstraint.py
- Generate default testdata constraints in JSON format.

### getScore.py
- Download submission list from NCTU OJ.

- Filter submissions by score, creation time, and IP address.

- Ignore submissions according to submission ID, user ID, and user name.

- Calculate grade and output in XLSX format.

## Note
Domain name of NCTU OJ has changed from `oj.nctu.me` to `oj.nctu.edu.tw`, and domain name for API has changed from `api.oj.nctu.me` to `api.oj.nctu.edu.tw`.
