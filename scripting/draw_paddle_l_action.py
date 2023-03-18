from constants import *
from scripting.action import Action


class DrawPaddleLAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        paddle_l = cast.get_first_actor(PADDLE_L_GROUP)
        body = paddle_l.get_body()

        if paddle_l.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = paddle_l.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)