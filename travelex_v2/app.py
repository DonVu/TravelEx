from flask import Flask, flash, redirect, render_template, request, session, abort
from datetime import date
app=Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template(
    'index.html')


@app.route("/hotels", methods=['POST'])
def hotels():

    if request.form.get('location'):
      loc=request.form['location']
      print(loc)
      return render_template("hoteldetails.html",loc=loc)
    return render_template("hoteldetails.html")

@app.route("/flights", methods=['POST'])
def flights():

    if request.form.get('origin') and request.form.get('destination') and request.form.get('depart') and request.form.get('return'):
      origin=request.form['origin']
      destination=request.form['destination']
      departdate=request.form['depart']
      returndate=request.form['return']
      print(origin)
      print(destination)
      print(departdate)
      print(returndate)
    #return 'origin: '+ ori + 'destination: ' + dest + 'depart: '+ dp + 'return' + rt
      return render_template('flightsdetails.html', origin=origin, destination=destination,departdate=departdate,returndate=returndate)
    return render_template('flightsdetails.html')


if __name__=="__main__":
 app.run()
