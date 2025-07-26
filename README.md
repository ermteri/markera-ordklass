# 🧠 Ordklassmarkerare med Flask + Stanza

Ett enkelt webbgränssnitt där du kan klistra in svensk text och få **adjektiv**, **adverb** och **pronomen** markerade i olika färger. Bygger på Python, Flask och Stanza.

---

## 🚀 Funktioner

- Markerar adjektiv (🔴 rött), adverb (🔵 blått) och pronomen (🟢 grönt)
- Statistik: total antal ord samt andel av varje ordklass
- Möjlighet att visa/dölja varje ordklass med ett klick

---

## 📦 Installation

1. **Kloning & miljö:**

```bash
git clone https://github.com/ermteri/markera-ordklass.git
cd <ditt-repo>
python3 -m venv env
source env/bin/activate
```

2. **Installera beroenden:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Starta appen

```bash
python app-3.py
 
Öppna sedan `http://127.0.0.1:5000` i din webbläsare.

---

## 📝 Exempel
Klistra in:  
> Den vackra staden låg stilla och skimrade i den mycket fina solnedgången.  
och klicka på "Adverb"

Du får:  
Resultat:  
Den vackra staden låg **stilla** och skimrade i den **mycket** fina solnedgången.  
Totalt antal ord: 13  
  
Antal adjektiv: 2  
  
Andel av totala ord: 15.38%  
---

## 🧾 Projektstruktur

ordklassmarkerare/
│
├── app-3.py                 # Flask-applikationen
├── requirements.txt         # Python-bibliotek
├── README.md                # Denna fil  
├── templates/
│   └── index.html           # HTML-sida för inmatning och resultat  
├── static/
│   └── style.css            # CSS-stilar för färgmarkering
└── .gitignore               # Ignorera t.ex. env/ och __pycache__/

---

## 📖 Licens

MIT License – fri att använda, ändra och dela.
