# We import the markdown library
import markdown
import os
from flask import Flask
from flask import render_template
from flask import Markup

app = Flask(__name__)
@app.route('/')

def index():
    contentDirectories = [x[0] for x in os.walk('content')]
    content = ""
    for directory in contentDirectories:
        content = content + "* <a href=\"" + str(directory) + "\">" + str(directory) + "</a>\n"

    content = Markup(markdown.markdown(content))
    return render_template('index.html', **locals())

app.run(debug=True)

