def fix_audio(filename, start, end):
  # Paths
  originalPath = f"audioFiles/original/{filename}.wav"
  stretchedPath = f"audioFiles/stretched/{filename}_stretched.wav"
  fixedPath = f"audioFiles/final/{filename}_final.wav"

  # Calculations
  og_duration = round(end-start, 2)
  ar_duration = librosa.get_duration(path=originalPath)
  durations_ratio = og_duration / ar_duration

  # Stretch audio
  stretch_audio(originalPath, stretchedPath, ratio=durations_ratio)

  # Trim audio
  x_seconds = og_duration * 1000
  audio = AudioSegment.from_file(stretchedPath, format="wav")
  audio[0:x_seconds].export(fixedPath, format="wav")

def fix_all_audio(sentences_ar):
  for i in range(len(sentences_ar)):
    fix_audio(f'sentence_{i}', sentences_ar[i]['start'], sentences_ar[i]['end'])

def concatanate_audio(sentences_ar, empty_audio):
  final_audio = empty_audio
  return final_audio