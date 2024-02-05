"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Favoritos
#from models import Person

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.url_map.strict_slashes = False


db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

################ENDPOINT###############

# @app.route('/user', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200
# obtener todo los personajes
@app.route('/people', methods=['GET'])
def get_all_people():
    people_query = People.query.all() #estamos haciendo una consulta a la User para que traiga todos
    people_query = list(map(lambda item: item.serialize(), people_query))#procesamos la info consultada y la volvemos un array
    # print(people_query)
    
    if people_query == []:
        return jsonify({
            "msg": "People not found"
        }), 404
    
    response_body = {
        "msg": "ok",
        "people": people_query
    }
    return jsonify(response_body), 200

# obtener los datos de un solo personaje
@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):
    people_query = People.query.filter_by(id = people_id).first() #estamos haciendo una consulta a la User para que traiga todos
    # print(people_query)
    
    if people_query == None:
        return jsonify({
            "msg": "People not found"
        }), 404
    
    response_body = {
        "msg": "ok",
        "people": people_query.serialize()
    }
    return jsonify(response_body), 200

# obtener todo los planetas
@app.route('/planets', methods=['GET'])
def get_all_planets():
    planet_query = Planets.query.all() #estamos haciendo una consulta a la User para que traiga todos
    planet_query = list(map(lambda item: item.serialize(), planet_query))#procesamos la info consultada y la volvemos un array
    # print(planet_query)
    
    if planet_query == []:
        return jsonify({
            "msg": "Planets not found"
        }), 404
    
    response_body = {
        "msg": "ok",
        "Planet": planet_query
    }
    return jsonify(response_body), 200

# obtener los datos de un solo planeta
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    planet_query = Planets.query.filter_by(id = planet_id).first() #estamos haciendo una consulta a la User para que traiga todos
    print(planet_query)
    
    if planet_query == None:
        return jsonify({
            "msg": "People not found"
        }), 404
    
    response_body = {
        "msg": "ok",
        "people": planet_query.serialize()
    }
    return jsonify(response_body), 200

# obtener todo los usuarios
@app.route('/user', methods=['GET'])
def get_all_users():
    user_query = User.query.all() #estamos haciendo una consulta a la User para que traiga todos
    user_query = list(map(lambda item: item.serialize(), user_query))#procesamos la info consultada y la volvemos un array
    # print(user_query)
    
    if user_query == []:
        return jsonify({
            "msg": "User not found"
        }), 404
    
    response_body = {
        "msg": "ok",
        "User": user_query
    }
    return jsonify(response_body), 200

#obten los favoritos de todos los usuarios

@app.route('/user/favoritos/', methods=['GET'])
@jwt_required()
def get_favorite_one_user():

    current_user = get_jwt_identity()

    user_query = User.query.filter_by(name=current_user).first() #estamos haciendo una consulta a la User para que traiga todos
    # user_query = list(map(lambda item: item.serialize(), user_query)) #estamos haciendo una consulta a la User para que traiga todos
    print(user_query.id)
    
    if not user_query:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    # Obtenemos los favoritos del usuario actual
    user_favorites_query = Favoritos.query.filter_by(id_user=user_query.id).all()
    user_favorites_query = list(map(lambda item: item.serialize(), user_favorites_query))

    if not user_favorites_query:
        return jsonify({"msg": "No hay favoritos registrados"}), 404

    response_body = {
        "msg": "ok",
        "favorites": user_favorites_query
    }

    return jsonify(response_body), 200

# añade un planeta favorito al usuario actual
@app.route('/favoritos/planets/<int:id_planet>', methods=['POST'])
def add_favorite_planet_to_user(id_planet):

    body = request.json

    new_favorit_planet = Favoritos(id_user = body["id_user"], id_planets = id_planet)
    db.session.add(new_favorit_planet)
    db.session.commit()
    print(new_favorit_planet)

    # if new_favorit_planet == "-":
    #     return jsonify({
    #         "msg": "User not found"
    #     }), 404
    
    response_body = {
        "msg": "favorito aderido",
    }
    return jsonify(response_body), 200

# añade un personaje favorito al usuario actual
@app.route('/favoritos/people/<int:id_people>', methods=['POST'])
def add_favorite_people_to_user(id_people):

    body = request.json

    new_favorit_people = Favoritos(id_user = body["id_user"], id_people = id_people)
    db.session.add(new_favorit_people)
    db.session.commit()
    print(new_favorit_people)

    # if new_favorit_people == "-":
    #     return jsonify({
    #         "msg": "User not found"
    #     }), 404
    
    response_body = {
        "msg": "favorito aderido",
    }
    return jsonify(response_body), 200

# elimuna un planeta favorito
@app.route('/favoritos/planets/<int:id_planet>', methods=['DELETE'])
def delete_favorite_planet_to_user(id_planet):

    body = request.json

    delete_favorite_planet = Favoritos.query.filter_by(id_planets = id_planet).first()
    db.session.delete(delete_favorite_planet)
    db.session.commit()
    # print(delete_favorite_planet)

    # if delete_favorite_planet == "-":
    #      return jsonify({
    #          "msg": "User not found"
    #      }), 404
    
    response_body = {
        "msg": "favorito eliminado",
    }
    return jsonify(response_body), 200

# elimuna un personaje favorito
@app.route('/favoritos/people/<int:id_people>', methods=['DELETE'])
def delete_favorite_people_to_user(id_people):

    body = request.json

    delete_favorite_people = Favoritos.query.filter_by(id_people = id_people).first()
    db.session.delete(delete_favorite_people)
    db.session.commit()
    # print(delete_favorite_planet)

    # if delete_favorite_planet == "-":
    #      return jsonify({
    #          "msg": "User not found"
    #      }), 404
    
    response_body = {
        "msg": "favorito eliminado",
    }
    return jsonify(response_body), 200

@app.route("/login", methods=["POST"])
def login():
    # id = request.json.get("id", None)
    name = request.json.get("name", None)
    password = request.json.get("password", None)

    user_query = User.query.filter_by(name=name).first()

    if name != user_query.name or password != user_query.password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=name)
    return jsonify(access_token=access_token)

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    info_profile = User.query.filter_by(name=current_user).first()

    return jsonify({"user":info_profile.serialize()}), 200
    # return jsonify(logged_in_as=current_user), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
