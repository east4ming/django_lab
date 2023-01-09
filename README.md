# Django Lab

My Django Study & Playground Lab!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Project 初始化

### cookiecutter-django

```bash
pip install "cookiecutter>=1.7.0"
cookiecutter https://github.com/cookiecutter/cookiecutter-django
```

```json
{
  "cookiecutter": {
    "project_name": "Django Lab",
    "project_slug": "django_lab",
    "description": "My Django Study & Playground Lab!",
    "author_name": "Casey Cui",
    "domain_name": "django-lab.ewhisper.cn",
    "email": "cuikaidong@foxmail.com",
    "version": "0.1.0",
    "open_source_license": "MIT",
    "timezone": "Asia/Shanghai",
    "windows": "n",
    "use_pycharm": "n",
    "use_docker": "y",
    "postgresql_version": "14",
    "cloud_provider": "None",
    "mail_service": "Other SMTP",
    "use_async": "y",
    "use_drf": "y",
    "frontend_pipeline": "None",
    "use_celery": "y",
    "use_mailhog": "n",
    "use_sentry": "n",
    "use_whitenoise": "y",
    "use_heroku": "n",
    "ci_tool": "Github",
    "keep_local_envs_in_vcs": "y",
    "debug": "y",
    "_template": "https://github.com/cookiecutter/cookiecutter-django",
    "_output_dir": "/home/casey/Projects/django-lab"
  }
}
```

### VSCode

添加 vscode workspace: `.vscode/django_lab.code-workspace`

### pyenv venv

```bash
PYENV_VERSION=3.10.8

python -m venv .venv
source .venv/bin/activate
```

### 安装依赖

```bash
sudo apt install -y libpq-dev

python -m pip install --upgrade pip
python -m pip install -r requirements/local.txt
```

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy django_lab

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd django_lab
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
