from constants import *
from casting.sound import Sound
from scripting.action import Action
from casting.point import Point
from casting.body import Body
from casting.image import Image
from casting.ball import Ball
import time

class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
        score_sound = Sound(SCORE_SOUND)
                
        if x < (FIELD_LEFT):
            # If the ball hits the left side of the screen, update points and reset ball position.
            self._audio_service.play_sound(score_sound)
            stats_l = cast.get_first_actor(STATS_L_GROUP)
            stats_l.add_points(1)
            # Conditional to check if the player has won.
            if stats_l.get_score() == 2:
                # Change scene to game over screen
                callback.on_next(GAME_OVER)
                # Play game over sound
                self._audio_service.play_sound(over_sound) 
            # Clear the ball and reset its position.
            cast.clear_actors(BALL_GROUP)
            x = CENTER_X - BALL_WIDTH / 2
            y = CENTER_Y
            position = Point(x, y)
            size = Point(BALL_WIDTH, BALL_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(BALL_IMAGE)
            ball = Ball(body, image, True)
            cast.add_actor(BALL_GROUP, ball)
            # Delay to allow time to prepare
            time.sleep(1)
            ball.release()
        
        # Game logic for if the ball hits the right side of the screen.
        if  x > (FIELD_RIGHT-BALL_WIDTH):
            self._audio_service.play_sound(score_sound)
            stats_r = cast.get_first_actor(STATS_R_GROUP)
            stats_r.add_points(1)
            
            #Conditional check if this player has won the game.
            if stats_r.get_score() == 2:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound) 

            # Clear ball and reset position.
            cast.clear_actors(BALL_GROUP)
            x = CENTER_X - BALL_WIDTH / 2
            y = CENTER_Y
            position = Point(x, y)
            size = Point(BALL_WIDTH, BALL_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(BALL_IMAGE)
            ball = Ball(body, image, True)
            cast.add_actor(BALL_GROUP, ball)
            time.sleep(1)
            ball.release()
            
        # If the ball hits the top or bottom, invert y velocity.
        if y <= FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
            
        if y >= (FIELD_BOTTOM-(BALL_WIDTH+20)):
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)
        