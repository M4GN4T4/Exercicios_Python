from pydub import AudioSegment
import simpleaudio as sa

# Carregar o arquivo de áudio MP4
audio_file = "C:/Users/jerds/ProjetosVscode/Guanabara_Exercícios/ex21/Saramusic.mp4"
audio = AudioSegment.from_file(audio_file, format="mp4")

# Converter o áudio para WAV (ou outro formato compatível)
wav_audio = audio.export("converted_audio.wav", format="wav")

# Reproduzir o áudio usando a biblioteca simpleaudio
wave_obj = sa.WaveObject.from_wave_file("converted_audio.wav")
play_obj = wave_obj.play()

# Esperar até que a reprodução termine
play_obj.wait_done()