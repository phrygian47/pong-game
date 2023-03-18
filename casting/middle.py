from constants import *
from casting.actor import Actor
from casting.point import Point

class Middle(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_image(self):
        """Gets the paddle's image
        
        Returns:
            and instance of Image
        """
        return self._image

    def get_body(self):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body