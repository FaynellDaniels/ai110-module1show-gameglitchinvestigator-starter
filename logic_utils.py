def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

#FIX: Refactored logic into logic_utils.py using agent mode for parse_guess to 
# fix the allowance of negative numbers and non-integer values between the range set by the difficulty level.

def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw:
        return False, None, "Enter a guess."

    try:
        value = int(float(raw))
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    if not low <= value <= high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using agent mode for check_guess 
# to ensure that the guess is compared to the secret number correctly, and returns appropriate
#  messages for winning, too high, or too low guesses.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    guess_value = int(guess)
    secret_value = int(secret)

    if guess_value == secret_value:
        return "Win", "🎉 Correct!"

    if guess_value > secret_value:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
