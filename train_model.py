import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import os


data_path = 'data/spam.csv'  

labels = []
texts = []

with open(data_path, 'r', encoding='latin-1') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            labels.append(parts[0])
            texts.append(parts[1])

df = pd.DataFrame({'label': labels, 'text': texts})
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB())
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy :", accuracy_score(y_test, y_pred))
print("\nRapport de classification :\n", classification_report(y_test, y_pred))

model_path = 'models/spam_model.pkl'
os.makedirs(os.path.dirname(model_path), exist_ok=True)
joblib.dump(model, model_path)
print(f"\nModèle (pipeline complet) sauvegardé dans '{model_path}'")
