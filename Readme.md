# Flashy - French Flashcard Learning App

Flashy is a simple yet effective flashcard application designed to help users learn French vocabulary. The app displays a French word and allows the user to test their knowledge by showing the English translation after a brief delay. Users can mark words as known or unknown, and the app will save their progress, ensuring a personalized and efficient learning experience.

## Features

- **Random Word Selection:** Displays a random French word from the dataset.
- **Flip Card:** Automatically flips the card to show the English translation after 3 seconds.
- **Known and Unknown Buttons:** Users can mark words as known or unknown. Known words are removed from the dataset.
- **Progress Save:** The app saves the user's progress, so they can continue learning from where they left off.

## Data Handling

- If the `words_to_learn.csv` file is not found, the app will use the original dataset from `french_words.csv`.
- Known words are removed from the dataset and the updated list is saved to `words_to_learn.csv`.

## Getting Started

### Prerequisites

- Python 3.x
- `tkinter` library (included with standard Python distribution)
- `pandas` library

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flashy.git
    cd flashy
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas
    ```

3. Ensure you have the following directory structure:
    ```
    flashy/
    ├── data/
    │   ├── french_words.csv
    ├── images/
    │   ├── card_front.png
    │   ├── card_back.png
    ├── main.py
    ```

### Usage

1. Navigate to the project directory.
2. Run the application:
    ```sh
    python main.py
    ```

### File Structure

- `main.py`: The main script that runs the application.
- `data/french_words.csv`: The original dataset containing French words and their English translations.
- `data/words_to_learn.csv`: The dataset that saves the user's progress.
- `images/card_front.png`: Image for the front of the flashcard.
- `images/card_back.png`: Image for the back of the flashcard.

