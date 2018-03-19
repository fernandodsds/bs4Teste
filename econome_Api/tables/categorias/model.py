from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from tables import db,ma

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'id':self.id,
            'name': self.name,
        }

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id','name')


categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)
