from faker import Faker
fake = Faker()


class Films:
    def __init__(self, title, year, type):
        self.title = title
        self.year = year
        self.type = type

        # Variables
        self.nr_view = 0

    def play(self, step=1):
        self.nr_view += step

    def __str__(self):
        return f'{self.title} {self.year}'

    def __repr__(self):
        return f"Films(title={self.title} year={self.year}, type={self.type}, view={self.nr_view})"


class Series(Films):
    def __init__(self, nr_episode, nr_season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nr_episode = nr_episode
        self.nr_season = nr_season

    def __str__(self):
        return f'{self.title} S{self.nr_season:02}E{self.nr_episode:02}'

    def __repr__(self):
        return f"Series(title={self.title} year={self.year}, type={self.type}, nr_view={self.nr_view}, nr_episode={self.nr_episode}," \
               f"nr_season={self.nr_season})"

films_list =[]


for x in range(10):
    film = Films(title=fake.word(), year=fake.year(), type=fake.word())
    films_list.append(film)
    serie = Series(title=fake.word(), year=fake.year(), type=fake.word(),
                   nr_season=fake.random_digit(), nr_episode=fake.random_int(0,20))
    films_list.append(serie)




def get_movies():
    for x in range(0, 19):
        if isinstance(films_list[19-x], Series) == True:
            del films_list[19-x]

def get_series():
    for x in range(0, 19):
        if isinstance(films_list[19-x], Series) == False:
            del films_list[19-x]

def search(x):
    for y in range(len(films_list)):
        if films_list[y].title == x:
            print(x)

print(films_list)























