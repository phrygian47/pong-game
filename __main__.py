from constants import *
from directing.director import Director
from directing.scene_manager import SceneManager


def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()