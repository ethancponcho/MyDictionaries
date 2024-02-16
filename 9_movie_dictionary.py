movie_ratings = {"The Shawshank Redemption": 10,
                 "Space Jam": 6,
                 "Reservoir Dogs": 9,
                 "The Godfather": 10,
                 "Avatar": 7,
                 "Kingdom of Heaven": 4}

def main():
    movie_select = input('Enter a movie title: ').title()
    
    recommend_movie(movie_ratings, movie_select)
    
def recommend_movie(movie_ratings, movie):
    
    #find movie in dictionary
    #for k, v in movie_ratings.items():
    if movie in movie_ratings:
        movie_rated = movie_ratings[movie]
        if movie_rated >= 8:
            print(f'Watching {movie} is recommended by top critics.')
        elif movie_rated < 8:
            print(f'Watching {movie} is not recommended. It is suggested to watch another movie.')
            
    else:
        print('Movie not found. Here are some other recommended movies you might like:')
        for movie, rate in movie_ratings.items():
            if rate >= 8:
                print(f'{movie}')
main()