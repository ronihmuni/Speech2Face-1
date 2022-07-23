# This class is responsible to get a filename of a wav file,
# and return a tensor compatible for the network
import tensorflow as tf
import librosa

# Consts
DURATION = 6 # The network is trained on 6 seconds audios
SAMPLE_RATE = 16000

class SpectrogramLoader():
    def __init__(self, filename):
        self.filename = filename

    def getTensor(self):
        #raw_audio = tf.io.read_file(self.filename)
        #waveform = tf.audio.decode_wav(raw_audio)
        #return waveform

        test = librosa.load(self.filename)
        
