from flask import request, jsonify, Blueprint, abort
from tables.categorias.model import *

categoria_blueprint = Blueprint('categoria',__name__)

@categoria_blueprint.route("/categorias", methods=["GET"])
def categoList():
    all_categories = Categoria.query.all()
    result = categorias_schema.dump(all_categories)
    return jsonify(result.data)

@categoria_blueprint.route("/categoria", methods =["POST"])
def adminAdd():
    categoria = request.json['name']
    new_categoria = Categoria(categoria)
    db.session.add(new_categoria)
    db.session.commit()
    return jsonify(new_categoria.serialize())
