# My Flask Blog

Eine einfache Blog-Anwendung, die mit Python und Flask entwickelt wurde. Das Projekt ermöglicht es, Blogbeiträge zu erstellen, anzuzeigen, zu bearbeiten und zu löschen (CRUD).

## Funktionen

- **Create:** Neue Blogbeiträge mit Titel, Autor und Inhalt erstellen
- **Read:** Alle Blogbeiträge auf der Startseite anzeigen
- **Update:** Bestehende Blogbeiträge bearbeiten
- **Delete:** Blogbeiträge löschen
- Automatische Vergabe eindeutiger Beitrags-IDs
- Speicherung der Blogbeiträge in einer JSON-Datei
- Responsive Design für Desktop und Smartphones
- Formularvalidierung durch HTML-Pflichtfelder

## Technologien

- Python
- Flask
- HTML5
- CSS3
- Jinja2
- JSON

## Installation und Start

**1. Repository klonen**

```bash
git clone https://github.com/maleika-waigel/masterblog-de.git
cd masterblog-de
```

**2. Virtuelle Umgebung erstellen und aktivieren**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Abhängigkeiten installieren**

```bash
pip install -r requirements.txt
```

**4. Anwendung starten**

```bash
python app.py
```

Die Anwendung ist anschließend unter folgender Adresse erreichbar:

`http://127.0.0.1:5000`

## Datenspeicherung

Die Blogbeiträge werden in `data/posts.json` als Liste von Dictionaries gespeichert.

Jeder Beitrag enthält folgende Eigenschaften:

- `id` – Eindeutige Beitrags-ID
- `title` – Titel des Beitrags
- `author` – Autor des Beitrags
- `content` – Inhalt des Beitrags

## Projektziel

Dieses Projekt wurde im Rahmen einer Python-Weiterbildung erstellt, um den Umgang mit Flask, HTTP-Anfragen, Jinja2-Templates und der Verarbeitung von JSON-Daten zu üben.