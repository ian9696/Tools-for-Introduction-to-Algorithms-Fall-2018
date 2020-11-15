## Tools for *Introduction to Algorithms (Fall 2018)*
Tools for grading and downloading/uploading assignment on [NCTU OJ](https://oj.nctu.edu.tw/) for undergraduate course *Introduction to Algorithms (Fall 2018)*, implemented using Python and [OpenPyXL](https://pypi.org/project/openpyxl/).

## Tools
### `download.py`, `upload.py`
Download/Upload assignment on NCTU OJ, which includes text files for title, description, input, output, hint, and source sections (PDF format is also supported).

Testdata are also downloaded/uploaded along with their constraints, which include JSON files for time_limit, memory_limit, output_limit, score, and sample.

### `genTest.py`
Generate default Testdata constraints in JSON format.

### `getScore.py`
Download submission list from NCTU OJ.

Filter submissions by score, creation time, and ip address.

Ignore submissions according to submission ID, user ID, and user name.

Calculate grade and output in XLSX format.
