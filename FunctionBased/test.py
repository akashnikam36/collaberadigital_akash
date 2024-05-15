import unittest
import json
from unittest.mock import patch, MagicMock
from crud import get_access_token, create_user, get_user, update_user, delete_user

class TestAuth0CRUD(unittest.TestCase):
    def setUp(self):
        self.email = "test@example.com"
        self.password = "password123"
        self.user_id = "auth0|1234567890"
        self.new_email = "new_email@example.com"
        self.token = "mock_access_token"

    @patch("requests.post")
    def test_get_access_token(self, mock_post):
        mock_post.return_value.json.return_value = {"access_token": self.token}
        token = get_access_token()
        self.assertEqual(token, self.token)

    @patch("requests.post")
    def test_create_user(self, mock_post):
        mock_post.return_value.json.return_value = {"user_id": self.user_id}
        user = create_user(self.email, self.password, self.token)
        self.assertEqual(user["user_id"], self.user_id)

    @patch("requests.get")
    def test_get_user(self, mock_get):
        mock_get.return_value.json.return_value = {"email": self.email}
        user = get_user(self.user_id, self.token)
        self.assertEqual(user["email"], self.email)

    @patch("requests.patch")
    def test_update_user(self, mock_patch):
        mock_patch.return_value.json.return_value = {"email": self.new_email}
        user = update_user(self.user_id, self.new_email, self.token)
        self.assertEqual(user["email"], self.new_email)

    @patch("requests.delete")
    def test_delete_user(self, mock_delete):
        mock_delete.return_value.status_code = 204
        status_code = delete_user(self.user_id, self.token)
        self.assertEqual(status_code, 204)

if __name__ == "__main__":
    unittest.main()