"""Lab2:  Movie Library Create a class MovieLibrary that manages a collection of movies: 

 1. Class Attribute: ○ available_movies: A list of all movies available in the library.

 2. Instance Attributes: ○ member_name: The name of the library member. ○ borrowed_movies: A list of movies borrowed by the member. 

3. Methods: ○ borrow_movie(self, movie): Borrows a movie from the library if available. 

 ○ return_movie(self, movie): Returns a movie to the library.

 ○ view_borrowed_movies(self): Prints a list of movies borrowed by the member"""

class MovieLibrary:
    # Class attribute
    available_movies = []

    def __init__(self, member_name):
        # Instance attributes
        self.member_name = member_name
        self.borrowed_movies = []

    def borrow_movie(self, movie):
        """Borrows a movie from the library if available."""
        if movie in MovieLibrary.available_movies:
            self.borrowed_movies.append(movie)
            MovieLibrary.available_movies.remove(movie)
            print(f"{self.member_name} successfully borrowed '{movie}'")
        else:
            print(f"'{movie}' is not available in the library.")

    def return_movie(self, movie):
        """Returns a borrowed movie to the library."""
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            MovieLibrary.available_movies.append(movie)
            print(f"{self.member_name} successfully returned '{movie}'")
        else:
            print(f"{self.member_name} hasn't borrowed '{movie}'")

    def view_borrowed_movies(self):
        """Displays the list of borrowed movies by the member."""
        if self.borrowed_movies:
            print(f"{self.member_name} has borrowed the following movies:")
            for movie in self.borrowed_movies:
                print(f"- {movie}")
        else:
            print(f"{self.member_name} has not borrowed any movies.")


# Example usage

# Initializing the movie library with available movies
MovieLibrary.available_movies = ['Inception', 'Titanic', 'The Matrix', 'Interstellar', 'Avatar']

# Creating members of the library
member1 = MovieLibrary("Alice")
member2 = MovieLibrary("Bob")

# Borrowing and returning movies
member1.borrow_movie('Inception')
member2.borrow_movie('Avatar')
member1.borrow_movie('The Matrix')

# Viewing borrowed movies
member1.view_borrowed_movies()
member2.view_borrowed_movies()

# Returning movies
member1.return_movie('Inception')
member2.return_movie('The Matrix')  # Bob didn't borrow 'The Matrix'

# Viewing borrowed movies after returns
member1.view_borrowed_movies()
member2.view_borrowed_movies()

# Viewing available movies in the library after actions
print("\nMovies available in the library:")
for movie in MovieLibrary.available_movies:
    print(f"- {movie}")
