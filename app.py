from flask import Flask, request, render_template
import stanza

app = Flask(__name__)

# Ladda svenska modellen
nlp = stanza.Pipeline(lang='sv', processors='tokenize,pos', use_gpu=False)

POS_MAPPING = {
    'ADJ': 'adjektiv',
    'ADV': 'adverb',
    'PRON': 'pron'
}


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


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
    
        highlighted_lines = []
        class_count = 0
        total_words = 0

        for line in input_text.splitlines():
            doc = nlp(line)
            highlighted_tokens = []

            for sent in doc.sentences:
                for word in sent.words:
                    total_words += 1
                    css_class = POS_MAPPING.get(word.upos)
                    token_text = word.text

                    if css_class == selected_class:
                        token_text = f'<span class="{css_class}">{token_text}</span>'
                        class_count += 1

                    highlighted_tokens.append(token_text)

            highlighted_line = ' '.join(highlighted_tokens)
            highlighted_lines.append(highlighted_line)

        output = '\n'.join(highlighted_lines)
        count = class_count
        percentage = round((class_count / total_words) * 100, 2) if total_words else 0.0

    return render_template(
        'index.html',
        input_text=input_text,
        output=output,
        selected_class=selected_class,
        count=count,
        total_words=total_words,
        percentage=percentage
    )

if __name__ == '__main__':
    app.run(debug=True, port=8080)

