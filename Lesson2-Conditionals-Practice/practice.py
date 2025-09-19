
age = int(input("What is your age?:"))

rating = input("What is your movie/show rating:")


if 0 <= age <= 6:
    print("You can watch G rated shows/movies")
elif 6 < age <= 13:
    print("You can watch PG rated shows/movies")
elif 13  < age <=17:
    print("You can watch PG-13 rated shows/movies")
else:
    print("You can watch R rated shows/movies")