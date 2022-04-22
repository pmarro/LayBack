from flask import Blueprint, jsonify
from .services.serialize_guides import serialize_guides
from app.design_guides.models import Designguide

blueprint = Blueprint('api', __name__)

@blueprint.route('/api/v1/design-guides')
def design_guides():
    guides = Designguide.query.all()

    return jsonify(
        serialize_guides(guides)
    )  