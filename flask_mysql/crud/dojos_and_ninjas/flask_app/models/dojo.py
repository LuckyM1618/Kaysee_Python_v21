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
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(cls.database).query_db(query)

        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )

        return dojos

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

    @classmethod
    def get_one_dojo_with_ninjas( cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s"

        results = connectToMySQL(cls.database).query_db(query, data)

        dojo = cls( results[0] )
        print(dojo)
        for ninja_info in results:
            ninja_data = {
                'id' : ninja_info['ninjas.id'],
                'first_name' : ninja_info['first_name'],
                'last_name' : ninja_info['last_name'],
                'age' : ninja_info['age'],
                'created_at' : ninja_info['ninjas.created_at'],
                'updated_at' : ninja_info['ninjas.updated_at']
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data) )

        return dojo

    @classmethod
    def save( cls, data ):
        query = "INSERT INTO dojos (`name`, `created_at`, `updated_at`) VALUES (%(name)s, NOW(),NOW());"

        return connectToMySQL( cls.database ).query_db( query, data )
