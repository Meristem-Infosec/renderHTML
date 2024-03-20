# Deliberately vulnerable Flask app to render HTML to PDF
# This is vulnerable to both SSRF and local file inclusion attacks
# It requires that the python pdfkit library is installed (pip install pdfkit)
# It also requires that the wkhtmltopdf binary is installed on the system
# The binary can be downloaded from https://wkhtmltopdf.org/downloads.html

from flask import Flask, request, send_file
import pdfkit
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Rendering Service Available'

@app.route('/render', methods=['POST'])
def render_pdf():
    # Check the origin header to "protect" the service
    # Obviously this is easily bypassed
    referer = request.headers.get('Referer')
    if referer is None or 'api.uuw.app' not in referer:
        return 'Invalid request', 403

    content = request.json.get('content')
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp:
        pdfkit.from_string(content, temp.name, options=options)
        return send_file(temp.name, mimetype='application/pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)