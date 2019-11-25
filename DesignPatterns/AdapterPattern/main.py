# -*- coding: utf-8 -*-
from AdapterPattern.MediaPlayer.AudioPlayer import AudioPlayer


if __name__ == '__main__':
    audioPlayer = AudioPlayer()
    audioPlayer.play("mp3", "audio.mp3")
    audioPlayer.play("mp4", "audio.mp4")
    audioPlayer.play("vlc", "audio.vlc")
    audioPlayer.play("avi", "audio.avi")