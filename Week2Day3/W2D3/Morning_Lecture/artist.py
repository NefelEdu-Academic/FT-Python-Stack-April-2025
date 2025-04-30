from mysqlconnection import connectToMySQL
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
    
    @classmethod
    def create_artist(cls, data):
        # data={first_name: Mostafa, last_name: daleji, rate: 4, image: artist.png, style: mezwed, is_popular: 0}
        query= """INSERT INTO artists (first_name, last_name, rate, image, style, is_popular)
                VALUES (%(first_name)s, %(last_name)s, %(rate)s, %(image)s, %(style)s, %(is_popular)s);"""
        result = connectToMySQL("artists_schema").query_db(query, data)
        print(result)
        return result
    
    @classmethod
    def get_all_artists(cls):
        query= "SELECT * FROM artists;"
        results = connectToMySQL("artists_schema").query_db(query)
        # print(results)
        all_artists=[]
        for row in results:
            artist = cls(row)
            all_artists.append(artist)
        return all_artists