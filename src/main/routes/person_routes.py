from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.views.person_register_views import PersonRegisterView

person_routes_bp = Blueprint("person_routes", __name__)

@person_routes_bp.route("/person/create", methods=["POST"])
def registry_person():
    http_request = HttpRequest(body=request.json)
    http_response = PersonRegisterView().handle(http_request)

    return jsonify(http_response.body), http_response.status_code