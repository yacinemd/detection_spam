function sendData() {
    // Récupérer le texte de la zone de texte
    const inputText = document.getElementById('inputText').value;

    // Vérifier si le champ de texte est vide
    if (!inputText) {
        document.getElementById('result').innerText = "Veuillez entrer un message.";
        return;
    }

    // Envoyer une requête POST au serveur
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => {
        // Vérifier si la réponse est correcte
        if (!response.ok) {
            throw new Error('Erreur lors de la prédiction : ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Afficher la prédiction dans l'élément de résultat
        if(data.prediction === 1) {
            document.getElementById('result').innerText = "Prédiction : Spam";
        } else {
            document.getElementById('result').innerText = "Prédiction : Non Spam";
        }

        // Afficher le score de confiance, si il est présent dans la réponse
        if (data.score !== undefined) {
            document.getElementById('score').innerText = "Score de confiance : " + data.score;
        } else {
            document.getElementById('score').innerText = "Score de confiance non disponible.";
        }
    })
    .catch(error => {
        // Gérer les erreurs
        document.getElementById('result').innerText = "Erreur : " + error.message;
        document.getElementById('score').innerText = "";
    });
}
