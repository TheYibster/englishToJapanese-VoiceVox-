# English Voice to Japanese Voice
Using the Whisper AI, DeepL, and VoiceVox API's to create a transcribe/translate/transpose machine from English language to Japanese language perfect for all weebs.

Credits to [@sociallyinephtweeb](https://www.youtube.com/@sociallyineptweeb) for the idea.

Docker Hubs for Whisper and VoiceVox:

[VoiceVox](https://hub.docker.com/r/voicevox/voicevox_engine)

[Whisper](https://hub.docker.com/r/onerahmet/openai-whisper-asr-webservice)

# Usage:
This is where it's different from the video. @sociallyinephtweeb used a similar program for Apex Legends' in-game voice chat. I wanted to generalize the voicechanger to all forms of media.

You will need a virtual audio cable to run it into your computer's audio. I used this [one](https://vb-audio.com/Cable/) here.

Then you will need to adjust the output index for PyAudio to match the virtual audio cable.

Now you are ready to become the anime.

By Default: 'r' is to record a phrase in English and 's' is to stop and play the recorded phrase in Japanese.