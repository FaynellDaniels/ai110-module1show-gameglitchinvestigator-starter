# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
  The game opened as a basic number-guessing game where I could select a difficulty and enter guesses. It displayed the number of attempts and gave me a message after each guess telling me whether I should go higher or lower.
  
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
- The game would tell me to go lower even when my guess was lower than the target.
- The game allowed negative numbers to be entered as guesses even though they were outside the valid range.
- The normal and hard difficulty number ranges were switched.
- The attempt limits for the easy and normal difficulties were switched.
- The game would not start a new game without reloading the application.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input    | Expected Behavior | Actual Behavior | Console Output / Error |
| -------- | ----------------- | --------------- | ---------------------- |
| Negative number, such as -5 | The game should reject the input and ask for a valid number within the allowed range.| The game accepts -5 as a guess and continues the game.|No error; negative guess is accepted.|Input validation / guess validation function|
|Guess higher than the target number, such as target 40 and guess 30|The game should tell the player that the guess is too low and to go higher.|The game gives the incorrect direction/hint even though the guess is lower than the target.|Incorrect "go lower" or direction output.|check_guess / guess comparison logic|
| Game completed, then choosing to play again.|A new game should start with a new number and reset attempts.|The game does not restart unless the page is reloaded.|No console error; game remains in the previous state.|Game restart/reset function|



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I gave the AI the bug where the game was giving the wrong high/low hint. The AI identified that the problem was in the check_guess function, where the comparison results and hint messages were reversed. It suggested changing the function so that when the guess is greater than the secret number, it returns "Too High" and tells the player to "Go LOWER!", and when the guess is lower, it returns "Too Low" and tells the player to "Go HIGHER!".

I accepted the suggestion because it directly addressed the bug and the logic matched how a number-guessing game should work. I verified the fix by running pytest and then testing the game with guesses both higher and lower than the target number. The game gave the correct "Go LOWER" or "Go HIGHER" message based on the guess.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I gave the AI the bug involving negative numbers and invalid guesses. The AI originally suggested checking the range using if value < low or value > high:. Although this would work, I felt the code was more complicated than necessary for this section. I asked the AI to simplify the solution, and it changed the condition to if not low <= value <= high:. I used the simplified version because it was easier to read and understand while still checking that the guess was within the allowed range.

I verified my version by running pytest and then testing different inputs in the game, including negative numbers, numbers within the allowed range, and numbers above the maximum. The game correctly rejected numbers outside the allowed range and accepted valid guesses.

---

## 3. Debugging and testing your fixes
- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when the program produced the expected result for the input that originally caused the problem. I also ran the pytest, which checked that a guess below the target returns “Go HIGHER,” a guess above the target returns “Go LOWER,” and a correct guess returns a winning result. The tests also showed that negative guesses and guesses outside the selected difficulty range are rejected. The tests covered Easy, Normal, and Hard ranges, and all 10 tests passed.

AI helped me design and understand the tests by identifying the important edge cases from the original bugs. It explained that I needed to test both the returned outcome and the hint message, not just whether the function ran without an error. It also helped me use separate range values for each difficulty so I could verify that Easy uses 1–20, Normal uses 1–100, and Hard uses 1–50.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain it as Streamlit restarting the script from the top whenever the user interacts with the app, such as entering a guess or clicking a button. Session state allows the app to remember important information, such as the secret number, the user's attempts, and the current game, even though the script is rerunning. Without session state, the game could lose its information and start over every time the user interacts with it.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

One habit I want to reuse is testing my code with different inputs instead of only testing the normal expected case. In this project, testing different values, including values at the boundaries and invalid inputs, helped me find and verify bugs that I might not have noticed otherwise.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time, I would give the AI more specific information about the existing code and ask it to keep the solution as simple as possible from the beginning. I learned that an AI solution can work but still be more complicated than necessary, so I want to review the suggested code and make sure it actually fits my project before using it.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project showed me that AI-generated code can be very useful for finding and fixing bugs, but I should not assume that every suggestion is automatically the best solution. I still need to understand the code, decide whether it fits my project, and test it myself to make sure it works.
