# Django Lab

My Django Study & Playground Lab!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## 前提

至少需要:

```bash
sudo apt install -y libpq-dev
```

安装 PG:

```bash
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql-14
```

WSL 启动 PG:

```bash
# the services that you currently have running on your WSL distribution
service --status-all

# .zshrc
vi ~/.zshrc
```

添加的内容如下:

```bash
# pg
alias start-pg='sudo service postgresql start'
alias run-pg='sudo -u postgres psql'
```

设置初始密码:

```bash
sudo -u postgres psql postgres
```

```postgresql
\password postgres
#输入密码两次
\q
```

修改 `pg_hba.conf` 以使用 `createdb`:

```bash
sudo vi /etc/postgresql/14/main/pg_hba.conf
```

改为:

```
local   all             postgres                                md5
```

重启:

```bash
sudo service postgresql restart
```

## Project 初始化

> 📚️**Reference:**
>
> [Getting Up and Running Locally — Cookiecutter Django 2023.2.1 documentation (cookiecutter-django.readthedocs.io)](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html)

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

pre-commit:

```bash
pre-commit install
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
python -m pip install --upgrade pip
python -m pip install -r requirements/local.txt
```

### 创建一个新的 PostgreSQL database

```bash
createdb --username=postgres <project_slug> # django_lab
```

### 设置 Database 相关的 Env

```bash
$ export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>
# Optional: set broker URL if using Celery
$ export CELERY_BROKER_URL=redis://localhost:6379/0
```

### 设置其他 Env

为了帮助设置环境变量:

在项目的根目录下创建一个`.env`文件，并在其中定义所需的所有变量。然后你只需要在你的机器中设置`DJANGO_READ_DOT_ENV_FILE=True`，所有的变量都会被读取。

### Apply migrations

```bash
python manage.py migrate
```

### Runserver

WSGI:

```bash
python manage.py runserver 0.0.0.0:8000
```

ASGI:

```bash
uvicorn config.asgi:application --host 0.0.0.0 --reload --reload-include '*.html'
```

### startapp

> 📚️**Reference:**
>
> [New apps created are located in the project root, not inside the project slug · Issue #1725 · cookiecutter/cookiecutter-django (github.com)](https://github.com/cookiecutter/cookiecutter-django/issues/1725)

1. 使用 `python manage.py startapp` 创建 app:  `<name-of-the-app>`
2. 移动 `<name-of-the-app>` 目录到 `<project_slug>` 目录
3. 编辑 `<project_slug>/<name-of-the-app>/apps.py` 并修改 `name = "<name-of-the-app>"` 为 `name = "<project_slug>.<name-of-the-app>"`
4. 在你的 [`LOCAL_APPS` on `config/settings/base.py`](https://github.com/pydanny/cookiecutter-django/blob/175381213672b409f940730c2bafc129815d5595/{{cookiecutter.project_slug}}/config/settings/base.py#L79), 添加 `"<project_slug>.<name-of-the-app>.apps.<NameOfTheAppConfigClass>",`

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

## Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers. Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
