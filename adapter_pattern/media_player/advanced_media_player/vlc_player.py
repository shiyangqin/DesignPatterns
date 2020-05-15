# -*- coding: utf-8 -*-
"""
Vlc播放器
"""
from adapter_pattern.media_player.advanced_media_player import AdvancedMediaPlayer


class VlcPlayer(AdvancedMediaPlayer):
    """Vlc播放器"""

    def play_vlc(self, file_name):
        """播放vlc"""
        print("Playing vlc file. Name: " + file_name)

    def play_mp4(self, file_name):
        """播放mp4"""
        pass
