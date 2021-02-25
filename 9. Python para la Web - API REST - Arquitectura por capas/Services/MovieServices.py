from flask import jsonify,request
import json
import sys
sys.path.append("..")
from Entity.Movie import MovieModel
from Repository.MovieRepository import MovieRepository

class MovieService():
    
    def __init__(self):
        print("Se inicio movie service")
    
    def GetAll():
        result = []
        movies = MovieRepository.GetAll()
        for item in movies:
            result.append(item.toJson())
        return result

    def GetById(id):
        print("Get By Id" + str(id))

    def Save(json):
        try:
            movie = MovieModel(json['id'],
                               json['name'],
                               json['director'],
                               json['costo'],
                               json['moneda'],
                               json['annio'])
            MovieRepository.Save(movie)
            return True
        except:
            return False

    def Update(json):
        try:
            movieParam = MovieModel(json['id'],
                               json['name'],
                               json['director'],
                               json['costo'],
                               json['moneda'],
                               json['annio'])
            movie = None
            movies = MovieRepository.GetAll()
            for item in movies:
                if item.id == movieParam.id:
                    movie = item
                    break
            if(movie!=None):
                movie.name = movieParam.name
                movie.director = movieParam.director
                movie.costo = movieParam.costo
                movie.moneda = movieParam.moneda
                movie.annio = movieParam.annio
                return True
            else:
                return False
        except:
            return False

    def DeleteById(id):
        try:
            movie = None
            movies = MovieRepository.GetAll()
            for item in movies:
                if item.id == id:
                    movie = item
                    break
            if(movie!=None):
                MovieRepository.Delete(movie)
                return True
            else:
                return False
        except:
            return False
        
print("SE ESTA INVOCANDO A LA CLASE MOVIE SERVICE")
