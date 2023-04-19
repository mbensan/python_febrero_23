from app.models.connection import MySQLConnection

MySQLConnection().query_db('''
    CREATE TABLE IF NOT EXISTS `world`.`countries` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `gdp` BIGINT NOT NULL,
    `population` BIGINT NOT NULL,
    PRIMARY KEY (`id`))
    ENGINE = InnoDB;
''')

class Country:

    @classmethod
    def get_all(cls):
        countries = MySQLConnection().query_db('select * from countries')
        return countries
    
    @classmethod
    def get_one(cls, id):
        query = 'select * from countries where id=%(id)s'
        data = {
            'id': id
        }
        countries = MySQLConnection().query_db(query, data)
        return countries[0]
    
    @classmethod
    def get_with_cities(cls, id):
        country = cls.get_one(id)
        query = 'select * from cities where country_id=%(id)s'
        data = {
            'id': id
        }
        cities = MySQLConnection().query_db(query, data)
        country['cities'] = cities
        print(country)
        return country
    
    @classmethod
    def delete(cls, id):
        query = 'delete from countries where id=%(id)s'
        data = {
            'id': id
        }
        MySQLConnection().query_db(query, data)
        return 'País eliminado'
    
    @classmethod
    def add(cls, name, gdp, population):
        query = 'insert into countries (name, gdp, population) values (%(name)s, %(gdp)s, %(population)s)'
        data = {
            'name': name,
            'gdp': gdp,
            'population': population
        }

        new_country_id = MySQLConnection().query_db(query, data)
        return new_country_id
    

    @classmethod
    def edit(cls, id, name, gdp, population):
        query = 'update countries set name=%(name)s, gdp=%(gdp)s, population=%(population)s where id=%(id)s'
        data = {
            'id': id,
            'name': name,
            'gdp': gdp,
            'population': population
        }

        MySQLConnection().query_db(query, data)