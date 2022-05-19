from flask import Flask, render_template, flash, request, redirect
app = Flask (__name__)
app.secret_key = 'secret key'

users={
    "admin": "admin",
    "user": "user"
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if users[request.form['username']] != request.form['password']:
            return render_template('invalid.html')
        else:    
            return redirect ('/cabinet')
    else:
        return render_template('login.html')

@app.route("/cabinet")
def cabinet():
    return render_template('cabinet.html')

@app.route('/favicon.ico')
def favicon():
        return send_from_directory("static", "favicon.ico", mimetype="image/vnd.microsoft.icon")

if __name__ == "__main__":
    app.run(debug=True)
