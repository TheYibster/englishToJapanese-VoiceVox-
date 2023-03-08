import requests
import urllib
import winsound
import pyaudio
import wave
from decouple import config

def speak(sentence):
    base_url = 'http://127.0.0.1:50021'
    audio_filepath = 'audio.wav'
    speaker_id = '1'
    params_encoded = urllib.parse.urlencode({'text': sentence, 'speaker': speaker_id})
    r = requests.post(f'{base_url}/audio_query?{params_encoded}')
    voicevox_query = r.json()
    voicevox_query['volumeScale'] = 2.0
    voicevox_query['intonationScale'] = 1.5
    voicevox_query['prePhonemeLength'] = 1.0
    voicevox_query['postPhenoemeLength'] = 1.0

    params_encoded = urllib.parse.urlencode({'speaker': speaker_id})
    r = requests.post(f'{base_url}/synthesis?{params_encoded}', json=voicevox_query)

    with open(audio_filepath, 'wb') as outfile:
        outfile.write(r.content)

    winsound.PlaySound(audio_filepath, winsound.SND_FILENAME)

def translate(phrase):
    auth_key = config('AUTH_KEY')

    result = requests.get(
        'https://api-free.deepl.com/v2/translate',
        params={
            "auth_key":auth_key,
            "target_lang": "JA",
            "text": phrase
        }
    )

    text = result.json()["translations"][0]["text"]

    return text

def transcribe(WAV_FILE):
        API_ENDPOINT = 'http://127.0.0.1:9000/asr?task=transcribe&language=en&output=json'

        # read the contents of the WAV file as binary data
        with open(WAV_FILE, 'rb') as f:
            files = {'audio_file': f} 
            response = requests.post(API_ENDPOINT, files=files)

        if response.status_code == 200:
            print('Transcription successful')
        else:
            print('Error')
        
        return response.json()['text']


def play_through_mic():
    with wave.open('./audio.wav', 'rb') as wf:
        # create PyAudio stream
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        output_device_index=5)

        data = wf.readframes(48000)
        while data:
            stream.write(data)
            data = wf.readframes(48000)


        # clean up resources
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf.close()
