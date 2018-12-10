from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.config['debug'] = True

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("editor.html")
    else:
        print(request.form['content'])
        return render_template("editor.html")

if __name__ == '__main__':
    app.run()
