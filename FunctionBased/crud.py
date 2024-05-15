import requests
import json
from getpass import getpass

# Auth0 credentials and settings
AUTH0_DOMAIN = 'dev-8rxv0ifihijphc75.us.auth0.com'
AUTH0_CLIENT_ID = 'Vcw87egL0WEIyjGcEO0p0PI9zYSyNfMI'
AUTH0_CLIENT_SECRET = 'l7Li0vnP8LtEio_uKsATma8SYqIr2kgRfX1UscbtoEkhg7Q9BnXLC1WfgfJSxJQL'
AUTH0_CONNECTION = 'Username-Password-Authentication'
AUTH0_AUDIENCE = f'https://{AUTH0_DOMAIN}/api/v2/'
AUTH0_TOKEN_URL = f'https://{AUTH0_DOMAIN}/oauth/token'

def get_access_token():
    payload = {
        'client_id': AUTH0_CLIENT_ID,
        'client_secret': AUTH0_CLIENT_SECRET,
        'audience': AUTH0_AUDIENCE,
        'grant_type': 'client_credentials'
    }
    response = requests.post(AUTH0_TOKEN_URL, json=payload)
    return response.json().get('access_token')

def create_user(email, password, token):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = {
        'email': email,
        'password': password,
        'connection': AUTH0_CONNECTION
    }
    response = requests.post(f'{AUTH0_AUDIENCE}users', headers=headers, data=json.dumps(data))
    return response.json()

def get_user(user_id, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{AUTH0_AUDIENCE}users/{user_id}', headers=headers)
    return response.json()

def update_user(user_id, new_email, token):
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data = {'email': new_email}
    response = requests.patch(f'{AUTH0_AUDIENCE}users/{user_id}', headers=headers, data=json.dumps(data))
    return response.json()

def delete_user(user_id, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(f'{AUTH0_AUDIENCE}users/{user_id}', headers=headers)
    return response.status_code

# Main function
def main():
    token = get_access_token()
    print("TOKEN=>", token)

    while True:
        print("\nChoose an option:")
        print("1. Create user")
        print("2. Get user details")
        print("3. Update user email")
        print("4. Delete user")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter Email: ")
            password = getpass("Password: ")
            new_user = create_user(email, password, token)
            print("Created user:", new_user)
        elif choice == '2':
            user_id = input("Enter user ID: ")
            user_details = get_user(user_id, token)
            print("User details:", user_details)
        elif choice == '3':
            user_id = input("Enter user ID: ")
            new_email = input("Enter new email: ")
            updated_user = update_user(user_id, new_email, token)
            print("Updated user:", updated_user)
        elif choice == '4':
            user_id = input("Enter user ID: ")
            status_code = delete_user(user_id, token)
            if status_code == 204:
                print("User deleted successfully")
            else:
                print("Failed to delete user")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()