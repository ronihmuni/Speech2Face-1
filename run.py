from spectrogram_loader import SpectrogramLoader

def main():
	sl = SpectrogramLoader("roni.wav")
	spec = sl.getTensor()
	print(spec)


if __name__ == "__main__":
	main()