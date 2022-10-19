from flask import *
app = Flask(__name__)

@app.route('/table/<int:num>')
def table (num):
    return render_template('print-table.html', n =num)
if __name__=='_main_':
    app.run(debug = True)