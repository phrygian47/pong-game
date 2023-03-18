from constants import *
from casting.sound import Sound
from scripting.action import Action
from casting.image import Image


class CollidePaddleAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        paddle_r = cast.get_first_actor(PADDLE_R_GROUP)
        paddle_l = cast.get_first_actor(PADDLE_L_GROUP)
        
        ball_body = ball.get_body()
        paddle_r_body = paddle_r.get_body()
        paddle_l_body = paddle_l.get_body()

        if self._physics_service.has_collided(ball_body, paddle_r_body):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            paddle_r.set_image(Image(f"{PADDLE_COLOR_R[randint(0, 4)]}"))
        if self._physics_service.has_collided(ball_body, paddle_l_body):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            paddle_l.set_image(Image(f"{PADDLE_COLOR_L[randint(0, 4)]}"))
        if self._physics_service.is_above(paddle_r_body, ball_body) or self._physics_service.is_above(paddle_l_body, ball_body):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
        if self._physics_service.is_below(paddle_r_body, ball_body) or self._physics_service.is_below(paddle_l_body, ball_body):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)