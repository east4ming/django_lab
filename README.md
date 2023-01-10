# Django Lab

My Django Study & Playground Lab!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![CI](https://github.com/east4ming/django_lab/actions/workflows/ci.yml/badge.svg)](https://github.com/east4ming/django_lab/actions/workflows/ci.yml)

License: MIT

## Project 初始化 - 本地环境开发

> 📚️**Reference:**
>
> [Getting Up and Running Locally — Cookiecutter Django 2023.2.1 documentation (cookiecutter-django.readthedocs.io)](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html)

### 前提

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

### cookiecutter-django

```bash
pyenv shell 3.10.9
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
    "use_mailhog": "y",
    "use_sentry": "n",
    "use_whitenoise": "y",
    "use_heroku": "n",
    "ci_tool": "Github",
    "keep_local_envs_in_vcs": "y",
    "debug": "n",
    "_template": "https://github.com/cookiecutter/cookiecutter-django",
    "_output_dir": "/home/casey/Projects"
  }
}
```

pre-commit:

```bash
pyenv local 3.10.9
python -m pip install pre-commit
pre-commit install
```

### VSCode

添加 vscode workspace: `.vscode/django_lab.code-workspace`

### pyenv venv

```bash
PYENV_VERSION=3.10.9

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

## Project 初始化 - 本地容器开发

> 📚**Reference:**
>
> [Getting Up and Running Locally With Docker — Cookiecutter Django 2023.2.1 documentation (cookiecutter-django.readthedocs.io)](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)

### 前提

- Docker
- Docker Compose
- Pre-commit
- Cookiecutter

### Cookiecutter

```bash
cookiecutter gh:cookiecutter/cookiecutter-django
```

### 构建容器

```bash
docker-compose -f local.yml build
```

通常，如果想要模拟生产环境，请使用 `production.yml` 代替。这对于您可能需要执行的任何其他操作都是正确的:只要需要切换，就执行它!

```bash
git init

pyenv shell system
pip install pre-commit
pre-commit install
```

### 运行容器

```bash
docker-compose -f local.yml up
```

也可以这样:

```bash
export COMPOSE_FILE=local.yml
docker-compose up
```

后台运行:

```bash
docker-compose up -d
```

### 执行管理命令

因为是一次性的, 所以需要加上 `docker-compose -f local.yml run --rm`

```bash
docker-compose -f local.yml run --rm django python manage.py migrate
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

上面的 2 个命令第一次运行时是需要执行的.

`django` 是目标 service

### (可选)指定 Docker 开发服务器 IP

当 `DEBUG` 设置为 `True` 时，主机将根据 `['localhost', '127.0.0.1', '[::1]']` 进行验证。这在运行 `virtualenv` 时就足够了。对于 Docker，在 `config.settings.local` 里, 将您的主机开发服务器 IP 添加到 INTERNAL_IPS 或 ALLOWED_HOSTS(如果变量存在)。

### 配置环境

这是从项目的 `local.yml` 中摘录的:

```yaml
# ...

postgres:
  build:
    context: .
    dockerfile: ./compose/production/postgres/Dockerfile
  volumes:
    - local_postgres_data:/var/lib/postgresql/data
    - local_postgres_data_backups:/backups
  env_file:
    - ./.envs/.local/.postgres

# ...
```

现在对我们来说最重要的事情是 `env_file` 部分征募 `./.envs/.local/.postgres`。通常，堆栈的行为是由一些环境变量(简称env)在`envs/`，例如，这是我们为您生成的:

```
.envs
├── .local
│   ├── .django
│   └── .postgres
└── .production
    ├── .django
    └── .postgres
```

根据约定，对于环境 `e` 中的任何服务 `sI` (您知道在项目根目录中有一个 `somenv.yml` 文件时，`somenv` 是一个环境) ，如果 `sI` 需要配置，则会有一个`.envs/.e/.sI` 用于存在 `sI` 服务配置文件。

最后一点:你是否需要合并 `.envs/` 为一个`.env` 文件, 那么需要运行`merge_production_dotenvs_in_dotenv.py`:

```bash
python merge_production_dotenvs_in_dotenv.py
```

然后将创建 `.env` 文件，其中所有生产环境都在里边。

### 提示与技巧

#### 查看日志

```bash
export COMPOSE_FILE=local.yml
docker-compose logs celeryworker
docker-compose top celeryworker
```

#### Mailhog

Mailhog 地址为: <http://127.0.0.1:8025>

#### 文档

文档地址为: <http://127.0.0.1:9000>

更新文档:

```bash
docker-compose -f local.yml up docs
```

#### Celery & Flower

Flower 地址为: <http://localhost:5555/>

#### Pytest

```bash
docker-compose -f local.yml run --rm django pytest
```

#### Coverage

```bash
docker-compose -f local.yml run --rm django coverage run -m pytest
docker-compose -f local.yml run --rm django coverage report
```

#### PG 备份

创建备份:

```bash
docker-compose -f local.yml exec postgres backup
```

> ⚠️**Warning:**
> 脚本不支持 PG 用户为: `postgres`

查看已存在的备份:

```bash
docker-compose -f local.yml exec postgres backups
```

复制备份到本地:

```bash
docker-compose cp postgres:/backups ./backups
```

恢复数据:

```bash
docker-compose -f local.yml exec postgres restore backup_2018_03_13T09_05_07.sql.gz
```

备份到 AWS S3:

```bash
docker-compose -f production.yml run --rm awscli upload
docker-compose -f production.yml run --rm awscli download backup_2018_03_13T09_05_07.sql.gz
```

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

## Django Startapp

> 📚️**Reference:**
>
> [New apps created are located in the project root, not inside the project slug · Issue #1725 · cookiecutter/cookiecutter-django (github.com)](https://github.com/cookiecutter/cookiecutter-django/issues/1725)

1. 使用 `python manage.py startapp` 创建 app:  `<name-of-the-app>`
2. 移动 `<name-of-the-app>` 目录到 `<project_slug>` 目录
3. 编辑 `<project_slug>/<name-of-the-app>/apps.py` 并修改 `name = "<name-of-the-app>"` 为 `name = "<project_slug>.<name-of-the-app>"`
4. 在你的 [`LOCAL_APPS` on `config/settings/base.py`](https://github.com/pydanny/cookiecutter-django/blob/175381213672b409f940730c2bafc129815d5595/{{cookiecutter.project_slug}}/config/settings/base.py#L79), 添加 `"<project_slug>.<name-of-the-app>.apps.<NameOfTheAppConfigClass>",`

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
