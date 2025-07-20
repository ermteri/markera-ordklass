from flask import Flask, request, render_template_string
import stanza

# Starta Stanza med svensk pipeline
stanza.download("sv")  # Körs bara första gången, annars kommentera bort
nlp = stanza.Pipeline(lang="sv", processors="tokenize,pos,lemma")

app = Flask(__name__)

# HTML-template
HTML = """
<!doctype html>
<html lang="sv">
<head>
  <meta charset="utf-8">
  <title>Markera adjektiv, adverb och pronomen</title>
  <style>
    body { font-family: sans-serif; padding: 2em; }
    textarea { width: 100%%; height: 200px; }
    .adj { color: red; font-weight: bold; }
    .adv { color: green; font-weight: bold; }
    .pron { color: blue; font-weight: bold; }
  </style>
</head>
<body>
  <h1>Markera adjektiv, adverb och pronomen</h1>
  <form method="post">
    <textarea name="text">{{ input_text }}</textarea><br><br>
    <button type="submit">Markera</button>
  </form>
  {% if output_text %}
    <h2>Resultat:</h2>
    <p>{{ output_text|safe }}</p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    input_text = ""
    output_text = ""

    if request.method == "POST":
        input_text = request.form["text"]
        doc = nlp(input_text)

        marked = []
        for sentence in doc.sentences:
            for word in sentence.words:
                w = word.text
                if word.upos == "ADJ":
                    w = f'<span class="adj">{w}</span>'
                elif word.upos == "PRON":
                    w = f'<span class="pron">{w}</span>'
                elif word.upos == "ADV":
                    w = f'<span class="adv">{w}</span>'
                marked.append(w)
        output_text = " ".join(marked)

    return render_template_string(HTML, input_text=input_text, output_text=output_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

