from logging.config import fileConfig

from sqlalchemy import create_engine

from alembic import context

config = context.config

import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from app.core.settings import metadata
from app.core.config import settings
import app.models.base


fileConfig(config.config_file_name)

target_metadata = metadata


def run_migrations_offline():
    context.configure(
        url=settings.SQLITE_URI,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(settings.SQLITE_URI)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            user_module_prefix="sa.",
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
