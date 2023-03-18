from constants import *
from casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points
  
    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0