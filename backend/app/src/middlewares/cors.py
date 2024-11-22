__all__ = ["settings"]

from starlette.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:5000",
    # Place your origins here #
]
settings = {
    "middleware_class": CORSMiddleware,
    "allow_origins": origins,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
