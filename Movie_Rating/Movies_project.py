# Class representing a Movie with its properties like title, genre, director, release_year, ratings, and average_rating.

class Movie:
    # emojis = [✔,🎥,🎬,🎞,🌟,👤,👥,ℹ,]
    all_movies = []

    # Constructor to initialize the Movie object with its properties.

    def __init__(self, title, genre, director, release_year, ratings):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.ratings = ratings
        self.average_rating = sum(self.ratings) / len(self.ratings)

    # Representation of the Movie object (used when printing the object).

    def __repr__(self):
        return f'{self.title}'

    # Class method to calculate the average rating given a list of ratings.

    @classmethod
    def average_rating(cls, ratings):
        average_rating = sum(ratings) / len(ratings)
        return average_rating

    def __str__(self):
        self.average_rating = Movie.average_rating(self.ratings)
        return f'\n🎥|{self.title}|🎥\n🎞Genre: {self.genre}\n🎬Director: {self.director}\n' \
               f'🕙Released {self.release_year} year.Rating: {self.average_rating:.1f}⭐'

    # Class method to add a new movie to the list of all_movies.

    @classmethod
    def add_movie(cls, title, genre, director, release_year, ratings: list):
        movie = Movie(title, genre, director, release_year, ratings)
        Movie.all_movies.append(movie)

    # Class method to find a movie by its title in the list of all_movies.

    def find_movie(self, name):
        for movie in Movie.all_movies:
            if name == movie.title:
                return movie


# Class representing a User with their properties like name, age, rated_movies, movie_for_recommend, and movies_to_recommend.
class User:
    users = []  # List to store all user objects.
    current_user = None  # To keep track of the current user.

    # Constructor to initialize the User object with its properties.

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.rated_movies = []
        self.movie_for_recommend = None
        self.movies_to_recommend = []

    # Class method to register a new user and set them as the current_user.

    @classmethod
    def register(cls, name, age):
        user_object = User(name, age)
        User.users.append(user_object)
        User.current_user = user_object

    # Method to rate a movie, add the rating to the movie's ratings, and update the average rating.

    def rate_movie(self, rated_movie, rate):
        self.rated_movies.append({"movie": rated_movie, 'rate': rate})
        rated_movie.ratings.append(rate)
        print('Results:')
        print(rated_movie)
        return f'\n👤✅Submitted rating: {rate:.1f}🌟\n✅New rating: 🎥|{rated_movie.title}|🎥-{rated_movie.average_rating:.1f}⭐'

    # Method to recommend movies based on the user's last rated movie's genre.

    def recommended(self):
        self.movies_to_recommend = []
        if self.rated_movies:
            self.movie_for_recommend = self.rated_movies[-1]['movie']
            for object in Movie.all_movies:
                if object.genre == self.movie_for_recommend.genre:
                    self.movies_to_recommend.append(object)
            return f'\n🔻Recommendations that you might like🔻\n\n' + '\n'.join(
                [f'🎥|{movie.title}|🎥- {movie.average_rating:.1f}⭐' for movie in self.movies_to_recommend])

    # Method to calculate similarity scores between two users based on rated movies.

    def similarity_scores(self, user_to_compare):
        usernames = [user.name for user in User.users]
        if user_to_compare in usernames:
            for user in User.users:
                if user_to_compare == user.name:
                    def calculate_similarity(list1, list2):
                        if len(list1) == 0:
                            return 0

                        common_titles = []
                        for dict1 in list1:
                            for dict2 in list2:
                                if dict1["movie"] == dict2["movie"]:
                                    common_titles.append(dict1["movie"])
                                    break

                        similarity_percentage = (len(common_titles) / len(list1)) * 100
                        return round(similarity_percentage)

                    return f"Your profile is {calculate_similarity(using.rated_movies, user.rated_movies)}% similar to {user.name}'s"

    # String representation of the User object.

    def __repr__(self):
        return f'{self.name}'

    # String representation of the User object.

    def __str__(self):
        if self.rated_movies:
            result = '\n'.join([f'{object["movie"].title}-{object["rate"]}🌟'
                                for object in self.rated_movies])
        else:
            result = f'You have not rated any movies yet.'
        profile = f'\n👥Profile:\n👤{self.name}({self.age}y.o)👤\n🔻Rated movies🔻\n' + result
        return profile


# Adding some movies to the Movie class using the add_movie method.

Movie.add_movie("The Shawshank Redemption", "Drama", "Frank Darabont", 1994, [9.3, 9.2, 9.3, 9.3, 9.4])
Movie.add_movie("The Godfather", "Crime", "Francis Ford Coppola", 1972, [9.2, 9.3, 9.2, 9.4, 9.3])
Movie.add_movie("The Dark Knight", "Action", "Christopher Nolan", 2008, [9.0, 9.1, 9.2, 9.4, 9.3])
Movie.add_movie("Pulp Fiction", "Crime", "Quentin Tarantino", 1994, [8.9, 9.1, 9.0, 8.8, 9.2])
Movie.add_movie("Fight Club", "Drama", "David Fincher", 1999, [8.8, 8.9, 8.8, 9.0, 9.1])
Movie.add_movie("Inception", "Sci-Fi", "Christopher Nolan", 2010, [8.7, 8.8, 8.9, 9.1, 9.0])
Movie.add_movie("The Matrix", "Sci-Fi", "Lana Wachowski, Lilly Wachowski", 1999, [8.7, 8.8, 8.7, 8.9, 9.0])
Movie.add_movie("Forrest Gump", "Drama", "Robert Zemeckis", 1994, [8.8, 8.9, 8.7, 8.8, 9.0])
Movie.add_movie("The Avengers", "Action", "Joss Whedon", 2012, [8.0, 8.1, 8.2, 8.4, 8.3])
Movie.add_movie("Inglourious Basterds", "War", "Quentin Tarantino", 2009, [8.9, 8.8, 8.7, 8.9, 9.1])
Movie.add_movie("The Social Network", "Biography", "David Fincher", 2010, [7.7, 7.9, 8.0, 8.5, 8.3])
Movie.add_movie("Interstellar", "Sci-Fi", "Christopher Nolan", 2014, [8.6, 8.7, 8.8, 9.0, 8.9])
Movie.add_movie("The Lion King", "Animation", "Roger Allers, Rob Minkoff", 1994, [8.5, 8.7, 8.6, 8.8, 8.9])
Movie.add_movie("Gone Girl", "Thriller", "David Fincher", 2014, [8.1, 8.2, 8.4, 8.6, 8.5])
Movie.add_movie("The Lord of the Rings: The Fellowship of the Ring", "Fantasy", "Peter Jackson", 2001,
                [8.8, 8.7, 8.9, 9.1, 9.2])

User.register('Koko', 18)
using = User.current_user

using.rate_movie(Movie.all_movies[2], 7.4)
using.rate_movie(Movie.all_movies[5], 5.9)
using.rate_movie(Movie.all_movies[9], 7.7)

User.register('defalt_user_613ti3', 32)
using = User.current_user
using.rate_movie(Movie.all_movies[0], 7.4)
using.rate_movie(Movie.all_movies[1], 5.9)
using.rate_movie(Movie.all_movies[2], 7.7)


# Function to display available commands and retrieve user input.

def display_commands():
    command = input('command: ')
    if command == 'info':
        print('commands: \nall (|view all movies|)\nprofile (|check your profile|)')
        print('compare (|compare similarity|)\nrate(|rate the last movie that you watch|)')
        print('add (|add movie|)\nregister (|register a user|)\n')
        print('*every movie name* (|check the movie|)')
        command = input('command: ')
    # print()
    return command


def main():
    print('Wellcome to the MovieInfo!  ')
    current_movie = None
    command = display_commands()
    while command != 'exit':
        global using
        if command == 'compare':
            print(using.similarity_scores(input('Enter a user to compare with: ')))
        elif command == 'all':
            result = '\n'.join([f'🎥|{movie.title}|🎥- {movie.average_rating:.1f}⭐' for movie in
                                sorted(Movie.all_movies, key=lambda x: x.title)])
            print(f"🔻All the movies\n{result}🔻")

        elif command == 'add':
            Movie.add_movie(input('Title: '), input('Genre: '), input('Director: '),
                            input('🔻Release data🔻'), input('Ratings-(list): '))

        elif command == 'register':
            User.register(input('Name: '), input("Age: "))
            using = User.current_user

        elif command == 'rate':
            rating = float(input('Submit your rating: '))
            print(current_movie)
            print(using.rate_movie(current_movie, rating))
            print(using.recommended())

        elif command == 'profile':
            print(using)

        else:
            current_movie = Movie.find_movie(command)
            current_movie
            print(current_movie)
        command = display_commands()


if __name__ == '__main__':
    main()
