import os
import requests
import json
from flask import Flask, request
from getpass import getpass

# Auth0 credentials and settings
AUTH0_DOMAIN = 'dev-8rxv0ifihijphc75.us.auth0.com'
AUTH0_CLIENT_ID = 'Vcw87egL0WEIyjGcEO0p0PI9zYSyNfMI'
AUTH0_CLIENT_SECRET = 'l7Li0vnP8LtEio_uKsATma8SYqIr2kgRfX1UscbtoEkhg7Q9BnXLC1WfgfJSxJQL'
AUTH0_CONNECTION = 'Username-Password-Authentication'
AUTH0_AUDIENCE = f'https://{AUTH0_DOMAIN}/api/v2/'
AUTH0_TOKEN_URL = f'https://{AUTH0_DOMAIN}/oauth/token'

app = Flask(__name__)

def get_access_token():
    payload = {
        'client_id': AUTH0_CLIENT_ID,
        'client_secret': AUTH0_CLIENT_SECRET,
        'audience': AUTH0_AUDIENCE,
        'grant_type': 'client_credentials'
    }
    response = requests.post(AUTH0_TOKEN_URL, json=payload)
    return response.json().get('access_token')

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    token = get_access_token()
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = {
        'email': email,
        'password': password,
        'connection': AUTH0_CONNECTION
    }
    response = requests.post(f'{AUTH0_AUDIENCE}users', headers=headers, data=json.dumps(data))
    print(response)
    return response.json()

@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    token = get_access_token()
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{AUTH0_AUDIENCE}users/{user_id}', headers=headers)
    return response.json()

@app.route('/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    new_email = data.get('new_email')
    token = get_access_token()
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = {'email': new_email}
    response = requests.patch(f'{AUTH0_AUDIENCE}users/{user_id}', headers=headers, data=json.dumps(data))
    return response.json()

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    token = get_access_token()
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(f'{AUTH0_AUDIENCE}users/{user_id}', headers=headers)
    if response:
        return {'message':"user is deleted successfully "}

if __name__ == '__main__':
    app.run(debug=True)