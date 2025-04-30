from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# Model
class Artist:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.rate = data_dict['rate']
        self.image = data_dict['image']
        self.style = data_dict['style']
        self.is_popular = data_dict['is_popular']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
    
    # ? create: to prepare query insert with data from HTML
    @classmethod
    def create_artist(cls, data):
        # data={first_name: Mostafa, last_name: daleji, rate: 4, image: artist.png, style: mezwed, is_popular: 0}
        query= """INSERT INTO artists (first_name, last_name, rate, image, style, is_popular)
                VALUES (%(first_name)s, %(last_name)s, %(rate)s, %(image)s, %(style)s, %(is_popular)s);"""
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        # result contain id of created artist
        return result
    # ? read All: to develop query to read all artists from DB
    @classmethod
    def get_all_artists(cls):
        query= "SELECT * FROM artists;"
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        # results contain a list of dictionaries of all artists in the DB
        all_artists=[]
        for row in results:
            artist = cls(row)
            all_artists.append(artist)
        return all_artists
    
    # ?UPDATE: to create quer for updating an artist
    @classmethod
    def update(cls,data):
        query= """UPDATE artists SET
                first_name = %(first_name)s,
                last_name = %(last_name)s,
                image = %(image)s,
                rate = %(rate)s,
                style = %(style)s,
                is_popular = %(is_popular)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # READ ONE : to get a specific artist from the DB
    @classmethod
    def get_one_artist(cls,data):
        query="SELECT * FROM artists WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result)>0:
            print(result)
            artist= cls(result[0])
            return artist
        return False
    
    # DELETE: a query to delete one artist by id
    @classmethod
    def delete(cls, data):
        query= "DELETE FROM artists WHERE id =%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)