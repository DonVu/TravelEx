from flask import Flask, flash, redirect, render_template, request, session, abort
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

    if request.form.get('location'):
      loc=request.form['location']
      print(loc)
      return render_template("flightsdetails.html",loc=loc)
    return render_template("flightsdetails.html")


if __name__=="__main__":
 app.run()
