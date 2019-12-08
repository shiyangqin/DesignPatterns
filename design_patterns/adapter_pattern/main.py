# -*- coding: utf-8 -*-
from adapter_pattern.media_player.AudioPlayer import AudioPlayer


if __name__ == '__main__':
    audio_player = AudioPlayer()
    audio_player.play("mp3", "audio.mp3")
    audio_player.play("mp4", "audio.mp4")
    audio_player.play("vlc", "audio.vlc")
    audio_player.play("avi", "audio.avi")