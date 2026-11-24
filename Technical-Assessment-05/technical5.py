from textblob import TextBlob

positive = 0
neutral = 0
negative = 0

for i in range(10):
    sentence = input("Enter a sentence : ")
    s = TextBlob(sentence)
    p = s.sentiment.polarity

    # Negative p<0, Neutral p=0, Positive p>0
    if p < 0:
        print("Negative")
        negative += 1
    elif p == 0:
        print("Neutral")
        neutral += 1
    elif p > 0 and p <= 1:
        print("Positive")
        positive += 1

print("\nSummary of 10 sentences")
print("Positive:", positive)
print("Neutral :", neutral)
print("Negative:", negative)
