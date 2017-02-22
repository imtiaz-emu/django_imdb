**Requirements:**
  - Python 2.7
  - Django 1.9
  
**Installation:**
  - create a `virtualenv`. Go to project folder and run `virtualenv .`
  - activate virtualenv using `source bin/activate`
  - install requirements using `pip install -r requirements.txt`
  - goto `project/src` folder.
  - Run migrations `python manage.py migrate` (As we're using mysql so change settings accordingly). If you want to use `sqlite3` for testing purpose change `imdb>setting>local.py` file
  - Run project `python manage.py runserver` 
  
