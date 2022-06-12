from flask import Flask, render_template
from post import Post
import requests



blog_response = requests.get("https://api.npoint.io/7555fe706a709b72b3e6")
blog_data = blog_response.json()
post_objects = []
for blog in blog_data:
    post_obj = Post(post_id=blog["id"], post_title=blog["title"], post_subtitle=blog["subtitle"], post_body=blog["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

# home page
@app.route('/')
def home():
    return render_template("index.html", all_blogs=post_objects)

#about page
@app.route('/about')
def about():
    return render_template("about.html")

#contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# post page
@app.route('/blog/<int:num>')
def read_post(num):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == num:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__=="__main__":
    app.run(debug=True)
