![Layback_Type](https://user-images.githubusercontent.com/101812100/166223243-3a665c7b-d377-4583-b859-9483564996c2.png)

current version: https://powerful-garden-83125.herokuapp.com/

## The Problem
The process of composing layouts following a brand guide can be very tedious. Essentially there is very little room for creativity or originality as the task is restricted to following the already established parameters in a repetitive matter to ensure graphic coherence.

**Consequences** 

* Time-consuming process
* No employee of a company is expected to deliver graphically pleasant content for presentations
* Content often ends up looking rather unprofessional and with no coherence

## The Solution
Luckily all repetitive tasks that follow established parameters can be automatized. And that is exactly what Layback strives for:
The automatic composition of content following a company's Brand Guidelines.

### What does the process look like?
A company registers on the platform and creates a list of the employees (the design team) that build/upload those Guidelines to the platform. The rest of the employees will now be able to upload their content (text, images, graphics) and get a graphically coherent and pleasant composition in return.

### In which state is the project currently?
As of this version, you're looking at the foundation of the web app. 
The actual valuable feature of the project is yet to be developed.
For now, users can register and upload a logo, a font, a color palette in hex code, and some keywords that fit the brand's image (i.e. fun, colorful, young…). 

## Tech Stack

### Build with 
* HTML
* CSS
* JavaScript
* Python
  * Flask
    * SQLAlchemy
    * Jinja2
   
### Server, Deployment & Data Base 
* Gunicorn
* Heroku
* Postgres

![LayBack Diagram Transparent3](https://user-images.githubusercontent.com/101812100/166223273-13b1055c-a17f-4f04-b695-7a506611e197.png)





## Installment & Running Instructions

First & foremost you should have python3 installed. To check your version run the following command.

`python3 --version`

Before starting to mess with the code make sure to set up a **Virtual enviroment**. This will keep the packages you will install for the project isolated from the rest of your computer files.

`python3 -m venv venv`

Oh... And never forget to activate the Virtual enviroment before working on the code.

`. venv/scripts/activate`

(venv) means the virtual enviroment is activated. To deactivate it simply enter

`deactivate`

Now that you have all the packages installed you can run tests with pytest whenever you make changes to the project.

`pytest -v`

Another important step before working on the code is to define enviroment variables.
First, create an .env file. 

`touch .env`

Copy and paste the following lines inside the file. These variables will set up your virtual environment to work properly.
```
FLASK_ENV=development

DATABASE_URL=sqlite:///database.db

FLASK_APP=run.py

SECRET_KEY= 
```
Use https://randomkeygen.com/ to generate a SECRET_KEY if your feeling uninspired. It is however important that you use one!

In order to ensure that you install the exact same versions of the packages that are being used in the project; use the command below.

`python -m pip install -r requirements.txt`

To set up the **database** run de following commands.

`flask db init`

`flask db migrate -m 'Init db'`

`flask db upgrade`

`python -m app.scripts.seed`

Your all set up!

To run the code run

`python run.py`


## How to use

1. Click on _Join Now_ to register.
2. Enter the first form and ignore the one underneath (YOUR TEAM is not relevant to the current state of the project)
3. Select the content you wish to upload to the design guide
4. Finally click on _View Your Design Guide_
5. Here you can access and edit your content

