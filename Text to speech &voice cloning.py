# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# def create_directories(): # error if it already exists
#   os.mkdir('audioFiles')
#   os.mkdir('audioFiles/original')
#   os.mkdir('audioFiles/stretched')
#   os.mkdir('audioFiles/final')

def empty_directory(directory):
  if os.path.exists(directory):
    for filename in os.listdir(directory):
      filepath = os.path.join(directory, filename)
      try:
        if os.path.isfile(filepath):
          os.remove(filepath)
      except Exception as e:
        print(f"Failed to delete {filepath}. Reason: {e}")

def create_directories():
  directories = ['audioFiles', 'audioFiles/original', 'audioFiles/stretched', 'audioFiles/final']

  for directory in directories:
    if not os.path.exists(directory):  # Check if directory does not exist
      os.mkdir(directory)  # Create the directory if it does not exist
    else:
      empty_directory(directory)  # If directory exists, empty it out




def text_to_speech(filename, sentences_ar, dir = 'audioFiles/original/'):
  for i in range(len(sentences_ar)):
    tts.tts_to_file(
      text = sentences_ar[i]['text'],
      speaker_wav=f'{filename}.wav',
      language="ar",
      file_path=f"{dir}sentence_{i}.wav")