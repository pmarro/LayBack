from flask import redirect, render_template, Blueprint, request, current_app, Response, send_file, url_for
from app.design_guides.models import Designguide
from .models import Designelement, Logo, Font, Color, Keyword
from werkzeug.utils import secure_filename
from app.extensions.database import db
from flask_login import current_user, login_required, login_user
blueprint = Blueprint('elements' , __name__)


@blueprint.route('/elements')
#@login_required
def design_elements():
  page_number = request.args.get('page', 1, type=int)
  elements_pagination = Designelement.query.paginate(page_number, current_app.config['ELEMENTS_PER_PAGE'])
  return render_template('design_elements/index.html', elements_pagination=elements_pagination)

@blueprint.route('/elements/<slug>')
#@login_required
def element(slug):
  element = Designelement.query.filter_by(slug=slug).first_or_404()
  return render_template('design_elements/show.html', element=element)



@blueprint.post('/elements/logo/upload')

def upload_logo():
  try:
    file = request.files['Logo']

    if not file:
      raise Exception( 'Something went Wrong :/')

    upload = Logo(filename=file.filename, data=file.read(), designguide_id = current_user.id)
    
    upload.save()

    element = 'Logo'
    success = f'Your {element} have been successfully uploaded'
    return render_template('design_elements/show.html', element= element, success = success)

  except Exception as error_message:
    element = 'Logo'
    error = error_message or 'An error occurred while processing your Upload.'
    return render_template('design_elements/show.html', element= element, error= error)



@blueprint.post('/elements/font/upload')
def upload_font():
  try:
    file = request.files['Font']

    if not file:
      raise Exception('Something went Wrong :/') 

    upload = Font(filename=file.filename, data=file.read(), designguide_id = current_user.id)
      
    upload.save()

    element = 'Font'
    success = f'Your {element} have been successfully uploaded'
    return render_template('design_elements/show.html', element= element, success = success)
  except Exception as error_message:
    element = 'Font'
    error = error_message or 'An error occurred while processing your Upload.'
    return render_template('design_elements/show.html', element= element, error= error)






@blueprint.post('/elements/color/upload')

def upload_color():
  try:
    color1 = request.form.get('color1')
    color2 = request.form.get('color2')
    color3 = request.form.get('color3')
    color4 = request.form.get('color4')
    color5 = request.form.get('color5')
    color6 = request.form.get('color6')  
    
    color_palette = Color(
    color1 = color1,
    color2 = color2,
    color3 = color3,
    color4 = color4,
    color5 = color5,
    color6 = color6,
    designguide_id = current_user.id
    )
    
    color_palette.save()

    element = 'Color Palette'
    success = f'Your {element} have been successfully uploaded'
    return render_template('design_elements/show.html', element= element, success = success)
  except:
    error = 'An error occurred while processing your Upload.'
    return redirect(url_for('elements.element', slug='color', error= error))


@blueprint.post('/elements/keywords/upload')

def upload_keywords():
  try:
    
    keyword1 = request.form.get('keyword1')
    keyword2 = request.form.get('keyword2')
    keyword3 = request.form.get('keyword3')
    keyword4 = request.form.get('keyword4')
    keyword5 = request.form.get('keyword5')
    keyword6 = request.form.get('keyword6')  


    keywords = Keyword(
    keyword1 = keyword1,
    keyword2 = keyword2,
    keyword3 = keyword3,
    keyword4 = keyword4,
    keyword5 = keyword5,
    keyword6 = keyword6,
    designguide_id = current_user.id
  )

    keywords.save()


    element = 'Keywords'
    success = f'Your {element} have been successfully uploaded'
    return render_template('design_elements/show.html', element= element, success = success)
  except:
    error = 'An error occurred while processing your Design Guide. Please make sure to enter valid data.'
    return redirect(url_for('elements.element', slug='keywords', error= error))


#--UPDATE PAGES---------------------------------------------------------------------------------


@blueprint.route('/elements/update/<slug>')
@login_required
def update_element(slug):
  
  element = Designelement.query.filter_by(slug=slug).first_or_404()
  return render_template('design_elements/update.html', element=element)


@blueprint.route('/elements/update/font', methods =['GET', 'POST'])

def update_font():
  try:
    id = current_user.id
    element = 'Font'
    file = request.files['Font']
    update = Font.query.filter_by(designguide_id = id).first()
    update.filename=file.filename
    update.data=file.read()

    update.save()

    success = f'Your {element} have been successfully updated.'
    return render_template('design_elements/update.html', element= element, success = success)
  except Exception as error_message:
    error = error_message or 'An error occurred while processing your update.'
    return render_template('design_elements/update.html', element= element, error= error)

@blueprint.route('/elements/update/logo', methods =['GET', 'POST'])

def update_logo():
  try:
    id = current_user.id
    element = 'Logo'
    file = request.files['Logo']
    update = Logo.query.filter_by(designguide_id = id).first()
    update.filename=file.filename
    update.data=file.read()

    update.save()

    success = f'Your {element} have been successfully updated.'
    return render_template('design_elements/update.html', element= element, success = success)
  except:
    error ='An error occurred while processing your update. Please try again'
    return render_template('design_elements/update.html', element= element, error= error)



@blueprint.route('/elements/update/keywords', methods =['GET', 'POST'])

def update_keywords():
  try:
    id = current_user.id
    keywords = Keyword.query.filter_by(designguide_id = id).first()

    keywords.keyword1 = request.form.get('keyword1')
    keywords.keyword2 = request.form.get('keyword2')
    keywords.keyword3 = request.form.get('keyword3')
    keywords.keyword4 = request.form.get('keyword4')
    keywords.keyword5 = request.form.get('keyword5')
    keywords.keyword6 = request.form.get('keyword6')
    
    keywords.save()
    element = 'Key Words'
    success = f'Your {element} have been successfully updated'
    return render_template('design_elements/update.html', element = element, success = success)
  except:
    error = error ='An error occurred while processing your update. Please try again'
    return render_template('design_elements/update.html', element = element, error = error)



@blueprint.route('/elements/update/color_palette', methods =['GET', 'POST'])
def update_color():
  try:
    id = current_user.id
    element = 'Color Palette'
    color = Color.query.filter_by(designguide_id = id).first()

    color.color1 = request.form.get('color1')
    color.color2 = request.form.get('color2')
    color.color3 = request.form.get('color3')
    color.color4 = request.form.get('color4')
    color.color5 = request.form.get('color5')
    color.color6 = request.form.get('color6')
    
    color.save()
    success = f'Your {element} have been successfully updated'
    return render_template('design_elements/update.html', element = element, success = success)
  except:
    error = error ='An error occurred while processing your update. Please try again'
    return render_template('design_elements/update.html', element = element, error = error)