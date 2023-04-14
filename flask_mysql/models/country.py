from models.connection import MySQLConnection

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
    def add(cls, name, gdp, population):
        query = 'insert into countries (name, gdp, population) values (%(name)s, %(gdp)s, %(population)s)'
        data = {
            'name': name,
            'gdp': gdp,
            'population': population
        }

        new_country_id = MySQLConnection().query_db(query, data)
        return new_country_id