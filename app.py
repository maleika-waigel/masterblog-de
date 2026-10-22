from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def load_posts():
    """Lade alle Blogbeiträge aus der JSON-Datei.

    Returns:
        list: Eine Liste mit den gespeicherten Blogbeiträgen.
    """
    with open('data/posts.json', 'r', encoding="utf-8") as file:
        return json.load(file)


def save_posts(posts):
    """Speichere die Blogbeiträge in der JSON-Datei.

    Args:
        posts (list): Liste der zu speichernden Blogbeiträge.
    """
    with open("data/posts.json", "w", encoding="utf-8") as newfile:
        json.dump(posts, newfile, indent=3)


def fetch_post_by_id(post_id, posts=None):
    """Sucht ein Post anhand seiner ID und gibt ihn zurück.

    Args:
        post_id (int): ID des gesuchten Blogbeitrags.
        posts (list | None): Optional - Liste der Blogbeiträge.
    Returns:
        dict | None: Gefundener Blogbeitrag als Dictionary
            oder None, wenn kein Beitrag mit dieser ID existiert.
    """
    if posts is None:
        posts = load_posts()

    for post in posts:
        if post['id'] == post_id:
            return post

    return None


@app.route('/')
def index():
    """Lade die Blogbeiträge und zeige sie auf der Startseite an.

    Returns:
        str: Gerendertes HTML-Template der Startseite.
    """
    current_posts = load_posts()
    return render_template('index.html', posts=current_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Zeige das Formular an oder füge einen neuen Blogbeitrag hinzu.

    Bei einer GET-Anfrage wird das Formular angezeigt.
    Bei einer POST-Anfrage werden die Formulardaten ausgelesen,
    eine eindeutige ID vergeben und der neue Beitrag gespeichert.

    Returns:
        str | Response: Gerendertes Formular bei GET oder
            Weiterleitung zur Startseite bei POST.
    """
    if request.method == 'POST':
        current_posts = load_posts()

        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        if current_posts:
            post_ids = []
            for post in current_posts:
                post_ids.append(post['id'])
            next_id = max(post_ids) + 1
        else:
            next_id = 1

        new_post = {
            'id': next_id,
            'title': title,
            'author': author,
            'content': content
        }

        current_posts.append(new_post)
        save_posts(current_posts)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """Lösche einen Blogbeitrag anhand seiner ID.

    Args:
        post_id (int): ID des zu löschenden Blogbeitrags.
    Returns:
        Response: Weiterleitung zur Startseite.
    """
    posts = load_posts()

    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
            break

    save_posts(posts)

    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Zeigt das Bearbeitungsformular oder aktualisiert einen
    Blogbeitrag anhand seiner ID.

    Args:
        post_id (int): ID des zu bearbeitenden Blogbeitrags.
    Returns:
        str | Response | tuple: HTML-Formular, Weiterleitung zur
            Startseite oder Fehlermeldung mit HTTP-Status 404.
    """
    posts = load_posts()
    post = fetch_post_by_id(post_id, posts)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post['title'] = request.form.get('title')
        post['author'] = request.form.get('author')
        post['content'] = request.form.get('content')

        save_posts(posts)

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
