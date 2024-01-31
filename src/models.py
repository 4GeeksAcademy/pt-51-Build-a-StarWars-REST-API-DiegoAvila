from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Films(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    episode_id = db.Column(db.Integer)
    opening_crawl = db.Column(db.String(250), nullable=False)
    director = db.Column(db.String(250), nullable=False)
    producer = db.Column(db.String(250), nullable=False)
    release_date = db.Column(db.String(250), nullable=False)
    # id_species = db.Column(db.Integer, db.ForeignKey('species.id'))
    # id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))
    # id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    # id_people = db.Column(db.Integer, db.ForeignKey('peple.id'))
    # id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    url = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    # favoritos_films = db.relationship('Favoritos', backref='films', lazy=True)
    # people = db.relationship('People', backref='films', lazy=True)
    # vehicles = db.relationship('Vehicles', backref='films', lazy=True)
    # starships = db.relationship('Starships', backref='films', lazy=True)
    # species = db.relationship('Species', backref='films', lazy=True)
    # planets = db.relationship('Planets', backref='films', lazy=True)

    def __repr__(self):
        return '<Films %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "title ": self.title,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    __tablename__ = 'people'
    # Here we define db.Columns for the table person
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # id_species = db.Column(db.Integer, db.ForeignKey('species.id'))
    # id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))
    # id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    # favoritos_people = db.relationship('Favoritos', backref='people', lazy=True)
    vehicle = db.relationship('Vehicles', backref='people', lazy=True)
    # species = db.relationship('Species', backref='people', lazy=True)
    # starships = db.relationship('Starships', backref='people', lazy=True)
    
    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
class Vehicles(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    url = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    # favoritos_vehicle = db.relationship('Favoritos', backref='vehicle', lazy=True)
    # people = db.relationship('People', backref='vehicle', lazy=True)
    #person = db.relationship(Person)
    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

    def to_dict(self):
        return {}
class Planets(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(250), nullable=False)
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # id_people = db.Column(db.Integer, db.ForeignKey('peple.id'))
    url = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    # favoritos_planets = db.relationship('Favoritos', backref='planets', lazy=True)
    
    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

# class Users(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False)
#     password = db.Column(db.String(250), nullable=False)

#     # favoritos_user = db.relationship('Favoritos', backref='users', lazy=True)

#     def __repr__(self):
#         return '<Users %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             # do not serialize the password, its a security breach
#         }

class Favoritos(db.Model):
    __tablename__ = 'favoritos'

    id = db.Column(db.Integer, primary_key=True)
    # id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    # id_people = db.Column(db.Integer, db.ForeignKey('peple.id'))
    # id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    # id_species = db.Column(db.Integer, db.ForeignKey('species.id'))
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))
    # id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))

    #user = db.relationship('Users', backref='hola', lazy=True)


class Starships(db.Model):
    __tablename__ = 'starships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    hyperdrive_rating = db.Column(db.String(250), nullable=False)
    MGLT = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # id_people = db.Column(db.Integer, db.ForeignKey('peple.id'))
    url = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    # favoritos_starships = db.relationship('Favoritos', backref='starships', lazy=True)

    def __repr__(self):
        return '<Starships %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    classification = db.Column(db.String(250), nullable=False)
    designation = db.Column(db.String(250), nullable=False)
    average_height = db.Column(db.String(250), nullable=False)
    average_lifespan = db.Column(db.String(250), nullable=False)
    eye_colors = db.Column(db.String(250), nullable=False)
    hair_colors = db.Column(db.String(250), nullable=False)
    skin_colors = db.Column(db.String(250), nullable=False)
    language = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    # id_people = db.Column(db.Integer, db.ForeignKey('peple.id'))
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    url = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    # favoritos_species = db.relationship('Favoritos', backref='species', lazy=True)
    def __repr__(self):
        return '<Species %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
