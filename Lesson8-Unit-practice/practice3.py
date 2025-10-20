songs = int(input("How many songs will you listen to?:"))

n = 0
while songs > 0:
    songs -= 1
    n += 3.5
print(f"You will listen for {n} mins")