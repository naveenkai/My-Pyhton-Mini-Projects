from imdb import IMDb
movie = IMDb().get_movie('012346')
print(movie)

for i in movie["directors"]:
    print(i)
    
    movies = IMDb().get_top250_movies()
for i in movies:
    print(i)
