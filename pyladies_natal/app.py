from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/series/add/", methods=['GET', 'POST'])
def add():
    return render_template("add.html")

@app.route("/series/<serie_id>/edit/", methods=['GET', 'POST'])
def edit(serie_id):
    return render_template("edit.html")

@app.route("/series/<int:serie_id>/delete/", methods=['POST'])
def delete(serie_id):
    return redirect("index")

if __name__ == "__main__":
    app.run(debug=True)