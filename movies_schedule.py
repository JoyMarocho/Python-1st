current_movies = {'Wakanda Forever':'10.00',
                'Black Adam': '12:00',
                'Enola Holmes': '2.00pm',
                'Christmas Vacation':'5:00pm'}


print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movie, 'is playing at ', showtime)