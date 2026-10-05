import pytest

from logic_utils import parse_guess


@pytest.mark.parametrize(
    ("raw_guess", "low", "high"),
    [
        ("21", 1, 20),
        ("101", 1, 100),
        ("51", 1, 50),
        ("-1", 1, 20),
    ],
)
def test_parse_guess_rejects_values_outside_difficulty_range(
    raw_guess, low, high
):
    assert parse_guess(raw_guess, low, high) == (
        False,
        None,
        f"Guess must be between {low} and {high}.",
    )
