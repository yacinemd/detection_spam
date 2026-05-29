# Détection de Spam SMS

Ce projet entraîne un modèle de machine learning pour détecter si un message est **spam** ou **non spam**, puis expose une interface web Flask pour tester des messages.

## Fonctionnalités

- Entraînement d’un pipeline `TF-IDF + Multinomial Naive Bayes`
- Sauvegarde du modèle entraîné dans `models/spam_model.pkl`
- API Flask (`/predict`) pour la prédiction
- Interface web simple pour tester des messages

## Structure du projet

```text
detection_spam/
├── app/
│   ├── app.py
│   ├── static/
│   └── templates/
├── data/
│   └── spam.csv
├── models/
│   ├── spam_model.py
│   └── spam_model.pkl
├── train_model.py
└── requirements.txt
```

## Prérequis

- Python 3.9+ (recommandé)
- pip

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Entraîner le modèle

Depuis la racine du projet :

```bash
python train_model.py
```

Le script lit `data/spam.csv`, entraîne le modèle puis le sauvegarde dans `models/spam_model.pkl`.

## Lancer l’application web

```bash
python app/app.py
```

Puis ouvrir : `http://127.0.0.1:5000`

## Utilisation de l’API

### Endpoint

- `POST /predict`
- Corps JSON :

```json
{
  "text": "Congratulations! You won a free ticket."
}
```

### Réponse

```json
{
  "prediction": 1,
  "score": 0.98
}
```

- `prediction = 1` → spam
- `prediction = 0` → non spam

## Dépendances

- Flask
- pandas
- scikit-learn
- joblib
