from diction import movies
movies = movies
def iscat(movies,ct):
    d = []
    for i in movies:
        if i["category"] == ct:
            d.append(i)
    return d
print(iscat(movies,input()))