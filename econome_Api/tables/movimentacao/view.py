from flask import request, jsonify, Blueprint, abort
from tables.categorias.model import *

mov_blueprint = Blueprint('movimentacao', __name__)
@mov_blueprint.route("/movimentacoes/<int: idCategoria>/<int: imes>/<int: iano>/<int: fmes>/<int: fano>", methods=["GET"])
