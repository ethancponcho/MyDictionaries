movie_ratings = {"The Shawshank Redemption": '10',
                 "Space Jam": '6',
                 "Reservoir Dogs": '9',
                 "The Godfather": '10',
                 "Avatar": '7',
                 "Kingdom of Heaven": '4'}

def main():
    movie_select = input('Enter a movie title: ').title()
    
    recommend_movie(movie_ratings, movie_select)
    
def recommend_movie(movie_ratings, movie):
    found = False
    
    #find movie in dictionary
    for k in movie_ratings:
        if movie in movie_ratings:
            found = True
        elif movie not in movie_ratings:
            if movie >= 8:
                
                print(f'Movie not found. Here are some other recommended movies you might like: {movie}')
        
            
        if found:
            if movie >= 8:
                print(f'Watching {movie} is recommended by top critics.')
            elif movie < 8:
                print(f'Watching {movie} is not recommended. It is suggested to watch another movie')
                
main()