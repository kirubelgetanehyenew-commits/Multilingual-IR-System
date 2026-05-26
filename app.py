from flask import Flask, render_template, request

from retrieval import search

from language_detection import detect_language

from translation import translate_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    query = ""

    translated_query = ""

    detected_language = ""

    results = []

    if request.method == "POST":

        query = request.form["query"]

        detected_language = detect_language(query)

        # English → Amharic
        if detected_language == "English":

            translated_query = translate_text(
                query,
                "am"
            )

        # Amharic → English
        elif detected_language == "Amharic":

            translated_query = translate_text(
                query,
                "en"
            )

        else:

            translated_query = query

        results = search(
            query + " " + translated_query
        )

    return render_template(
        "index.html",
        query=query,
        translated_query=translated_query,
        detected_language=detected_language,
        results=results
    )

if __name__ == "__main__":
    app.run(debug=True)