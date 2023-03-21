from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

@app.route('/', methods=["GET"])
def index():
    if 'notes' not in session:
        session['notes'] = []
    return render_template("home.html", notes=session['notes'])

@app.route('/add_note', methods=["POST"])
def add_note():
    note = request.form.get("note")
    if note:
        session['notes'].append(note)
        session.modified = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)