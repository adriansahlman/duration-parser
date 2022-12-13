import pytest

import duration_parser


NANOSECONDS = 1
MICROSECOND = 10 ** 3 * NANOSECONDS
MILLISECOND = 10 ** 3 * MICROSECOND
SECOND = 10 ** 3 * MILLISECOND
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY


@pytest.mark.parametrize(
    'duration,nanoseconds',
    (
        ('1d', DAY),
        ('1 d', DAY),
        ('1 day', DAY),
        ('1 days', DAY),
        ('1days', DAY),
        ('0.5d', DAY // 2),
        ('1hr2m', HOUR + 2 * MINUTE),
        ('1hours2m', HOUR + 2 * MINUTE),
        ('1hours,2m', HOUR + 2 * MINUTE),
        ('1hours, 2minute', HOUR + 2 * MINUTE),
    )
)
def test_parse_nanoseconds(
    duration: str,
    nanoseconds: int,
) -> None:
    parsed_nanoseconds = duration_parser.parse_nanoseconds(duration)
    assert parsed_nanoseconds == nanoseconds, \
        f'{parsed_nanoseconds} != {nanoseconds}'
