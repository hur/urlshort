# URLshort
Shortens URLs by taking database index and converting to base 56 with a modified character set.

In its current state, URLshort is not hosted anywhere and
only generates and displays a shortened URL.

![Sample Image](https://raw.githubusercontent.com/hur/urlshort/master/sample_image.png)
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
source venv\Scripts\activate 
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

Initialize the database in the Python interpreter:
```
>>> from urlshort import db
>>> db.create_all()
```
Run the app using `flask run`.

Enter a URL and press shorten. The web app will display `urlshort.git/X`. Navigate to `http://127.0.0.1:5000/X` to be redirected to the page.
