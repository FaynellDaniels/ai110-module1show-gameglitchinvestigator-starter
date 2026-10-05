# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The purpose of the game is to have the player guess a randomly generated secret number within a selected difficulty range. The player receives higher or lower hints after each guess and has a limited number of attempts to find the correct number. I found several bugs in the game, including negative numbers being accepted as guesses, the game not restarting without reloading, the normal and hard number ranges being switched, the attempt limits for easy and normal being switched, and the game giving the wrong higher/lower hints when comparing the guess to the secret number. I fixed two of these bugs: the incorrect higher/lower hints and the input validation that allowed negative numbers. I also tested the fixes with pytest and by entering different guesses in the game to make sure the changes worked correctly.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 12.
2. Game returns "Go HIGHER."
3. User enters a guess of 20.
4. Game returns "Go LOWER."
5. User enters a guess of 15.
6. Game returns "Go LOWER."
7. User enters a guess of 11.
8. Game returns "Go HIGHER."
9. User enters a guess of 14.
10. Game returns "Go LOWER."
11. The user runs out of attempts, and the game displays "Out of attempts. The secret was 13."


## 🧪 Test Results

```
# pytest output:
================================== test session starts ===================================
platform darwin -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/nellie/Documents/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 10 items                                                                       

tests/test_game_logic.py ......                                                    [100%]

=================================== 10 passed in 0.03s ===================================
```




