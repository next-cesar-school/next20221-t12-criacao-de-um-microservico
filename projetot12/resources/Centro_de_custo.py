from flask_restful import Resource

class Centro_de_custo(Resource):
    def get(self):
        return {1:"nome", 2:"id"}