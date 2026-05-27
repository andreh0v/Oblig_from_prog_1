class movie:
    def __init__(self, tittel, aar, rating):
        self.tittel = tittel
        self.aar = aar
        self.rating = rating
    def describe(self):
        print(f"{self.tittel}, ({self.aar}), - Rating: {self.rating}")
    def info(self):
        return f"{self.tittel} was released in {self.aar} with a current score of {self.rating}"

movie1 = movie("Inception", 2010, 8.8)
movie2 = movie("The martian", 2015, 8.0)
movie3 = movie("Joker", 2019, 8.4)
movie4 = movie("Interstellar", 2014, 8.6)


all_movies = [movie1, movie2, movie3, movie4]
for m in all_movies:
    print(m.info())
