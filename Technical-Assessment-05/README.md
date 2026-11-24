# Sentiment Analysis using TextBlob

A simple Python program that classifies sentences as **Positive**, **Neutral**, or **Negative** using the [TextBlob](https://textblob.readthedocs.io/) library. Built for a laboratory exercise on Intelligent Systems.

## Features

- Reads 10 sentences typed in by the user
- Measures the sentiment of each sentence using TextBlob's polarity score
- Prints the result for each sentence
- Prints a summary of how many sentences were positive, neutral, and negative

## How It Works

TextBlob's `sentiment` property returns two values:

| Value | Range | Meaning |
|---|---|---|
| Polarity | -1 to 1 | -1 is very negative, 0 is neutral, 1 is very positive |
| Subjectivity | 0 to 1 | 0 is factual, 1 is opinion-based |

This program uses **polarity** only:

| Polarity (`p`) | Sentiment |
|---|---|
| `p < 0` | Negative |
| `p == 0` | Neutral |
| `p > 0` | Positive |

## Requirements

- Python 3.8 or higher
- TextBlob

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Install TextBlob:

   ```bash
   pip install textblob
   ```

3. If you get an error about missing data, download the TextBlob corpora:

   ```bash
   python -m textblob.download_corpora
   ```

## Usage

Run the program:

```bash
python laboratory_technical5.py
```

Type a sentence when prompted. Repeat for all 10 sentences, and the summary appears at the end.

## Sample Output

```
Enter a sentence : I love this class
Positive
Enter a sentence : This is terrible
Negative
Enter a sentence : The table is brown
Neutral
Enter a sentence : What a wonderful day
Positive
Enter a sentence : I hate waiting in traffic
Negative
Enter a sentence : The meeting is at noon
Neutral
Enter a sentence : This food is delicious
Positive
Enter a sentence : That movie was awful
Negative
Enter a sentence : The book is on the shelf
Neutral
Enter a sentence : I am so happy today
Positive

Summary of 10 sentences
Positive: 4
Neutral : 3
Negative: 3
```

## Project Structure

```
.
├── laboratory_technical5.py   # Main program
└── README.md                  # Project documentation
```

## Learning Outcomes

- Demonstrate understanding of Sentiment Analysis
- Design and develop a simple sentiment analysis program using Python

## Limitations

- TextBlob is a simple, rule-based tool, so it can misjudge sarcasm or complex sentences.
- A sentence with no words TextBlob recognizes will be classified as Neutral.

## Author

Your Name  
Course / Section
