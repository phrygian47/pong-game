from constants import *
from scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats_r = cast.get_first_actor(STATS_R_GROUP)
        stats_l = cast.get_first_actor(STATS_L_GROUP)
        self._draw_label(cast, SCORE_R_GROUP, SCORE_R_FORMAT, stats_r.get_score())
        self._draw_label(cast, SCORE_L_GROUP, SCORE_L_FORMAT, stats_l.get_score())


    def _draw_label(self, cast, group, format_str, data):
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(format_str.format(data))
        position = label.get_position()
        self._video_service.draw_text(text, position)