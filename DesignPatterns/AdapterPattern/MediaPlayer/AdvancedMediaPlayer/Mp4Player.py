# -*- coding: utf-8 -*-
"""
Mp4播放器
"""
from AdapterPattern.MediaPlayer.AdvancedMediaPlayer import AdvancedMediaPlayer


class Mp4Player(AdvancedMediaPlayer):
    """Mp4播放器"""

    def playVlc(self, fileName):
        """播放vlc"""
        pass

    def playMp4(self, fileName):
        """播放mp4"""
        print("Playing mp4 file. Name: "+ fileName)
