## Project Description
This project is a simple Python-based Mood Guesser that predicts whether a sentence expresses a Happy or Sad mood.

## Level 1 – Mood Counting
The `count_moods()` function counts the number of Happy and Sad sentences in the training dataset.

## Level 2 – Manual Mood Prediction
The `guess_mood()` function predicts the mood using manually selected Happy and Sad words.

**Tie-breaker:** When both counts are equal, the prediction is Sad.

## Level 3 – Practice Testing
The program tests five practice sentences and calculates prediction accuracy.

## Optional Bonus – Automatic Word Scoring
The `learn_scores()` function automatically calculates word scores from the training data.

The `guess_mood_learned()` function uses these scores to predict the mood of a sentence.

## Learning Notes
1. The score of "good party today" is calculated by adding the scores of all three words.
2. The score of "bad exam day" is calculated by adding the scores of all three words.
3. The word "exam" has a score of zero when its Happy and Sad occurrences are equal.
4. "Not good" may be incorrectly predicted as Happy because the basic word-scoring method does not understand negation. It can be improved by handling words such as "not".

## AI Declaration
I used ChatGPT as an AI learning assistant to understand Python concepts and clarify errors. I reviewed and tested the code to understand how it works.

## Reflection
Through this project, I learned about Python functions, loops, lists, tuples, dictionaries, word scoring, and basic mood prediction.

## Optional Bonus – Voice Note

Voice note explaining my guess_mood() function:
https://1drv.ms/v/c/fbcb3c538efd0724/IQCmNL5xrTO-T6BXzR3C8FZ6AQ-Eyz_Rvo6vrIa6nKlWj-8?e=CqaJKI
