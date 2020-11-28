def get_movie_id(movies, title, year=None):
    res = movies.loc[movies['title'] == title]
    if year:
        res = res.loc[res['year'] == year]

    if res.shape[0] > 1:
        print("Ambiguous: found")
        print(f"{res.loc[:,'title']} {res.loc[:,'year']}")
    elif res.shape[0] == 0:
        print('not found')
    else:
        return res.index[0]
def get_movie_name(movies, movie_id):
    return movies.loc[movies['movie_id']==movie_id].loc[:,'title'].values[0]
    # I chose to change the way the movie's name is retrieved
    # Because the proposed way rests on the belief that the DataFrame's index progresses just like the movie_id column.
    # This did not take into account the possibility of removed movies(with reseted indexes) along the way, and could have resulted in mismatches.

def get_movie_year(movies, movie_id):
    return movies.loc[movies['movie_id']==movie_id].loc[:,'year'].values[0]
    # Same than in get_movie_name
