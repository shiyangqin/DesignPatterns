# -*- coding: utf-8 -*-
"""
媒体播放器接口
"""
from AdapterPattern.MediaPlayer.AdvancedMediaPlayer.Mp4Player import Mp4Player
from AdapterPattern.MediaPlayer.AdvancedMediaPlayer.VlcPlayer import VlcPlayer

class MediaPlayer(object):
    """
    媒体播放器接口
    """

    def play(self, audioType, fileName):
        """播放mp3"""
        pass


class MediaAdapter(MediaPlayer):
    """
    适配器
    """

    def __init__(self):
        self._vlcPlayer = VlcPlayer()
        self._mp4Player = Mp4Player()

    def play(self, audioType, fileName):
        """播放mp3"""
        if audioType.lower() == 'vlc':
            self._vlcPlayer.playVlc(fileName)
        elif audioType.lower() == 'mp4':
            self._mp4Player.playMp4(fileName)
