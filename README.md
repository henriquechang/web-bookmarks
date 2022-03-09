# webBookmarks

Web Bookmarks django application with very simple auth method for testing

#### Setup:

```
pipenv install --dev
python manage.py makemigrations
python manage.py migrate
```

#### Create test users - Password doesn't matter:
```
python manage.py createsuperuser --username=test --email=test@example.com 
python manage.py createsuperuser --username=test2 --email=test@example.com 
```

#### Run App:
```
pipenv shell
python manage.py runserver
```

#### Run Tests
```
python manage.py test
```

#### Run Local curl scripts:
```
./script.sh
```