from constants import *
from scripting.action import Action


class ControlPaddleLAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        paddle_l = cast.get_first_actor(PADDLE_L_GROUP)
        if self._keyboard_service.is_key_down(P1_DOWN): 
            paddle_l.swing_up()
        elif self._keyboard_service.is_key_down(P1_UP): 
            paddle_l.swing_down()  
        else: 
            paddle_l.stop_moving()        