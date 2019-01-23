## About

Models the database in python using SQLAlchemy.

---

### Installing

Clone repository and go to destination.
```
cd PATH_TO_DESTINATION/
```

Setup and activate virtual environment, normally same as destination.
```
virtualenv venv
source venv/bin/activate
```

Use pip to install setup
```
cd PATH_TO_DESTINATION/
pip install .
```
---

### Connecting

The connection string for postgresql is 
```
CONNECTION = '{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'
```

Separate production and test `settings.py` files are used to establish connections.

### Testing

To run all tests, go to the project root directory and run

`python -m unittest discover -v`

The project mostly uses absolute imports. However, the test files use relative 
imports because the test directory is not included in the package distribution.
