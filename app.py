from flask import Flask, request, jsonify

app = Flask(__name__)

# Dicionário para armazenar as traduções
translations = {
    "hello": {
        "en": "Hello",
        "es": "Hola",
        "fr": "Bonjour"
    },
    "dog": {
        "en": "Dog",
        "es": "Perro",
        "fr": "Chien"
    }
}


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    word = data.get("word")
    language = data.get("language")

    if word in translations and language in translations[word]:
        translated_word = translations[word][language]
        return jsonify({"translation": translated_word})
    else:
        return jsonify({"error": "Tradução não encontrada."})


if __name__ == "__main__":
    app.run()
