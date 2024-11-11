__all__ = ["settings"]

from starlette.middleware.cors import CORSMiddleware

origins = [
    # Place your origins here #
]
settings = {
    "middleware_class": CORSMiddleware,
    "allow_origins": origins,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
