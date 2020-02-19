# Head First

room = ["Vijay", "Ganesh", "Jidhu", "Thanos", "Vicky"]
movies = ["The Parasite", 2019,
         "The Life of Brian", 1979,
         "The Meaning of Life", 1983,
         "1917", 2019]
fav_movies = ["The Parasite", "The Life of Brian"]

print(fav_movies[0])
print(fav_movies[1])
print(fav_movies)
print(room)
print(movies)
print(len(room))
print(room[2])

room.append("Anand")
print(room)

room.pop()
print(room)

room.extend(["Anand", "Vignesh"])
print(room)

room.insert(4, "Aashi")
print(room)

room.remove("Aashi")
print(room)


room.insert(1, 1995) #or room = ["Vijay",1995,                              "Ganesh", "Jidhu",1996, "Thanos"                      "vicky", 1997, "Anand",                                "Vignesh", 1996]
room.insert(4, 1996)
room.append(1996)
print(room)
