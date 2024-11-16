from datetime import datetime, timezone

DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"


def utcnow() -> datetime:
    return now(timezone.utc)


def now(tz: timezone):
    return datetime.now(tz=tz).replace(tzinfo=None)


def str_utcnow(_: str = DEFAULT_FORMAT):
    return utcnow().strftime(_)


def str_now(tz: timezone, _: str = DEFAULT_FORMAT):
    return now(tz).strftime(_)


# def strf(delta: timedelta, _: str = DEFAULT_FORMAT):
#     return datetime(delta.total_seconds()).strftime(_)
