from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route('/<name>/<location>') #http://127.0.0.1:5000/Anthony/Las Vegas
def pdf_template(name, Location):
  rendered = render_template('pdf_template.html', name=name, Location=location)
  pdf = pdfkit.from_string(rendered, False)

  response = make_response(pdf)
  response.headers['Content-Type'] = 'application/pdf'
  # response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
  response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

if __name__ == '__main__':
  app.run(debug=True)
