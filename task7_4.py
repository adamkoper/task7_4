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


class Series(Films):
    def __init__(self, nr_episode, nr_season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nr_episode = nr_episode
        self.nr_season = nr_season








