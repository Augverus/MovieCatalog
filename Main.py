movies = [
    {
        "title": "The Shawshank Redemption",
        "rating": 9.3,
        "genres": ["Drama"],
        "min_age": 17,
        "year": 1994,
        "runtime": 142
    },
    {
        "title": "The Godfather",
        "rating": 9.2,
        "genres": ["Crime", "Drama"],
        "min_age": 17,
        "year": 1972,
        "runtime": 175
    },
    {
        "title": "The Dark Knight",
        "rating": 9.1,
        "genres": ["Action", "Crime", "Drama"],
        "min_age": 13,
        "year": 2008,
        "runtime": 152
    },
    {
        "title": "The Godfather Part II",
        "rating": 9.0,
        "genres": ["Crime", "Drama"],
        "min_age": 17,
        "year": 1974,
        "runtime": 202
    },
    {
        "title": "12 Angry Men",
        "rating": 9.0,
        "genres": ["Crime", "Drama"],
        "min_age": 12,
        "year": 1957,
        "runtime": 96
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "rating": 9.0,
        "genres": ["Action", "Adventure", "Fantasy"],
        "min_age": 13,
        "year": 2003,
        "runtime": 201
    },
    {
        "title": "Schindler's List",
        "rating": 9.0,
        "genres": ["Biography", "Drama", "History"],
        "min_age": 17,
        "year": 1993,
        "runtime": 195
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "rating": 8.9,
        "genres": ["Action", "Adventure", "Fantasy"],
        "min_age": 13,
        "year": 2001,
        "runtime": 178
    },
    {
        "title": "Pulp Fiction",
        "rating": 8.9,
        "genres": ["Crime", "Drama"],
        "min_age": 17,
        "year": 1994,
        "runtime": 154
    },
    {
        "title": "The Good, the Bad and the Ugly",
        "rating": 8.8,
        "genres": ["Adventure", "Western"],
        "min_age": 16,
        "year": 1966,
        "runtime": 178
    },
    {
        "title": "The Lord of the Rings: The Two Towers",
        "rating": 8.8,
        "genres": ["Action", "Adventure", "Fantasy"],
        "min_age": 13,
        "year": 2002,
        "runtime": 179
    },
    {
        "title": "Forrest Gump",
        "rating": 8.8,
        "genres": ["Drama", "Romance"],
        "min_age": 13,
        "year": 1994,
        "runtime": 142
    },
    {
        "title": "Fight Club",
        "rating": 8.8,
        "genres": ["Drama"],
        "min_age": 17,
        "year": 1999,
        "runtime": 139
    },
    {
        "title": "Inception",
        "rating": 8.8,
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "min_age": 13,
        "year": 2010,
        "runtime": 148
    },
    {
        "title": "Star Wars: Episode V - The Empire Strikes Back",
        "rating": 8.7,
        "genres": ["Action", "Adventure", "Fantasy"],
        "min_age": 10,
        "year": 1980,
        "runtime": 124
    },
    {
        "title": "The Matrix",
        "rating": 8.7,
        "genres": ["Action", "Sci-Fi"],
        "min_age": 17,
        "year": 1999,
        "runtime": 136
    },
    {
        "title": "Goodfellas",
        "rating": 8.7,
        "genres": ["Biography", "Crime", "Drama"],
        "min_age": 17,
        "year": 1990,
        "runtime": 145
    },
    {
        "title": "One Flew Over the Cuckoo's Nest",
        "rating": 8.7,
        "genres": ["Drama"],
        "min_age": 17,
        "year": 1975,
        "runtime": 133
    },
    {
        "title": "Se7en",
        "rating": 8.6,
        "genres": ["Crime", "Drama", "Mystery"],
        "min_age": 17,
        "year": 1995,
        "runtime": 127
    },
    {
        "title": "Seven Samurai",
        "rating": 8.6,
        "genres": ["Action", "Drama"],
        "min_age": 14,
        "year": 1954,
        "runtime": 207
    }
]
while True: 
    print("\n==== Movie Recommendator ====")
    print("1 - Choose by Rating")
    print("2 - Choose by genre")
    print("3 - Choose by Minimum age")
    print("4 - Runtime")
    print("5 - Year Made")
    print("6 - Exit")

    Choice = input("Choose an option ")
    if Choice == "1":
        print("Type 'back' to return to the main menu.")
        user_rating = input("enter you desired rating: ")
        if user_rating.lower() == "back":
            continue
        user_rating = float(user_rating)
        for movie in movies:
            if movie["rating"] >= user_rating:
                print("----------------------------------------")
                print(f'{movie["title"]}')
                print(f'\nhas rating of {movie["rating"]} and is equal or higher than you desired rating')
                print()
    elif Choice == "2":
        print("\nAvailable genres:")
        print("Action, Adventure, Biography, Crime, Drama, Fantasy,")
        print("History, Mystery, Romance, Sci-Fi, Western")
        print("Type 'back' to return to the main menu.")

        print("enter desired genre ")
        user_input = input("if you want multiple genres seperate them with , :")
        if user_input.lower() == "back":
            continue
        user_genres = user_input.split(",")
        clean_genres = []
        for genre in user_genres:
            clean_genres.append(genre.strip().lower())
        for movie in movies:
            matches = True
            movie_genres = []
            for genre in movie["genres"]:
                movie_genres.append(genre.lower())
            for genre in clean_genres:
                if genre not in [g.lower() for g in movie["genres"]]:
                    matches = False
            if matches:
                print("----------------------------------------")
                print(movie["title"])
                print(f'this movie has the following genres {movie["genres"]}')
    elif Choice == "3":
        print("Type 'back' to return to the main menu.")
        user_age = input("enter you desired minimum age: ")
        if user_age.lower == "back":
            continue
        user_age = int(user_age)
        for movie in movies:
            if user_age >= movie["min_age"]:
                print("----------------------------------------")
                print(f'{movie["title"]}')
                print(f'\nhas minimum age of {movie["min_age"]} and is equal or higher than you desired minimum age to watch: ')
                print()
    elif Choice == "4":
        print("Type 'back' to return to the main menu.")

        user_runtime = input("enter your desired runtime (will choose equal or shorter runtime) ")
        if user_runtime.lower() == "back":
            continue
        user_runtime = int(user_runtime)
        for movie in movies:
            if user_runtime >= movie["runtime"]:
                print("----------------------------------------")
                print(f'{movie["title"]}')
                print(f'\nhas runtime of {movie["runtime"]} and is equal or shorter than you desired runtime to watch')
                print()
    elif Choice == "5":
        print("\nAvailable years:")
        print("1954, 1957, 1966, 1972, 1974, 1975, 1980, 1990, 1993, 1994,")
        print("1995, 1999, 2001, 2002, 2003, 2008, 2010")
        print("Type 'back' to return to the main menu.")

        user_year = input("enter you desired year of production: ")
        if user_year.lower() == "back":
            continue
        user_year = int(user_year)
        for movie in movies:
            if user_year == movie["year"]:
                print("----------------------------------------")
                print(f'{movie["title"]}')
                print(f'this movie was made in year {movie["year"]}')
                print()
    elif Choice == "6":
        print("thanks for using")
        break
    else:
        print("invalid option bro :(")