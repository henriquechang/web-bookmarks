from django.contrib.auth.models import User
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from api.models.bookmark import Bookmark

fake = Faker()


class TestAPI(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='test')
        self.user_2 = User.objects.create(username='test2')

    def test_post_unauthorized(self):
        response = self.client.post('/bookmark')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_unauthorized(self):
        response = self.client.delete('/bookmark/1')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_unauthorized(self):
        response = self.client.patch('/bookmark/1')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_authorized_missing_fields(self):
        self.client.force_authenticate(self.user)
        response = self.client.post('/bookmark')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_authorized_valid_fields(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': fake.pybool()
        }
        response = self.client.post('/bookmark', data)
        bookmark = Bookmark.objects.get(id=1)
        self.assertEqual(bookmark.title, data.get('title'))
        self.assertEqual(bookmark.url, data.get('url'))
        self.assertEqual(bookmark.is_public, data.get('isPublic'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch_authorized_valid_fields(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': fake.pybool()
        }
        self.client.post('/bookmark', data)
        updated_data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': fake.pybool()
        }
        response = self.client.patch('/bookmark/1', updated_data)
        bookmark = Bookmark.objects.get(id=1)
        self.assertEqual(bookmark.title, updated_data.get('title'))
        self.assertEqual(bookmark.url, updated_data.get('url'))
        self.assertEqual(bookmark.is_public, updated_data.get('isPublic'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_authorized_valid_fields(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': fake.pybool()
        }
        self.client.post('/bookmark', data)
        response = self.client.delete('/bookmark/1')
        with self.assertRaises(Exception):
            Bookmark.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_authorized_different_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': fake.pybool()
        }
        self.client.post('/bookmark', data)
        self.client.force_authenticate(self.user_2)
        updated_data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': fake.pybool()
        }
        response = self.client.patch('/bookmark/1', updated_data)
        bookmark = Bookmark.objects.get(id=1)
        self.assertEqual(bookmark.title, data.get('title'))
        self.assertEqual(bookmark.url, data.get('url'))
        self.assertEqual(bookmark.is_public, data.get('isPublic'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_authorized_different_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': fake.pybool()
        }
        self.client.post('/bookmark', data)
        self.client.force_authenticate(self.user_2)
        response = self.client.delete('/bookmark/1')
        bookmark = Bookmark.objects.get(id=1)
        self.assertEqual(bookmark.title, data.get('title'))
        self.assertEqual(bookmark.url, data.get('url'))
        self.assertEqual(bookmark.is_public, data.get('isPublic'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_nonexistent_bookmarks(self):
        response = self.client.get('/bookmarks')
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_public_bookmarks_same_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': True
        }
        self.client.post('/bookmark', data)
        response = self.client.get('/bookmarks')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_public_bookmarks_different_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': True
        }
        self.client.post('/bookmark', data)
        self.client.force_authenticate(self.user_2)
        response = self.client.get('/bookmarks')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_private_bookmarks_same_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': False
        }
        self.client.post('/bookmark', data)
        response = self.client.get('/bookmarks')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_private_bookmarks_different_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': False
        }
        self.client.post('/bookmark', data)
        self.client.force_authenticate(self.user_2)
        response = self.client.get('/bookmarks')
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nonexistent_bookmark(self):
        response = self.client.get('/bookmark/1')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_public_bookmark_same_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': True
        }
        self.client.post('/bookmark', data)
        response = self.client.get('/bookmark/1')
        bookmark = Bookmark.objects.get(id=1)
        self.assertEqual(bookmark.title, data.get('title'))
        self.assertEqual(bookmark.url, data.get('url'))
        self.assertEqual(bookmark.is_public, data.get('isPublic'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_public_bookmark_different_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': True
        }
        self.client.post('/bookmark', data)
        self.client.force_authenticate(self.user_2)
        response = self.client.get('/bookmark/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_private_bookmark_same_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': False
        }
        self.client.post('/bookmark', data)
        response = self.client.get('/bookmark/1')
        bookmark = Bookmark.objects.get(id=1)
        self.assertEqual(bookmark.title, data.get('title'))
        self.assertEqual(bookmark.url, data.get('url'))
        self.assertEqual(bookmark.is_public, data.get('isPublic'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_private_bookmark_different_user(self):
        self.client.force_authenticate(self.user)
        data = {
            'title': fake.pystr(),
            'url': fake.url(),
            'isPublic': False
        }
        self.client.post('/bookmark', data)
        self.client.force_authenticate(self.user_2)
        response = self.client.get('/bookmark/1')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
