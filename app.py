from flask import Flask, render_template



app = Flask(__name__)



@app.route('/inventory')

def inventory():

    inventory_items = ['apple', 'banana', 'cherry']

    return render_template('other_templates.html', inventory=inventory_items)



if __name__ == '__main__':

    app.run(debug=True)