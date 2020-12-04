# Flask Web Application with Mongo DB

A simple enrollment system build using Python, Flask, Jinja2 and MongoDB

<p align="center">
  <img src="https://github.com/haxamxam/Flask_WebApplication_MongoDB/blob/main/flask_website.gif" width="600" alt="accessibility text">
</p>


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage

Go to the main directory in the terminal and run the following

```python
flask run
```

## __init.py__


```python
from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from application import routes

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
