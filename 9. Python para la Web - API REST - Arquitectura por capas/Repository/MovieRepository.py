import sys
sys.path.append("..")
from Entity.Movie import MovieModel
movieList=[]
class MovieRepository():
    def __init__(self,movieList):
        movieList = movieList

    def Save(movie):
        movieList.append(movie)

    def GetAll():
        return movieList

    def Delete(movie):
        movieList.remove(movie)


print("SE ESTA INVOCANDO A LA CLASE MOVIE REPOSITORY")    
