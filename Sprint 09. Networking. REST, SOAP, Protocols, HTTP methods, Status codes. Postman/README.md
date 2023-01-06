# SimpleHTTPRequestHandler

## Run tests

`python -m unittest tests.py`

## Tasks

### update `do_GET` method:

- if url `/reset` reset list `USERS_LIST` to

   ```python
   [   
       {
           "id": int,
           "username": str,
           "firstName": str,
           "lastName": str,
           "email": str,
           "password": str,
       }
   ]
   ```

- if url `/users` returns a json response that contains all users
- if url `/user/{username}` returns a json response that contains all the user data with the corresponding `username`,
  if such a user does not exist then return the status code `400` and json

   ```json
   {
        "error": "User not found"
   }
   ``` 

### update `do_POST` method:

- the request body is valid if it has such a structure
    ```json
    {
             "id": int,
             "username": str,
             "firstName": str,
             "lastName": str,
             "email": str,
             "password": str
    }
    ```

  or

    ```json
     [
             {
                 "id": int,
                 "username": str,
                 "firstName": str,
                 "lastName": str,
                 "email": str,
                 "password": str
             },
             ...
     ] 
    ```
  if body not valid return status code `400` and empty json
- if url `/user` add user to list `USERS_LIST` and return status code `201` and this user, if id already exists then
  return status code `400` and empty json
- if url `/createWithList` add users to list `USERS_LIST` and return status code `201` and these users, if at least some
  id already exists then return status code `400` and empty json

### update `do_PUT` method:

the request body is valid if it has such a structure

```json
{
  "username": str,
  "firstName": str,
  "lastName": str,
  "email": str,
  "password": str
}
```

if url `/user/{id}`

- if update user in list `USERS_LIST` and return status code `200` and this user
- if request data not valid return status code `400` and json
  ```json
  {
    "error": "not valid request data"
  }
  ```
- if id already exists return status code `404` and json
  ```json
  {
    "error": "User not found"
  }
  ```

### update `do_DELETE` method:

- if url `/user/{id}` return status code `200` and empty json else status code `404` and json
  ```json
  {
    "error": "User not found"
  }
  ```

