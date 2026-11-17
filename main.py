train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]

def count_moods(data):
    happy = 0
    sad = 0

    for sentence,i in data:
        if i == "Happy":
            happy += 1
        elif i == "Sad":
            sad += 1

    return happy, sad

print(count_moods(train_data))

happy_words = [
    "marks", "won", "surprise",
    "tasty", "excited", "selected",
    "learned", "favourite", "party"
]

sad_words = [
    "lost", "failed", "moving",
    "cancelled", "missed", "upset",
    "stopped", "lonely", "rained"
]


def guess_mood(sentence):
    c = ""

    for char in sentence.lower():
        if char.isalnum() or char.isspace():
            c+= char

    words = c.split()

    happy_count = 0
    sad_count = 0

    for word in words:
        if word in happy_words:
            happy_count += 1

        if word in sad_words:
            sad_count += 1

    if happy_count > sad_count:
        return "Happy"
    elif sad_count > happy_count:
        return "Sad"
    else:
        
        return "Sad"

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]


correct = 0

for sentence, actual_mood in practice_data:
    predicted_mood = guess_mood(sentence)

    print("Sentence:", sentence)
    print("Actual mood:", actual_mood)
    print("Predicted mood:", predicted_mood)
    print()

    if predicted_mood == actual_mood:
        correct += 1

accuracy = (correct / len(practice_data)) * 100

print("Correct predictions:", correct)
print("Accuracy:", accuracy, "%")


def learn_scores(data):
    scores = {}

    for sentence, mood in data:

        words = sentence.lower().split()

        for word in words:

            if word not in scores:
                scores[word] = 0

            if mood == "Happy":
                scores[word] += 1

            elif mood == "Sad":
                scores[word] -= 1

    return scores

word_scores = learn_scores(train_data)

print("\nBONUS: LEARNED WORD SCORES")
print(word_scores)

def guess_mood_learned(sentence):

    total_score = 0

    words = sentence.lower().split()

    for word in words:
        total_score += word_scores.get(word, 0)

    if total_score > 0:
        return "Happy"
    else:
        return "Sad"



print("\nBONUS: LEARNED MOOD PREDICTIONS")

correct_learned = 0

for sentence, actual_mood in practice_data:

    predicted_mood = guess_mood_learned(sentence)

    print("Sentence:", sentence)
    print("Actual mood:", actual_mood)
    print("Predicted mood:", predicted_mood)

    if predicted_mood == actual_mood:
        correct_learned += 1

accuracy_learned = (correct_learned / len(practice_data)) * 100

print("Correct predictions:", correct_learned)
print("Learned model accuracy:", accuracy_learned, "%")
