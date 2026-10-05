from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_guess_below_target_tells_player_to_go_higher():
    result = check_guess(30, "40")

    assert result == ("Too Low", "📈 Go HIGHER!")


def test_parse_guess_rejects_values_outside_range():
    assert parse_guess("-1", 1, 20) == (
        False,
        None,
        "Guess must be between 1 and 20.",
    )
    assert parse_guess("21", 1, 20) == (
        False,
        None,
        "Guess must be between 1 and 20.",
    )


def test_parse_guess_uses_each_difficulty_range():
    assert parse_guess("20", 1, 20) == (True, 20, None)
    assert parse_guess("21", 1, 20)[0] is False

    assert parse_guess("100", 1, 100) == (True, 100, None)
    assert parse_guess("101", 1, 100)[0] is False

    assert parse_guess("50", 1, 50) == (True, 50, None)
    assert parse_guess("51", 1, 50)[0] is False
