from app.design_elements.models import Designelement, Logo

def test_design_elements_index_success(client):
    # Load Page

    # Act
    response = client.get('/elements')

    # Assess
    assert b'Upload your' in response.data


def test_elements_renders(client):
#   Paginated Index-list of design elements

    # Page loads & Renders...

    # Arrange
    new_element = Designelement(slug='dada', name='dada', url='dadada')
    new_element.save()

    # Act
    response = client.get('/elements')

    # Assess
    assert b'dada' in response.data


def test_individual_element_renders(client):
#   Individual design elements page

    # Page loads & Renders...

    # Arrange
    new_element = Designelement(slug='font', name='Font', url='https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap')
    new_element.save()

    # Act
    response = client.get('/elements/font')

    # Assess
    assert b'Upload your Font' in response.data


def test_logo_post(client):
#   Upload a File

    #Arrange
    response = client.post('/elements/logo', data={
        'buffer' : 'ñkmvnfwpkqvnepn',
        'name' : 'my_company_logo',
        'mimetype' : '(image/png)',

    })

    #Assess
    assert Logo.query.first() is not None
