from app.models.connection import MySQLConnection

MySQLConnection().query_db('''
    CREATE TABLE IF NOT EXISTS `world`.`cities` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `languages` TEXT,
    `country_id` INT NOT NULL,
    PRIMARY KEY (`id`),
    foreign key (country_id) references countries(id))
    ENGINE = InnoDB;
''')

class City:

    @classmethod
    def get_all(cls):
        countries = MySQLConnection().query_db('select * from countries')
        return countries
    
    @classmethod
    def add(cls, name, languages, country_id):
        query = 'insert into cities (name, languages, country_id) values (%(name)s, %(languages)s, %(country_id)s)'
        data = {
            'name': name,
            'languages': languages,
            'country_id': country_id
        }

        new_city_id = MySQLConnection().query_db(query, data)
        return new_city_id