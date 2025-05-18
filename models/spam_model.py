import joblib
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, 'models', 'spam_model.pkl')


model = joblib.load(model_path)

def predict(text):
    try:
        print(f"Texte reçu pour prédiction: {text}")
        
        prediction = model.predict([text])
        
        prediction_proba = model.predict_proba([text])
        
        # La probabilité de la classe prédite (spam ou non spam)
        confidence_score = prediction_proba[0][prediction[0]]
        
        print(f"Prédiction: {prediction[0]}, Score de confiance: {confidence_score}")
        
        return prediction[0], confidence_score  
    except Exception as e:
        print(f"Erreur dans la prédiction : {str(e)}")
        raise  
