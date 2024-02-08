from diction import movies
movie = movies
def sub(movie):
    s = []
    for i in movie:
        if i["imdb"] >= 5.5:
            s.append(i)
    return s
print(sub(movie))