from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

from werkzeug.exceptions import HTTPException

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

