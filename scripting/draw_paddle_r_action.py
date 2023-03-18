from constants import *
from scripting.action import Action


class DrawPaddleRAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        paddle_r = cast.get_first_actor(PADDLE_R_GROUP)
        body = paddle_r.get_body()

        if paddle_r.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = paddle_r.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)