from os import environ

from .default import DefaultSettings


def get_settings() -> DefaultSettings:
    env = environ.get("ENV", "default")
    if env == "default":
        return DefaultSettings()
    # ...
    # space for other settings
    # ...
    return DefaultSettings()  # fallback to default


__all__ = [
    "get_settings",
]
