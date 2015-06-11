# views for home
from flask import Blueprint, request, redirect, render_template

from flask.ext.mongoengine.wtf import model_form
from ast_space.models import Post


home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')



@home.route('/home', methods=['GET', 'POST'])
def new_talk():
    talk_form = model_form(Post)(request.form)
    if request.method == 'POST' and talk_form.validate():
        return redirect('/home')
    return render_template('home.html', form=talk_form)