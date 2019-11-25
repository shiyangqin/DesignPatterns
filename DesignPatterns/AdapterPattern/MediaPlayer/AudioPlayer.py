# -*- coding: utf-8 -*-
"""
音频播放器
"""
from AdapterPattern.MediaPlayer import MediaPlayer, MediaAdapter


class AudioPlayer(MediaPlayer):
    """音频播放器"""
    def __init__(self):
        self._mediaAdapter = MediaAdapter()

    def play(self, audioType, fileName):
        """播放"""
        if audioType.lower() == 'mp3':
            print("Playing mp3 file. Name: "+ fileName)
        elif audioType.lower() in ['vlc', 'mp4']:
            self._mediaAdapter.play(audioType, fileName)
        else:
            print("Invalid media. " + audioType + " format not supported")
