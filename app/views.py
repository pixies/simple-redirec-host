from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    page_title = 'Festa de Luana'
    context = {
        'user':'joao'
    }
    return render_template('index.html', title=page_title, context=context)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Solicitação de Login para OpenId="%s", lembre-me=%s'% (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',title='Login',form=form)