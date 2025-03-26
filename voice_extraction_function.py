def extract_voice(filename):
  # Load mp4 file
  audio = AudioSegment.from_file(f'{filename}.mp4', format="mp4")
  # Export as wav
  audio.export(f'{filename}.wav', format="wav")