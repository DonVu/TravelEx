from flask import Flask, flash, redirect, render_template, request, session, abort
app=Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return "Flask App!!"


@app.route("/hotels/")
def hotels():
    return render_template(
    'index.html')


# @app.route("/hotels/<string:name>/")
# def details(name):
#     return render_template(
#     'page3.html',name="page3.html")

@app.route("/hotels/details", methods=['POST'])
def details():

    if request.form.get('location'):
      loc=request.form['location']
      print(loc)
      return render_template("hoteldetails.html",loc=loc)
    return render_template("hoteldetails.html")


if __name__=="__main__":
 app.run()
