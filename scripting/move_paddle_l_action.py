from constants import *
from casting.point import Point
from scripting.action import Action


class MovePaddleLAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        paddle_l = cast.get_first_actor(PADDLE_L_GROUP)
        body = paddle_l.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        y = position.get_y()
        
        position = position.add(velocity)

        if y <= FIELD_TOP:
            position = Point(position.get_x(), FIELD_TOP)
        elif y >= (SCREEN_HEIGHT - PADDLE_HEIGHT):
            position = Point(position.get_x(),SCREEN_HEIGHT - PADDLE_HEIGHT)

        position = position.add(velocity)  
        body.set_position(position)
        
        