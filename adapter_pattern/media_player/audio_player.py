# -*- coding: utf-8 -*-
from adapter_pattern.media_player import MediaPlayer, MediaAdapter


class AudioPlayer(MediaPlayer):
    """音频播放器"""
    def __init__(self):
        self._media_adapter = MediaAdapter()

    def play(self, audio_type, file_name):
        """播放"""
        if audio_type.lower() == 'mp3':
            print("Playing mp3 file. Name: " + file_name)
        elif audio_type.lower() in ['vlc', 'mp4']:
            self._media_adapter.play(audio_type, file_name)
        else:
            print("Invalid media. " + audio_type + " format not supported")
