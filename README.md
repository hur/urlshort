# URLshort
![tests](https://github.com/hur/urlshort/workflows/tests/badge.svg)

Shortens URLs by taking translating database indexes to a radix-56 representation with a character set that improves readability.

For a live demo, see https://hur.wtf (for proper TLS, please use https://url-shortening-app.herokuapp.com/).
The demo runs on a free heroku dyno, which means that the dyno sleeps when not used and takes some time to restart.

## How to setup development environment
### Requirements
Python 3 & virtualenv (recommended)
### Steps
Clone the repository and cd into the directory:
```
git clone https://github.com/hur/urlshort.git
cd urlshort
```
Set up a virtual environment:

`virtualenv venv`

Activate the virtual environment:
```
(Windows / CMD):
venv\Scripts\activate
(Mac OS / Unix):
source venv/bin/activate 
```
Install requirements:

`pip install -r requirements.txt`

Set up `.env` file with your secret key

```
SECRET_KEY = "yoursecretkey"
```
You can generate a random secret key using Python:
```
>>> import uuid
>>> uuid.uuid4().hex
```

Configure your environment variables and `config.py` to suit your needs, e.g.
if you wish to use a different database url.
It is recommended to set the `URL` environment variable to whatever url you are running the app in
(e.g. `http://127.0.0.1:5000`)
so that the app can provide correct output.

To initialize the database, use
```
flask createdb
```

Run the app using `flask run`. In some cases using `python -m flask run` instead may resolve issues that occur with `flask run`.

For running all tests, use `py.test`

