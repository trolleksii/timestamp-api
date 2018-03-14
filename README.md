# FreeCodeCamp API Basejump: Timestamp Microservice

## User stories:
1) It will check to see whether that string contains either a unix timestamp or a natural language date (example: January 1, 2016)
2) If it does, it returns both the Unix timestamp and the natural language form of that date.
3) If it does not contain a date or Unix timestamp, it returns null for those properties.

## Example usage:
`http://localhost:8000/December%2015,%202015`<br>
`http://localhost:8000/1450137600`

## Example output:
`{ "unix": 1450137600, "natural": "December 15, 2015" }`

## Installation instructions
1. Install Python3, pip, venv:<br>
`sudo apt install python3 python3-pip python3-venv`
2. Clone this repository:
```
mkdir project
cd ./project
git clone https://github.com/trolleksii/timestamp-api.git
```
3. Create a new virtual environment with Python 3 interpreter:<br>
 `virtualenv -p python3 ./venv`
4. Activate it:<br>
 `source ./venv/bin/activate`
5. Install required packages from requirements.txt:<br>
 `pip install -r ./timestamp-api/requirements.txt`
6. `cd` into ./timestamp-api:<br>
 `cd ./timestamp-api/`
7. Run tests to make sure that everything is working as it should:<br>
 `python manage.py test`

