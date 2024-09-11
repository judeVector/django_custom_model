from django.test import TestCase
from unittest import mock
from django.contrib.auth import get_user_model

from manage import main

User = get_user_model()


# Create your tests here.
class UserAccountTests(TestCase):

    def test_new_superuser(self):
        super_user = User.objects.create_superuser(
            user_name="testuser",
            email="testuser@example.com",
            first_name="testuser",
            password="testuserpassword",
        )
        self.assertEqual(super_user.email, "testuser@example.com")
        self.assertEqual(super_user.user_name, "testuser")
        self.assertEqual(super_user.first_name, "testuser")
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "testuser")

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                user_name="testuser",
                email="testuser@example.com",
                first_name="testuser",
                password="testuserpassword",
                is_superuser=False,
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                user_name="testuser",
                email="testuser@example.com",
                first_name="testuser",
                password="testuserpassword",
                is_staff=False,
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                user_name="testuser",
                email="testuser@super.com",
                first_name="testuser",
                password="testuserpassword",
                is_active=False,
            )

    def test_new_user(self):
        user = User.objects.create_user(
            user_name="testuser",
            email="testuser@user.com",
            first_name="testuser",
            password="testuserpassword",
        )
        self.assertEqual(user.email, "testuser@user.com")
        self.assertEqual(user.user_name, "testuser")
        self.assertEqual(user.first_name, "testuser")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        self.assertEqual(str(user), "testuser")

        with self.assertRaises(ValueError):
            user = User.objects.create_user(
                user_name="testuser",
                email="",
                first_name="testuser",
                password="testuserpassword",
            )
