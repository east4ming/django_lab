import pytest
from django.contrib.auth.models import Group, Permission

from django_lab.users.models import User

# from django.test import TestCase


# class MyTest(TestCase):
#     fixtures = ["group.json"]

#     def test_should_create_group(self):
#         group = Group.objects.get(pk=1)
#         self.assertEqual(group.name, "appusers")


# def test_should_create_user_with_username(db) -> None:
#     user = User.objects.create_user("Haki")
#     assert user.username == "Haki"


@pytest.fixture
def user_A(db) -> User:
    group = Group.objects.create(name="app_user")
    change_user_permissions = Permission.objects.filter(
        codename=["change_user", "view_user"],
    )
    group.permissions.add(*change_user_permissions)
    user = User.objects.create_user("A")
    user.groups.add(group)
    return user


def test_should_create_user(user_A: User) -> None:
    assert user_A.username == "A"


def test_user_is_in_app_user_group(user_A: User) -> None:
    assert user_A.groups.filter(name="app_user").exists()


def test_should_check_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    assert user_A.check_password("secret") is True


def test_should_not_check_unusable_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    user_A.set_unusable_password()
    assert user_A.check_password("secret") is False
