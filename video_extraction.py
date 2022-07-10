import speech_recognition as sr 
import moviepy.editor as mp

# Help: https://towardsdatascience.com/extracting-speech-from-video-using-python-f0ec7e312d38

# Convert Video to audio format
def vid_to_audio(vid_recording, wave_file):
    '''
    Convert video to Wave format.
    Converted Name should be .wav
    '''
    clip = mp.VideoFileClip(vid_recording) #r”video_recording.mov”
    clip.audio.write_audiofile(wave_file)
    return wave_file

def speech_recognizer(wave_file):
    r = sr.Recognizer()
    audio = sr.AudioFile(wave_file)
    with audio as source:
        audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    return result

# Might need to change this function.
def export_to_txt(result):
    with open('recognized.txt',mode ='w') as file: 
        file.write("Recognized Speech:") 
        file.write("\n") 
        file.write(result) 
        print("ready!")
    # return 'recognized.txt'