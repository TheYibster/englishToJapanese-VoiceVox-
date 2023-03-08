import pyaudio
import wave
import keyboard
import requests
from apimethods import translate, transcribe, speak, play_through_mic

# variable to keep track of whether we are recording
is_recording = False

transcribe_path = "./output.wav"
# function to start recording
def start_recording():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "output.wav"

    # initialize PyAudio
    audio = pyaudio.PyAudio()

    # open microphone stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    
    global is_recording
    if not is_recording:
        is_recording = True
        # start recording
        frames = []
        while is_recording:
            data = stream.read(CHUNK)
            frames.append(data)
            if keyboard.is_pressed('s'):
                is_recording = False

        # stop recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # save the recorded data as a WAV file
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        en_text = transcribe(transcribe_path)
        if en_text:
            JP_text = translate(en_text)
            speak(JP_text)
            play_through_mic()
        else:
            raise Exception


# start recording when the "r" key is pressed
keyboard.add_hotkey('r', start_recording)

# wait for hotkeys
keyboard.wait()