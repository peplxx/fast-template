from os import path as os_path
from pathlib import Path
from types import SimpleNamespace
from typing import Union

from alembic.config import Config
from configargparse import Namespace

from app.config import get_settings


PROJECT_PATH = Path(__file__).parent.parent.resolve()


def make_alembic_config(
    cmd_opts: Union[Namespace, SimpleNamespace], base_path: Path = PROJECT_PATH
) -> Config:
    """
    Creates an alembic configuration object based on command line arguments,
    replaces relative paths with absolute ones.
    """
    database_uri = get_settings().database_uri_sync

    path_to_folder = cmd_opts.config
    # Replace alembic.ini file path with absolute path
    if not os_path.isabs(cmd_opts.config):
        cmd_opts.config = os_path.join(base_path, cmd_opts.config + "alembic.ini")

    config = Config(file_=cmd_opts.config, ini_section=cmd_opts.name, cmd_opts=cmd_opts)

    # Replace alembic folder path with absolute path
    alembic_location = config.get_main_option("script_location")
    if not os_path.isabs(alembic_location):
        config.set_main_option(
            "script_location",
            os_path.join(base_path, path_to_folder + alembic_location),
        )
    if cmd_opts.pg_url:
        config.set_main_option("sqlalchemy.url", database_uri)

    return config
