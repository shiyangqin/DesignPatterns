# -*- coding: utf-8 -*-
from adapter_pattern.media_player.advanced_media_player.mp4_player import Mp4Player
from adapter_pattern.media_player.advanced_media_player.vlc_player import VlcPlayer


class MediaPlayer(object):
    """媒体播放器接口"""
    def play(self, audio_type, file_name):
        """播放mp3"""
        pass


class MediaAdapter(MediaPlayer):
    """适配器"""

    def __init__(self):
        self._vlc_player = VlcPlayer()
        self._mp4_player = Mp4Player()

    def play(self, audio_type, file_name):
        """播放mp3"""
        if audio_type.lower() == 'vlc':
            self._vlc_player.play_vlc(file_name)
        elif audio_type.lower() == 'mp4':
            self._mp4_player.play_mp4(file_name)
