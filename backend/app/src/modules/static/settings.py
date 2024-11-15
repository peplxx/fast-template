

class StaticFileSettings:
    STATIC_FILES_PATH: str = "/tmp/static"

settings: StaticFileSettings = StaticFileSettings()
__all__ = ["settings", "StaticFileSettings"]