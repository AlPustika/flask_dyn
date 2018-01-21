from flask import Flask,render_template,abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/user/<name>')
def user(name):
    if name:
        return render_template('hello.html',name=name)
    else:
        abort(404)

if __name__==('__main__'):
    app.run(debug=True)