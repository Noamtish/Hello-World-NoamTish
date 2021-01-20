from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

from pages.Assignment10.Assignment10 import Assignment10
app.register_blueprint(Assignment10)

from pages.HW11.HW11 import HW11
app.register_blueprint(HW11)
## Page error handlers
# from pages.page_error_handlers.page_error_handlers import page_error_handlers
# app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

if __name__== '__main__':
    app.run(debug=True)