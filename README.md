It looks like you are setting up a brand-new repository for your **Mancala Game** on your `semiculine` account!

Since the repository only has the `mancala_game.py` file so far, here is a professional, fully structured `README.md` tailored specifically for a Python-based Mancala project.

You can copy the code block below and paste it directly into the GitHub text editor on your screen:

```markdown
# Mancala Game

A Python implementation of the classic two-player strategy board game, Mancala. This project handles the traditional game logic, pit management, turn-switching, and stone redistribution.

---

## 🎮 How to Play Mancala

1. **Setup:** The board consists of two rows of 6 small pits (holes) and two large stores (Mancalas) at either end. Each player controls the row of 6 pits closest to them and the Mancala to their right.
2. **Gameplay:** On your turn, choose one of your 6 pits that contains stones. All stones are picked up and deposited one-by-one counter-clockwise into subsequent pits, including your own Mancala (but skipping your opponent's Mancala).
3. **Free Turn:** If your last deposited stone lands in your own Mancala, you immediately get another turn.
4. **Capturing:** If your last deposited stone lands in an empty pit on your side, and the opponent's opposite pit has stones, you capture both your last stone and the opponent's stones, placing them all into your Mancala.
5. **Winning:** The game ends when all 6 pits on one player's side are completely empty. The player with the most stones in their Mancala wins!

---

## 🚀 Features

* **Complete Mancala Rule Enforcement:** Full implementation of standard rules including the "free turn" on Mancala landing and the "opposite side capture" mechanic.
* **Turn-Based State Machine:** Robust state tracking to seamlessly alternate turns between Player 1 and Player 2.
* **Console-Based Board UI:** A clean, text-based visual representation of the board state updated dynamically after every move.
* **Input Validation:** Built-in error handling to prevent players from selecting empty pits or pits belonging to their opponent.

---

## 🛠️ Technical Details

* **Language:** Python 3.x
* **Data Structure:** The board is represented efficiently using an array/list where specific indices map to each player's pits and stores, enabling smooth $O(1)$ calculations for stone distribution.

---

## 📦 How to Run

### Prerequisites
Make sure you have Python 3 installed on your machine.

### Execution
1. Clone your repository to your local machine:
   ```bash
   git clone [https://github.com/semiculine/mancala_game.git](https://github.com/semiculine/mancala_game.git)

```

2. Navigate into the directory:
```bash
cd mancala_game

```


3. Run the game script:
```bash
python mancala_game.py
