from app.design_elements.models import Designelement
from app.extensions.database import db

def test_element_update(client):
    # Update Element Properties

    # Arrange
    element = Designelement(slug='logo', name='Logo', url='https://study-eu.s3.amazonaws.com/uploads/university/code-university-berlin-logo.png')
    db.session.add(element)
    db.session.commit() 
    
    # Act
    element.name = 'Font'
    element.save()

    # Assess
    updated_element = Designelement.query.filter_by(slug='logo').first()
    assert updated_element.name == 'Font'


def test_element_delete(client):
    # Deletes cookie

    # Arrange
    element = Designelement(slug='font', name='Font', url='https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap')
    db.session.add(element)
    db.session.commit()

    # Act
    element.delete()

    # Assess
    deleted_element = Designelement.query.filter_by(slug='font').first()
    assert deleted_element is None