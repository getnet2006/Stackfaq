from flask import Blueprint

# create blueprint boject
bp = Blueprint('main', __name__, template_folder='templates')

from app.main import routes