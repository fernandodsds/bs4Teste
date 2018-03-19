from flask_sqlalchemy import SQLAlchemy,func
from flask_marshmallow import Marshmallow
from tables import db,ma

class Movimentacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    data = db.Column(db.DateTime, default=func.now())
    idCategoria = db.Column(db.Integer)
    rendimento = db.Column(db.Boolean)


    def __init__(self, name, data, idCategoria, rendimento):
        self.name = name
        self.data = data
        self.idCategoria = idCategoria
        self.rendimento = rendimento

    def serialize(self):
        return {
            # 'id':self.id,
            # 'name': self.name,
        }

class MovSchema(ma.Schema):
    class Meta:
        fields = ('id','name','data','idCategoria', 'rendimento')


mov_schema = MovSchema()
movs_schema = MovSchema(many=True)
