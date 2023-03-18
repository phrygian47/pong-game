from constants import *
from scripting.action import Action


class ControlPaddleRAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        paddle_r = cast.get_first_actor(PADDLE_R_GROUP)
        if self._keyboard_service.is_key_down(P2_DOWN): 
            paddle_r.swing_up()
        elif self._keyboard_service.is_key_down(P2_UP): 
            paddle_r.swing_down()  
        else: 
            paddle_r.stop_moving()        