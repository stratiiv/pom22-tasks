import json
from http.server import HTTPServer, BaseHTTPRequestHandler

import jsonschema.exceptions
from jsonschema import validate

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]
obj_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "username": {"type": "string"},
            "firstName": {"type": "string"},
            "lastName": {"type": "string"},
            "email": {"type": "string"},
            "password": {"type": "string"}
        },
        "required": ["id", "username", "firstName", "lastName", "email", "password"]
    }
arr_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "username": {"type": "string"},
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "email": {"type": "string"},
                "password": {"type": "string"}
            },
            "required": ["id", "username", "firstName", "lastName", "email", "password"]
        }
    }
put_schema={
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["username", "firstName", "lastName", "email", "password"]
}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself
    def do_GET(self):
        global USERS_LIST
        if self.path=='/users':
            self._set_response(body=USERS_LIST)
        elif self.path=='/reset':
            reset = {
                    "id": 1,
                    "username": "theUser",
                    "firstName": "John",
                    "lastName": "James",
                    "email": "john@email.com",
                    "password": "12345",
                }
            USERS_LIST.clear()
            USERS_LIST.append(reset)
            self._set_response(418)
        elif self.path.startswith('/user/'):
            username=self.path.split('/')[-1]
            user_found=False
            for user in USERS_LIST:
                if user['username'] == username:
                    user_found = True
                    self._set_response(body=user)
                    break
            if user_found==False:
                self._set_response(400, {"error": "User not found"})
        else:
            self._set_response(418)

    def do_POST(self):
        try:
            global USERS_LIST
            body = self._pars_body()
            if self.path=='/user':
                validate(body,obj_schema)
                if body['id'] in [user['id'] for user in USERS_LIST]:
                    self._set_response(400,{})
                else:
                    USERS_LIST.append(body)
                    self._set_response(201,body)
            elif self.path=='/user/createWithList':
                validate(body,arr_schema)
                id_exists=False
                for obj in body:
                    if obj['id'] in [user['id'] for user in USERS_LIST]:
                        id_exists=True
                        break
                if id_exists:
                    self._set_response(400, {})
                else:
                    USERS_LIST.extend(body)
                    self._set_response(201,body)

        except jsonschema.exceptions.ValidationError:
            self._set_response(400,{})


    def do_PUT(self):
        global USERS_LIST
        body=self._pars_body()
        try:
            validate(body,put_schema)
        except jsonschema.exceptions.ValidationError:
            self._set_response(400,{"error": "not valid request data"})
        else:
            if self.path.startswith('/user/'):
                id=int(self.path.split('/')[-1])
                id_found=False
                for user in USERS_LIST:
                    if id==user['id']:
                        id_found=True
                        user['username']=body['username']
                        user['firstName'] = body['firstName']
                        user['lastName'] = body['lastName']
                        user['email'] = body['email']
                        user['password'] = body['password']
                        break
                if id_found:
                    self._set_response(200, user)
                else:
                    self._set_response(404,{"error": "User not found"})

    def do_DELETE(self):
        if self.path.startswith('/user/'):
            id=int(self.path.split('/')[-1])
            if id in [user['id'] for user in USERS_LIST]:
                self._set_response(200,{})
            else:
                self._set_response(404,{"error": "User not found"})

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
