# -*- coding: utf-8 -*-
"""
Vlc播放器
"""
from AdapterPattern.MediaPlayer.AdvancedMediaPlayer import AdvancedMediaPlayer


class VlcPlayer(AdvancedMediaPlayer):
    """Vlc播放器"""

    def playVlc(self, fileName):
        """播放vlc"""
        print("Playing vlc file. Name: "+ fileName)

    def playMp4(self, fileName):
        """播放mp4"""
        pass
