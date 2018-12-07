# fantalytix-sqlalchemy

ORM for Python

#Setup postgresql

#Setup pgAdmin4

Use python environment to run pgAdmin4 as web application.

Install using a virtual environment, python3 and pip3.

Example execution:

`virtualenv venv-bb`

Download the the wheel from pgadmin.org and install e.g.
`pip install ./pgadmin4-1.3-py2.py3-none-any.whl`

Then pgadmin can be run with the following:
`source ~/pgadmin4/bin/activate`
`python ~/pgadmin4/lib/python2.7/site-packages/pgadmin4/pgAdmin4.py`
assuming `~/pgadmin4/` is the virtualenv.

Then point browser to http://127.0.0.1:5050

Once pgadmin is running, connect it to postgresql:

From the dashboard > Add new server

Tab General > Name can be arbitrary

Tab Connection > Host should be `localhost`

Type in password for postgres

#Restoring schema

In pgAdmin, right-click database > Query Tool

Open .sql files. A helper script has been provided to
generate one consolidate file for all .sql queries beginning
with `create-<table_name>.sql`.

#ORM

SQLAlchemy is used in this project as the ORM.

#Connecting

The connection string for postgresql is 

`CONNECTION = '{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}'`

`sqlalchemy.create_engine(CONNECTION)`

#Testing

The project is structured similar to the following:

new_project
├── app
│   ├── __init__.py         # make it a package
│   └── app.py
└── test
    ├── __init__.py         # also make test a package
    └── test_app.py

We can't just run python test_app.py from the test directory
since its `import app` will fail. That module is not on the
`sys.path`.

Luckily, python's `unittest` will solve this for us.

In `test_app.py` import `app.py` normally.

`# import the package`
`import app`

`# import the app module`
`from app import app`

`# or an object inside the app module`
`from app.app import my_object`

Now to run the tests:

`cd new_project`
`python -m unittest test.test_app`

For this particular project do the following:

`cd fantalytix-sqlalchemy`
`python -m unittest test.common.player`

https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure/24266885#24266885

