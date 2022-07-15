import glob

POSITIVE = "M03\\data\\aclImdb\\train\\pos\\*txt"
NEGATIVE = "M03\\data\\aclImdb\\train\\neg\\*txt"

positive = glob.glob(POSITIVE)
negative = glob.glob(NEGATIVE)

# Load and parse positive reviews
pos=[]
for pos_comment in positive:  
    with open(pos_comment, encoding="utf8") as stream:
        positive_raw = stream.read()
        words = positive_raw.lower().replace("<br />", "").split()
        positive_com = pos.append(words)

# Load and parse negative reviews
neg = []
for neg_comment in negative:  
    with open(neg_comment, encoding="utf8") as stream:
        negative_raw = stream.read()
        words = negative_raw.lower().replace("<br />", "").split()
        negative_com = neg.append(words)

# Get sentence
sentence = input("Your comment: ")
words = sentence.lower().replace("<br />","").replace(".","").split()

# word's sentiment
sentence_sentiment = 0
for word in words:
    pos_count = 0
    neg_count = 0
    for positive in pos:
        if word in positive:
            pos_count += 1
    for negative in neg:
        if word in negative:
            neg_count +=1
    all_ = pos_count + neg_count
    if all_ != 0:
        sentiment = (pos_count - neg_count) /all_
    else:
        sentiment = 0.0
    print(word, sentiment)
    sentence_sentiment += sentiment
sentence_sentiment /= len(words)

# Comment's grade
if sentence_sentiment > 0:
    label = "positive"
else:
    label = "negative"

print("This comment is ", label, "sentiment =", sentence_sentiment)
