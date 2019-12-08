# -*- coding: utf-8 -*-
"""
Mp4播放器
"""
from adapter_pattern.media_player.advanced_media_player import AdvancedMediaPlayer


class Mp4Player(AdvancedMediaPlayer):
    """Mp4播放器"""

    def play_vlc(self, file_name):
        """播放vlc"""
        pass

    def play_mp4(self, file_name):
        """播放mp4"""
        print("Playing mp4 file. Name: " + file_name)
