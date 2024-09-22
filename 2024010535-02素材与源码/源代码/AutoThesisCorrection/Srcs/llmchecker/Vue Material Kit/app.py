from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
app = Flask(__name__, static_folder='dist/assets', template_folder='dist')
app.root_path = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)