from pytube import YouTube
from pydub import AudioSegment


# # assign files
# input_file = "hello.mp3"
# output_file = "result.wav"
#
# # convert mp3 file to wav file
# sound = AudioSegment.from_mp3(input_file)
# sound.export(output_file, format="wav")
#

def install(url: str):
    yt = YouTube(url)
    yt = yt.streams.get_audio_only()
    audio = yt.download()
    print('Video downloaded')
    return audio


def convert(file):
    audio = AudioSegment.from_file(file, format="mp4")
    audio.export("output_file.wav", format="wav")
    print('video converted')
