from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(120), unique=True, nullable=True)
    # password = db.Column(db.String(80), unique=False, nullable=True)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    favoritos_user = db.relationship('Favoritos', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "Name": self.name,
            # do not serialize the password, its a security breach
        }
    
class Films(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    episode_id = db.Column(db.Integer)
    opening_crawl = db.Column(db.String(250), nullable=True)
    director = db.Column(db.String(250), nullable=True)
    producer = db.Column(db.String(250), nullable=True)
    release_date = db.Column(db.String(250), nullable=True)
    # id_species = db.Column(db.Integer, db.ForeignKey('species.id'))
    # id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))
    # id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    # id_people = db.Column(db.Integer, db.ForeignKey('peple.id'))
    # id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    url = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)

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
    birth_year = db.Column(db.String(250), nullable=True)
    eye_color = db.Column(db.String(250), nullable=True)
    gender = db.Column(db.String(250), nullable=True)
    hair_color = db.Column(db.String(250), nullable=True)
    height = db.Column(db.String(250), nullable=True)
    mass = db.Column(db.String(250), nullable=True)
    skin_color = db.Column(db.String(250), nullable=True)
    homeworld = db.Column(db.String(250), nullable=True)
    url = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    id_species = db.Column(db.Integer, db.ForeignKey('species.id'))
    # id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))
    id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    favoritos_people = db.relationship('Favoritos', backref='people', lazy=True)
    vehicle = db.relationship('Vehicles', backref='people', lazy=True)
    species = db.relationship('Species', backref='people', lazy=True)
    planets = db.relationship('Planets', backref='people', lazy=True)
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
    model = db.Column(db.String(250), nullable=True)
    vehicle_class = db.Column(db.String(250), nullable=True)
    manufacturer = db.Column(db.String(250), nullable=True)
    length = db.Column(db.String(250), nullable=True)
    cost_in_credits = db.Column(db.String(250), nullable=True)
    crew = db.Column(db.String(250), nullable=True)
    passengers = db.Column(db.String(250), nullable=True)
    max_atmosphering_speed = db.Column(db.String(250), nullable=True)
    cargo_capacity = db.Column(db.String(250), nullable=True)
    consumables = db.Column(db.String(250), nullable=True)
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    url = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)
    
    favoritos_vehicle = db.relationship('Favoritos', backref='vehicle', lazy=True)
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
    diameter = db.Column(db.String(250), nullable=True)
    rotation_period = db.Column(db.String(250), nullable=True)
    orbital_period = db.Column(db.String(250), nullable=True)
    gravity = db.Column(db.String(250), nullable=True)
    population = db.Column(db.String(250), nullable=True)
    climate = db.Column(db.String(250), nullable=True)
    terrain = db.Column(db.String(250), nullable=True)
    surface_water = db.Column(db.String(250), nullable=True)
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    url = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)

    favoritos_planets = db.relationship('Favoritos', backref='planets', lazy=True)
    
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
#     name = db.Column(db.String(250), nullable=True)
#     password = db.Column(db.String(250), nullable=True)

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
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    id_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    id_species = db.Column(db.Integer, db.ForeignKey('species.id'))
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # id_starships = db.Column(db.Integer, db.ForeignKey('starships.id'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))


    #user = db.relationship('User', backref='favoritos', lazy=True)
    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        if self.id_people is not None:
            people = People.query.filter_by(id=self.id_people).first()
            return{
                "id": self.id,
                "user": self.id_user,
                "info_people": people.serialize()
            }
        if self.id_planets is not None:
            planet = Planets.query.filter_by(id=self.id_planets).first()
            return{
                "id": self.id,
                "user": self.id_user,
                "info_planet": planet.serialize()
            }
        return {
            "id": self.id,
            "user": self.id_user,
            "info_people": None if self.id_people is None else people.serialize(),
            "info_planet": None if self.id_planets is None else planet.serialize()
            # do not serialize the password, its a security breach
        }

class Starships(db.Model):
    __tablename__ = 'starships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=True)
    starship_class = db.Column(db.String(250), nullable=True)
    manufacturer = db.Column(db.String(250), nullable=True)
    cost_in_credits = db.Column(db.String(250), nullable=True)
    length = db.Column(db.String(250), nullable=True)
    crew = db.Column(db.String(250), nullable=True)
    passengers = db.Column(db.String(250), nullable=True)
    max_atmosphering_speed = db.Column(db.String(250), nullable=True)
    hyperdrive_rating = db.Column(db.String(250), nullable=True)
    MGLT = db.Column(db.String(250), nullable=True)
    cargo_capacity = db.Column(db.String(250), nullable=True)
    consumables = db.Column(db.String(250), nullable=True)
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    # id_people = db.Column(db.Integer, db.ForeignKey('peple.id'))
    url = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)

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
    classification = db.Column(db.String(250), nullable=True)
    designation = db.Column(db.String(250), nullable=True)
    average_height = db.Column(db.String(250), nullable=True)
    average_lifespan = db.Column(db.String(250), nullable=True)
    eye_colors = db.Column(db.String(250), nullable=True)
    hair_colors = db.Column(db.String(250), nullable=True)
    skin_colors = db.Column(db.String(250), nullable=True)
    language = db.Column(db.String(250), nullable=True)
    homeworld = db.Column(db.String(250), nullable=True)
    # id_people = db.Column(db.Integer, db.ForeignKey('peple.id'))
    # id_films = db.Column(db.Integer, db.ForeignKey('films.id'))
    url = db.Column(db.String(250), nullable=True)
    created = db.Column(db.String(250), nullable=True)
    edited = db.Column(db.String(250), nullable=True)

    favoritos_species = db.relationship('Favoritos', backref='species', lazy=True)
    def __repr__(self):
        return '<Species %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
