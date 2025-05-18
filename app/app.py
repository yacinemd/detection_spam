from flask import Flask, request, jsonify, render_template
import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))           
MODELS_DIR = os.path.join(CURRENT_DIR, '..', 'models')              
sys.path.insert(0, os.path.abspath(MODELS_DIR))  

import spam_model

app = Flask(__name__)

@app.route('/')
def home():
    """Rend la page d'accueil."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        if 'text' not in data:
            return jsonify({'error': 'Aucun texte fourni.'}), 400
        
        text = data['text']
        
        # Prédiction et score de confiance via le modèle
        prediction, confidence_score = spam_model.predict(text)

        return jsonify({
            'prediction': int(prediction),
            'score': confidence_score
        })
    
    except Exception as e:
        print(f"Erreur lors de la prédiction : {str(e)}")
        return jsonify({'error': 'Erreur lors de la prédiction : ' + str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
