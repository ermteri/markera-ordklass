from flask import Flask, request, render_template_string
import stanza

app = Flask(__name__)

# Ladda svenska modellen
nlp = stanza.Pipeline(lang='sv', processors='tokenize,pos', use_gpu=False)

TEMPLATE = '''
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Ordklassmarkering</title>
    <style>
        .adjektiv { color: red; font-weight: bold; }
        .adverb { color: blue; font-weight: bold; }
        .verb { color: green; font-weight: bold; }
        textarea { width: 100%; height: 150px; font-size: 1em; }
        .btn-group button {
            margin-right: 10px;
        }
        .stats {
            margin-top: 1em;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h2>Klistra in text och välj ordklass</h2>
    <form method="POST">
        <textarea name="input_text">{{ input_text }}</textarea><br><br>
        <div class="btn-group">
            <button name="show_class" value="adjektiv">Visa Adjektiv</button>
            <button name="show_class" value="adverb">Visa Adverb</button>
            <button name="show_class" value="verb">Visa Verb</button>
        </div>
    </form>
    <hr>
    {% if output %}
        <h3>Resultat:</h3>
        <p>{{ output|safe }}</p>
        <div class="stats">
            <p>Totalt antal ord: <strong>{{ total_words }}</strong></p>
            <p>Antal {{ selected_class }}: <strong>{{ count }}</strong></p>
            <p>Andel av totala ord: <strong>{{ percentage }}%</strong></p>
        </div>
    {% endif %}
</body>
</html>
'''

POS_MAPPING = {
    'ADJ': 'adjektiv',
    'ADV': 'adverb',
    'VERB': 'verb'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ''
    output = ''
    selected_class = ''
    count = 0
    total_words = 0
    percentage = 0.0

    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        selected_class = request.form.get('show_class', '')
        doc = nlp(input_text)

        highlighted = []
        class_count = 0

        for sent in doc.sentences:
            for word in sent.words:
                total_words += 1
                css_class = POS_MAPPING.get(word.upos)
                token_text = word.text

                if css_class == selected_class:
                    token_text = f'<span class="{css_class}">{token_text}</span>'
                    class_count += 1

                highlighted.append(token_text)

        output = ' '.join(highlighted)
        count = class_count
        percentage = round((class_count / total_words) * 100, 2) if total_words else 0.0

    return render_template_string(
        TEMPLATE,
        input_text=input_text,
        output=output,
        selected_class=selected_class,
        count=count,
        total_words=total_words,
        percentage=percentage
    )

if __name__ == '__main__':
    app.run(debug=True)

