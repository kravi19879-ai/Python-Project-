# Importing
from flask import Flask, render_template,request
# Interaction
web=Flask(__name__)
# Mapping
@web.route('/')
@web.route('/register')
# Inputs
def homepage():
    return render_template('register.html')
# Mapping
@web.route("/confirmation" , methods=['POST','GET'])
# Inputs
def register():
    if request.method=='POST':
        name=request.form['name']
        city=request.form['city']
        phone=request.form['phone number']
        return render_template('confirm.html',name=name,city=city,phonenumber=phone)

# Main
if __name__ == '__main__':
    web.run(debug=True)

