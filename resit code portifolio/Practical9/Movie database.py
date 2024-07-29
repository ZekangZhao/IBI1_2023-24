class Movie:
    def __init__(self, title, runtime, year_released, genre):
        self.title = title
        self.runtime = runtime
        self.year_released = year_released
        self.genre = genre
    
    def print_details(self):
        print(f"{self.title}, {self.runtime} minutes, {self.year_released}, {self.genre}")

# Example of using this class
godfather = Movie("The Godfather", 175, 1972, "Crime")
shawshank = Movie("The Shawshank Redemption", 142, 1994, "Drama")
godfather.print_details()
shawshank.print_details()
