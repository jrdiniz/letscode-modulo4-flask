import json
from flask import Flask
from flask import make_response
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/<site>')
def url_shortener(site):
    hyperlink_format = '<a href="{link}">{text}</a>'
    link_text = hyperlink_format.format(link='http://www.{}.com'.format(site), text=site)
    return link_text, 200


@app.route('/html_page/<nome>')
def html_page(nome):
    return u'''
        <html lang="en">
            <head><title>Aprendendo a usar o Flask</title></head>
            <body>
                <h1>Ola {}! Algumas coisas que você pode fazer em Flask.</h1>
                <ul>
                    <li>Escrever html na view</li>
                    <li> Tentar automatizar a escrita de html via Python</li>
                </ul>
            </body>
        </html>
    '''.format(nome)

@app.route('/api')
def json_api():
    pessoas = [
        {"Nome":"Juliano Resende"},
        {"Nome":"Renata Pereira"},
        {"Nome":"Miguel Pereira"}
    ]
    response = make_response(json.dumps(pessoas))
    response.content_type = "application/json"
    return response

@app.route('/api/v2')
def api():
    pessoas = [
        {"Nome":"Juliano Resende"},
        {"Nome":"Renata Pereira"},
        {"Nome":"Miguel Pereira"}
    ]
    return jsonify(pessoas)

@app.route('/api/v3/<nome>')
def api_v3(nome):
    response = [
        {"nome":nome},
        {"coringa": False}
    ]
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8250)