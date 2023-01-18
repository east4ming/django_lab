import pytest
from django.contrib.auth.models import Group, Permission

from django_lab.users.models import User


@pytest.fixture
def app_user_group(db) -> Group:
    group = Group.objects.create(name="app_user")
    change_user_permissions = Permission.objects.filter(
        codename=["change_user", "view_user"],
    )
    group.permissions.add(*change_user_permissions)
    return group


@pytest.fixture
def app_user_factory(db, app_user_group: Group):
    # Closure
    def create_app_user(
        username: str,
        password: str | None = None,
        email: str | None = "foo@bar.com",
        is_staff: bool = False,
        is_superuser: bool = False,
        is_active: bool = True,
        groups: list[Group] = [],
    ) -> User:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        user.groups.add(app_user_group)
        # Add additional groups, if provided
        user.groups.add(*groups)
        return user

    return create_app_user


@pytest.fixture
def user_A(db, app_user_factory) -> User:
    return app_user_factory("A")


@pytest.fixture
def user_B(db, app_user_factory) -> User:
    return app_user_factory("B")


def test_should_create_user(user_A: User, app_user_group: Group) -> None:
    assert user_A.username == "A"
    assert user_A.email == "foo@bar.com"


def test_should_create_user_in_app_user_group(
    user_A: User, app_user_group: Group
) -> None:
    assert user_A.groups.filter(pk=app_user_group.pk).exists()


def test_should_check_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    assert user_A.check_password("secret") is True


def test_should_not_check_unusable_password(db, user_A: User) -> None:
    user_A.set_password("secret")
    user_A.set_unusable_password()
    assert user_A.check_password("secret") is False


def test_should_create_two_users(user_A: User, user_B: User) -> None:
    assert user_A.pk != user_B.pk
