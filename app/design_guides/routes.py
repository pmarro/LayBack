from app.design_elements.models import Keyword, Logo, Font, Color
from app.users.models import User
from flask import Blueprint, render_template, send_file
from flask_login import current_user, login_required
from io import BytesIO

blueprint = Blueprint('design-guide', __name__)

@blueprint.route('/design-guide')
@login_required

def design_guide():
  try:
    logo = Logo.query.filter_by(designguide_id = current_user.id)
    font = Font.query.filter_by(designguide_id = current_user.id)
    colors = Color.query.filter_by(designguide_id = current_user.id)
    keywords = Keyword.query.filter_by(designguide_id = current_user.id)
    user = User.query.filter_by(designguide_id = current_user.id)
      
    return render_template('design_guide/index.html', logos = logo, fonts = font, colors = colors, keywords = keywords, user = user)
  except:
    return render_template('design_guide/index.html',
    error = 'An error occurred while processing your Design Guide. Please make sure to enter valid data.'
    )

@blueprint.route('/logo/download')

def download_logo():
  logo = Logo.query.filter_by(designguide_id = current_user.id).first()
  return send_file(BytesIO(logo.data), attachment_filename=logo.filename, as_attachment=True)

@blueprint.route('/font/download')

def download_font():
  font = Font.query.filter_by(designguide_id = current_user.id).first()
  return send_file(BytesIO(font.data), attachment_filename=font.filename, as_attachment=True)
