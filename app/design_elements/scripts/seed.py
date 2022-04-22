from app.app import create_app
from app.design_elements.models import Designelement
from app.extensions.database import db

app = create_app()
app.app_context().push()

elements_data = {
  'font' : {'name': 'Font', 'url': 'https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap'},
  'logo' : {'name': 'Logo', 'url': 'https://study-eu.s3.amazonaws.com/uploads/university/code-university-berlin-logo.png'},
  'color_palette' : {'name': 'Color Palette', 'url': 'https://www.color-hex.com/color-palette/1011024'},
  'keywords' : {'name': 'Key Word', 'url': 'https://grids.obys.agency/'},
}

for slug, element in elements_data.items():
    new_element = Designelement(slug=slug, name=element['name'], url=element['url'])
    db.session.add(new_element)

db.session.commit()
