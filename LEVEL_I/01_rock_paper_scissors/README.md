# Project: Number Guesser Game

## 🎯 Objective
The objective is to build a CLI-based game that challenges the user to guess a randomly generated number. The system must provide feedback (hints) for incorrect guesses and implement a scoring mechanic where efficiency is rewarded.

## 📋 Functional Requirements
The application must meet the following specifications:

1.  **Random Generation:** The system shall generate a random number within a configurable range (e.g., 1 to 100).
2.  **User Interaction:** The system must prompt the user to input a guess via the terminal.
3.  **Feedback Loop:** For every incorrect guess, the system must provide a directional hint:
    * "Higher" if the target is larger than the guess.
    * "Lower" if the target is smaller than the guess.
4.  **Scoring System:** Each incorrect guess must decrement the user's final score.
5.  **Game Termination:** The loop ends when the user correctly guesses the number or explicitly chooses to quit.
6.  **Input Validation:** User input must be validated to ensure it is an integer within the bounds.

## 🛠️ Architectural Guidelines
To ensure maintainability and scalability, the implementation should adhere to these technical standards:

* **Modularity:** Break down the game logic into distinct modules or functions rather than a single script.
* **Encapsulation:** Use functions or classes to isolate specific behaviors (e.g., `calculate_score()`, `validate_input()`).
* **Component Testing:** Verify individual components (like the scoring algorithm) before full system integration.