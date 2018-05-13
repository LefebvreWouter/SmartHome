from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import mysql.connector as connector
import os


from DbClass import dbClass


app = Flask(__name__)
@app.route('/')
def index():
    return render_template("signup.html")


@app.route('/signup', methods=["POST"])
def singUp():
    gebruikersnaam = str(request.form["Naam"])
    passwoord = str(request.form["Passwoord"])
    cursor = conn.cursus()

    cursor.excute("INSERT INTO Gebruikers (Naam,Passwoord)VALUES(%s,%s)"(0,gebruikersnaam,passwoord,0))
    conn.commit()
    return redirect (url_for('dashboard'))

@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/checkGebruiker", methods=["POST"])
def check():
    db = dbClass()
    gebruikersnaam = str(request.form["Naam"])
    passwoord = str(request.form["Passwoord"])
    aantal = db.checkGebruiker(gebruikersnaam, passwoord)

    if aantal[0] == 1:
        return redirect(url_for('dashboard'))
    else:
        return "lukt niet "



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/temperatuur')
def temperatuur():
    db = dbClass()
    lstData = db.getDataTemp()
    lstDates = []
    lst_temp = []
    print(str(lstData))
    for waarde in lstData:
        lstDates.append(waarde[0])
        lst_temp.append(waarde[1])
    return  render_template('temperatuur.html', Datum=lstDates[::-1], Temp=lst_temp[::-1])

@app.route('/lights')
def lights():
    return render_template('lights.html')

@app.route('/stats')
def stats():
    db = dbClass()
    lstData = db.getDataTemp()
    lstDates =[]
    lst_temp =[]
    print(str(lstData))
    for waarde in lstData:
        lstDates.append(waarde[0])
        lst_temp.append(waarde[1])
    return render_template('stats.html', Datum=lstDates[::-1], Temp=lst_temp[::-1])



@app.route('/statsLicht')
def statsLicht():
    db = dbClass()
    lstData = db.getDataLicht()
    lstDates = []
    lst_licht = []
    print(str(lstData))
    for waarde in lstData:
        lstDates.append(waarde[0])
        lst_licht.append(waarde[1])
    return render_template('statsLicht.html', Datum=lstDates[::-1], Licht=lst_licht[::-1])


@app.route('/statsDeur')
def statsDeur():
    db = dbClass()
    lstData = db.getDataDeur()
    lstDates = []
    lst_deur = []
    lst_serieNr = []
    print(str(lstData))
    for waarde in lstData:
        lstDates.append(waarde[0])
        lst_deur.append(waarde[1])
        lst_serieNr.append(waarde[2])
    return render_template('statsDeur.html', Datum=lstDates[::-1], Deur=lst_deur[::-1], SerieNr=lst_serieNr)

@app.route('/deuren')
def deuren():
    return render_template('deuren.html')

@app.errorhandler(404)
def PageNotFound(error):
    return render_template('error.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')




@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':

    app.run()
