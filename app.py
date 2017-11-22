#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('https://www.facebook.com/claclickfotos/'))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 80))
    app.run(host='claclick.com.br', port=port)
