
app = Flask(__name__)
@app.route('/')

def view():
    return render_template('/index.html')
@app.route('/index.html')

app.run(debug=True)