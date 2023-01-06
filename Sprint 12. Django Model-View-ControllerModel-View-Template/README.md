# Django_MTV

## install requirement project's packages

```commandline
pip install -r requirements.txt
```

## Run project

Go to the folder with manage.py file, run library

```commandline
python manage.py runserver
```

## Run tests

Go to the folder with manage.py file, run library

```commandline
python manage.py test
```

## Tests

Add to the project `library` such applications author, book, order, user.

Determine the possibility of processing `GET` requests

```
http://127.0.0.1:8000/author
http://127.0.0.1:8000/book
http://127.0.0.1:8000/order
http://127.0.0.1:8000/user
```

which will return pages with the appropriate `HTML`

Example of minimal template:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>This is author/book/order/user app page! Congratulations!</h1>
</body>
</html>
```