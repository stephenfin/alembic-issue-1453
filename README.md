# Reproducer for Alembic issue #1453

https://github.com/sqlalchemy/alembic/issues/1453

## Usage

First, we'll test with Alembic < 1.11. Install that in a virtualenv.

```shell
virtualenv .venv
source .venv/bin/activate
pip install 'alembic<1.11' mysql
```

Now bring up a MySQL instance (this would probably work just fine with SQLite, but SQLite's `ALTER` support is limited so I didn't try that.

```shell
docker-compose up -d
```

> **Note**
> You might need to run `chcon -Rt svirt_sandbox_file_t .` to fix SELinux permission for the directory if using Fedora

Apply migrations.

```shell
alembic upgrade head
```

Now, let's try with Alembic >= 1.11. First, stop and remove the existing MySQL container.

```shell
docker-compose rm -sf db
```

Now upgrade Alembic:

```
pip install --upgrade 'alembic>=1.11'
```

Apply migrations again and observe failures.

```
alembic upgrade head  # this will fail
```
