
from transformers import pipeline
from moviepy.editor import VideoFileClip
import os

# create directory to store audio files called '/audio_files'
audio_directory = '/audio_files'
if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)

# create pipeline
pipe = pipeline(model="openai/whisper-base", device_map="auto")


# extract audio from video
def extract_audio(mp4_file, output_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(output_file)


def processor(todos):
    for video_file in todos.file_paths_to_process:

        # video name
        video_name = video_file.split('/')[-1].split('.')[0]

        # Save the audio clip as an MP3 file
        audio_file = audio_directory + '/' + video_name + '.mp3'

        # extract audio from video
        extract_audio(video_file, audio_file)

        # process audio
        output = pipe(audio_file, chunk_length_s=30)
        print(output, flush=True)

        # write to output
        with open(todos.path_to_output + '/' +
                  video_file.split('/')[-1].split('.')[0] + '.txt', 'w') as f:
            f.write(output['text'])
