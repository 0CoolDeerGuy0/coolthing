from flask import Flask, request, render_template
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
CORS(app)

UPLOAD_FOLDER = 'server/resource'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'html'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/get_html_code")
def get_html_code():
    # Читаем содержимое HTML файла с помощью функции render_template
    html_code = render_template("resource/flore1.html")  # Замените example.html на имя вашего файла HTML

    # Отправляем HTML код в ответе
    return html_code

@app.route('/api/css')
def get_css():
    with open('css_template.css') as css_file:
        css = css_file.read()
    return css

if __name__ == '__main__':

    app.run(debug=True)