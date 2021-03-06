from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:hello11@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'hello1111'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(240))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/blog', methods=['POST', 'GET'])
def blog():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_blog = Blog(title, body)
        db.session.add(new_blog)
        db.session.commit()
    
    blogs = Blog.query.all()
    return render_template('blog.html', blogs=blogs)

@app.route('/newpost', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_blog = Blog(title, body)
        db.session.add(new_blog)
        db.session.commit()

        blogs = Blog.query.all()
        blogs.append(new_blog)
        return redirect('/blog')

    return render_template('new_post.html')

@app.route('/blog/<int:id>')
def solo_post(id=None):
    blog = Blog.query.filter_by(id=id).first()
    return render_template('solo.html', blog=blog)


if __name__ == '__main__':
    app.run()


