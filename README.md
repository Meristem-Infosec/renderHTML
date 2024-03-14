# renderHTML.py

## Summary
This is a deliberately vulnerable flask application that accepts HTML, renders it using wkhtmltopdf, and returns the PDF file.
It also checks the referer header as a token defense against abuse.  Bypassing this defense makes a better demo.

## Requirements
Python Libraries (pip install -r requirements.txt)
* flask
* pdfkit

wkhtmltopdf (must be installed at the OS level - https://wkhtmltopdf.org/downloads.html)

## Usage
_Modify the string in the referer check to be the domain where you're hosting it, or just remove the check depending on your needs_

``curl -H "Referer: api.uuw.app" --json "{\"content\":\"<HTML><BODY><H1>HTML Rendering Successful</H1></BODY></HTML>\"} http://render.uuw.app:8080/render``
