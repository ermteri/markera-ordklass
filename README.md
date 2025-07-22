# 🧠 Ordklassmarkerare med Flask + Stanza

Ett enkelt webbgränssnitt där du kan klistra in svensk text och få **adjektiv**, **adverb** och **verb** markerade i olika färger. Bygger på Python, Flask och Stanza.

---

## 🚀 Funktioner

- Markerar adjektiv (🔴 rött), adverb (🟢 grönt) och verb (🔵 blått)
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
python app.py
 
Öppna sedan `http://127.0.0.1:5000` i din webbläsare.

---

## 📝 Exempel

<img width="1672" height="906" alt="image" src="https://github.com/user-attachments/assets/78c7fc5e-440f-49e7-83ab-6b941328cc46" />

---

## 🧾 Projektstruktur

```
├── app.py                 # Flask-servern  
├── requirements.txt       # Python-beroenden  
├── templates/  
│   └── index.html         # Webbgränssnitt  
├── static/  
│   └── style.css          # Färger och design  
└── .gitignore  

```

---

## 📖 Licens

MIT License – fri att använda, ändra och dela.
