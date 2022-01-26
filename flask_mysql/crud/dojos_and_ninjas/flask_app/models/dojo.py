from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    database = "dojos_and_ninjas_schema"

    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []


    @classmethod
    def get_all_dojos_with_ninjas( cls ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id"
        results = connectToMySQL(cls.database).query_db(query)

        dojos = []
        dojo_ids = []

        for dojo in results:
            if dojo['id'] not in dojo_ids:
                dojo_ids.append(dojo['id'])
                dojos.append( cls(dojo) )
            ninja_data = {
                'id' : dojo['ninjas.id'],
                'first_name' : dojo['first_name'],
                'last_name' : dojo['last_name'],
                'age' : dojo['age'],
                'created_at' : dojo['ninjas.created_at'],
                'updated_at' : dojo['ninjas.updated_at']
            }
            dojos[len(dojos) - 1].ninjas.append( ninja.Ninja(ninja_data) )

        return dojos
