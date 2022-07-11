from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "THIS IS MY SECRET"

@app.route('/')
def dojo_survey():
    return render_template( "index.html" )

@app.route('/result')
def survey_result():
    return render_template( "result.html" )


@app.route('/process', methods = ['POST'])
def process_survey():
    print( request.form['name'], request.form['location'] )
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    return redirect('/result')









if __name__ == "__main__":
    app.run(debug=True)