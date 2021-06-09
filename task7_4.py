class Films:
    def __init__(self, title, year, type, nr_view):
        self.title = title
        self.year = year
        self.type = type
        self.nr_view = nr_view

        # Variables
        self.nr_plays = 0

    def play(self, step=1):
        self.nr_plays += step

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
        return f'{self.title} S{self.nr_season}E{self.nr_episode}'

    def __repr__(self):
        return f"Series(title={self.title} year={self.year}, type={self.type}, nr_view={self.nr_view}, nr_episode={self.nr_episode}," \
               f"nr_season={self.nr_season})"










