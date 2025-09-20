
age = int(input("What is your age?:"))

rating = input("What is your movie/show rating:")


if rating == "G":
    print("You can watch G rated shows/movies")
elif rating == "PG":
    if age > 6:
        print("You can Watch PG rated shows/movies")
    else:
        print("You are too young to watch PG rated shows/movies!")
elif rating == "PG-13":
    if age > 13:
        print("You can watch PG-13 rated shows/movies")
    else:
        print("You are too young to watch PG-13 rated shows/movies!")
elif rating == "R":
    if age > 17:
        print("You can watch R rated shows/movies")    
    else:
        print("You cannot watch R rated shows/movies!!!")