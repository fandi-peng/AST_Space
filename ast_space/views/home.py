# views for home
from flask import Blueprint, request, redirect, render_template

from flask.ext.mongoengine.wtf import model_form
from ast_space.models import Talk


home = Blueprint('home', __name__)

# to add a new talk / view coming talks
@home.route('/', methods=['GET', 'POST'])
def new_talk():
    talks = Talk.objects.order_by('-created_at')
    talk_form = model_form(Talk, exclude=('created_at',))(request.form)
    if request.method == 'POST' and talk_form.validate():
        talk = Talk()
        talk_form.populate_obj(talk)
        talk.save()
        return redirect('/')
    return render_template('home/home.html', form=talk_form, talks=talks)