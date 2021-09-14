from movie_model import MovieModel
import requests

def callMovieApi(page=1):
    url = f'''
        https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number={page}
    '''
    response = requests.get(url)

    responseDict = response.json() 
    movies = responseDict["data"]["movies"]
    return movies

def convert_model(movies):
    list= []

    for movie in movies:
        movie_model = MovieModel(movie["title"], movie["rating"], movie["samll_cover_image"], movie["summary"]) 
        list.append(movie_model)
    
    return list


print(type("title"))
print(type("rating"))
print(type("samll_cover_image"))
print(type("summary"))
