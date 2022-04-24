from ast import keyword
from app.design_elements.models import Keyword, Logo, Font, Color
from flask import Blueprint, render_template, send_file
from flask_login import login_required

blueprint = Blueprint('design-guide', __name__)

@blueprint.route('/design-guide')
@login_required

def design_guide():
  try:
    logo = Logo.query.all()
    font = Font.query.all()
    colors = Color.query.all()
    keywords = Keyword.query.all()
    pict = send_file(logo[0].buffer, mimetype= logo[0].mimetype)
      
    return render_template('design_guide/index.html', logos = pict, fonts = font, colors = colors, keywords = keywords)
  except:
    return render_template('design_guide/index.html',
    error = 'An error occurred while processing your order. Please make sure to enter valid data.'
    )