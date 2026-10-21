from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def load_posts():
    with open('data/posts.json', 'r', encoding="utf-8") as file:
        return json.load(file)


def save_posts(posts):
    with open("data/posts.json", "w", encoding="utf-8") as newfile:
        json.dump(posts, newfile, indent=3)


@app.route('/')
def index():
    current_posts = load_posts()
    return render_template('index.html', posts=current_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    current_posts = load_posts()

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        # ID ermitteln
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
