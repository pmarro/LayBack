from ast import keyword
from app.design_elements.models import Keyword, Logo, Font, Color
from flask import Blueprint, render_template, send_file
from flask_login import current_user, login_required

blueprint = Blueprint('design-guide', __name__)

@blueprint.route('/design-guide')
@login_required

def design_guide():
  try:
    logo = Logo.query.filter_by(designguide_id = current_user.id)
    font = Font.query.filter_by(designguide_id = current_user.id)
    colors = Color.query.filter_by(designguide_id = current_user.id)
    keywords = Keyword.query.filter_by(designguide_id = current_user.id)
    #pict = send_file(logo[0].buffer, mimetype= logo[0].mimetype)
      
    return render_template('design_guide/index.html', logos = logo, fonts = font, colors = colors, keywords = keywords)
  except:
    return render_template('design_guide/index.html',
    error = 'An error occurred while processing your Design Guide. Please make sure to enter valid data.'
    )