# This class is responsible to get a filename of a wav file,
# and return a tensor compatible for the network
import tensorflow as tf

class SpectrogramLoader():
    def __init__(self, filename):
        self.filename = filename

    def getTensor(self):
        raw_audio = tf.io.read_file(self.filename)
        waveform = tf.audio.decode_wav(raw_audio)
