import pytest
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


@pytest.fixture
def user_A(db) -> User:
    return User.objects.create_user("A")


def test_should_check_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    assert user_A.check_password("secret") is True


def test_should_not_check_unusable_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    user_A.set_unusable_password()
    assert user_A.check_password("secret") is False
