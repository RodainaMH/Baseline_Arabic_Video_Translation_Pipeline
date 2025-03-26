def extract_sentences(filename, DG_KEY):

  # Read the audio file
  AUDIO_FILE = f'{filename}.wav'

  try:
      # Create a Deepgram client using the API key
      deepgram = DeepgramClient(DG_KEY)

      # Read audio file
      with open(AUDIO_FILE, "rb") as file:
          buffer_data = file.read()

      payload: FileSource = {
          "buffer": buffer_data,
      }

      # Configure Deepgram options for audio analysis
      options = PrerecordedOptions(
          model="nova-2",
          language="en",
          smart_format=True,
          punctuate=True,
          paragraphs=True,
      )

      # Call the transcribe_file method with the text payload and options
      response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

      # Convert response to string
      json_str = response.to_json()

      # Convert string to json
      json_file = json.loads(json_str)

      # Extract sentences info from the json file
      for idx, i in enumerate(json_file['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']):
        if idx == 0:
          sentences = i['sentences']
        else:
          sentences += i['sentences']

  except Exception as e:
      print(f"Exception: {e}")

  return sentences, sentences, json_file