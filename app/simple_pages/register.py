from flask import Blueprint, render_template


blueprint = Blueprint('resgistration',__name__)


@blueprint.route('/register')
def register():
      return render_template('register.html')