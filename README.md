# Easy CID

La constatazione amichevole 


## Run easycid locally (dev mode)

Clone the project:
```
$ git clone git@bitbucket.org:Dosdos/easycid.git
```

Setup a virtualenv.

If you use *virtualenvwrapper* create a new env
```
$ mkvirtualenv easycid
```

or execute the existing one:
```
$ workon easycid
```

Move to the root folder of easycid:
```
$ cd easycid
```

Use pip to update dependencies from the requirements file:
```
$ pip install requirements.txt
```

If you are setting up the production environment:

- Create a new environment variable **ENV** and set it to **prod** and
- Ensure the configurations (e.g. DB connection) in *easycid/production_settings.py* file are set correctly for your environment.


Perform migrations for database sync: (it automatically runs migrations and creates a superuser - yes, do it!)
```
$ ./manage.py migrate
```

Finally run Django:
```
$ ./manage.py runserver
```

Verify all is working going to [EasyCid CMS homepage](http://127.0.0.1:8000/).
