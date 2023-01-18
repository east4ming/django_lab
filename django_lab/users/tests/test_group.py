from django.contrib.auth.models import Group
from django.test import TestCase

from django_lab.users.models import User


class MyTest(TestCase):
    fixtures = ["group.json"]

    def test_should_create_group(self):
        group = Group.objects.get(pk=1)
        self.assertEqual(group.name, "appusers")


def test_should_create_user_with_username(db) -> None:
    user = User.objects.create_user("Haki")
    assert user.username == "Haki"
