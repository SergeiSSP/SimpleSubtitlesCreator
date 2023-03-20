import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

from utils import convert, install


r = sr.Recognizer()


def transcribe_large_audio(path):
    """Split audio into chunks and apply speech recognition"""
    sound = AudioSegment.from_wav(path)
    chunks = split_on_silence(
        sound,
        min_silence_len=700,
        silence_thresh=sound.dBFS - 14,
        keep_silence=700
    )
    p = enumerate(chunks)
    # Create folder to store audio chunks
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    with open('result.txt', 'w+') as dst:
        whole_text = ""
        # Process each chunk
        for i, audio_chunk in enumerate(chunks, start=1):
            # Export chunk and save in folder
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # Recognize chunk
            with sr.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                # Convert to text
                try:
                    text = r.recognize_google(audio_listened, language='zh-CN')
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()}. "
                    print(chunk_filename, ":", text)
                    dst.write(text + '\n')

    print('Finito')


if __name__ == '__main__':
    url = input('Enter url of video...')
    a = install(url)
    audio = convert(a)
    transcribe_large_audio('output_file.wav')

