from app.app import create_app
from app.design_elements.models import Designelement   
from app.users.models import User
from app.extensions.database import db

app = create_app()
app.app_context().push()


design_elements = {

    
    'logo' : { 'name' : 'Logo'},
    'font' : { 'name' : 'Font'},
    'color_pallete' : { 'name' : 'Color Palette' },
    'keywords' : {'name' : 'Keywords'}

}

for slug, element in design_elements.items():
    new_element = Designelement(slug = slug , name = element['name'])
    db.session.add(new_element)

db.session.commit()