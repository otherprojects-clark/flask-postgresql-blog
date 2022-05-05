from flask import Flask, render_template, request, flash, get_flashed_messages, redirect, url_for
from db.db import Database
from secrets import token_hex
from core.data import ctx, postdata
from arrow import utcnow
from colorama import init

init()

app = Flask(__name__, template_folder='views')
app.secret_key = token_hex()

p = postdata()

def init_db():
  dat = Database()
  cur = dat.db.cursor()
  with open('schema.sql', 'r') as schema:
    cur.execute(schema.read())
  dat.db.commit()
  cur.close()
  dat.db.close()
init_db()

# main
@app.route('/')
def index():
  return render_template('index.html', ctx=ctx())

# 404 not found 
@app.errorhandler(404)
def notfound(request):
  return render_template("404.html", ctx=ctx()), 404

# about page
@app.route('/about')
def about():
  return render_template("about.html", ctx=ctx())



# crud pages

# create
@app.route('/create', methods=['GET', 'POST'])
def create():
  dat = Database()
  cur = dat.db.cursor()
  success = False
  invalid = False
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']
    createdat = utcnow().to('local').format('MMM D, YYYY h:mm A')
    if not title:
      flash("Title is required.")
      invalid = True
    else:
      success = True
      cur.execute(f"insert into posts (title, body, createdat) values ('{title}', '{content}', '{createdat}')")
      dat.db.commit()
      cur.close()
      dat.db.close()
      flash('Post created successfully')
  else:
    pass
  messages = get_flashed_messages()
  return render_template('crud/create.html', ctx=ctx(), messages=messages, success=success, invalid=invalid)

# edit
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
  dat = Database()
  cur = dat.db.cursor()
  cur.execute(f"select * from posts where id={id}")
  post = cur.fetchone()
  cur.execute('select id from posts')
  ids_tuple = cur.fetchall()
  ids = []
  success = False
  invalid = False

  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']
    # createdat = utcnow().to('local').format('MMM D, YYYY h:mm A')
    if not title:
      flash('Title is required')
      invalid = True
    else:
      cur.execute(f"update posts set title='{title}', body='{content}' where id={id};")
      dat.db.commit()
      cur.close()
      dat.db.close()
      flash('Post edited successfully')
      success = True
      return redirect(url_for('index'))
  else:
    print('get method')
  messages = get_flashed_messages()
  for x in ids_tuple:
    ids.append(x[0]) 
  return render_template(
    "crud/edit.html", 
    ctx=ctx(), 
    id=id,
    ids=ids,
    success=success,
    invalid=invalid,
    post=post,
    title=p.title,
    messages=messages
  )

# read posts
@app.route('/posts')
def posts():
  dat = Database()
  cur = dat.db.cursor()
  cur.execute('select * from posts;')
  posts = cur.fetchall()
  cur.close()
  dat.db.close()
  return render_template(
    "crud/posts.html",
    ctx=ctx(), 
    id=p.id,
    posts=posts, 
    title=p.title, 
    createdAt=p.createdAt
  )

# read one post
@app.route('/post/<int:id>')
def post(id):
  dat = Database()
  cur = dat.db.cursor()
  cur.execute(f"select * from posts where id={id}")
  post = cur.fetchone()
  cur.execute('select id from posts')
  ids_tuple = cur.fetchall()
  ids = []
  for x in ids_tuple:
    ids.append(x[0])

  return render_template(
    "crud/post.html", 
    ctx=ctx(), 
    id=id, 
    post=post, 
    ids=ids,
    title=p.title,
    content=p.content,
    createdAt=p.createdAt
  )

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  dat = Database()
  cur = dat.db.cursor()
  cur.execute(f"select * from posts where id={id}")
  post = cur.fetchone()
  cur.execute('select id from posts')
  ids_tuple = cur.fetchall()
  ids = []
  for x in ids_tuple:
    ids.append(x[0])
  deleted = False
  if request.method == 'POST':
    delete = request.form['delete']
    if delete == 'false':
      return redirect(url_for('posts'))
    else:
      cur.execute(f"delete from posts where id={id}")
      dat.db.commit()
      cur.close()
      dat.db.close()
      deleted = True
      flash('Post deleted successfully')
      return redirect(url_for('posts'))
  else:
    print('get method')
  messages = get_flashed_messages()

  return render_template(
    "crud/delete.html", 
    ctx=ctx(),
    post=post,
    id=id,
    title=p.title,
    messages=messages,
    deleted=deleted
  )

if __name__ == '__main__':
  app.run(debug=True)
  