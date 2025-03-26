#create_directories()
filename = 'ML'
DG_KEY = '90a4afc2746af03f2ecc430c482dee41f76e4c31'
extract_voice(filename)
sentences_en, sentences_ar, json_file = extract_sentences(filename, DG_KEY)

translate_text(sentences_ar)
create_directories()
text_to_speech(filename, sentences_ar)
fix_all_audio(sentences_ar)
def concatinate_audio(sentences_ar):
  emptyAudio = AudioSegment.from_file('empty.wav', format="wav")
  audios = []
  for i in range(len(sentences_ar)):
    audios.append(AudioSegment.from_file(f'/content/audioFiles/final/sentence_{i}_final.wav', format="wav"))

  for i in range(len(sentences_ar)-1):
    combined = emptyAudio
    empty_duration = sentences_ar[i+1]['start'] - sentences_ar[i]['end']
    for j in range(int(empty_duration*100)-1):
      combined = combined + emptyAudio

    combined.export("combined.wav", format="wav")
    if i == 0:
      finalAudio = audios[0]
    if empty_duration > 0:
      finalAudio = finalAudio + combined + audios[i+1]
    else:
      finalAudio = finalAudio + audios[i+1]

  finalAudio.export("finalAudio.wav", format="wav")
  librosa.get_duration(path="finalAudio.wav")



concatinate_audio(sentences_ar)
%%capture --no-display
!pip install noisereduce
!pip install speechbrain

import IPython
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import io
from IPython.display import Audio
%matplotlib inline

from speechbrain.inference.separation import SepformerSeparation as separator
import torchaudio

model = separator.from_hparams(source="speechbrain/sepformer-wham-enhancement", savedir='pretrained_models/sepformer-wham-enhancement')

#torchaudio.save("/content/speechbrain/sepformer-wham-enhancement/example_wham.wav")

est_sources = model.separate_file(path='speechbrain/sepformer-wham-enhancement/example_wham.wav')

torchaudio.save("/content/enhanced_wham.wav", est_sources[:, :, 0].detach().cpu(), 8000)

lip_sync('finalAudio.wav', f'{filename}.mp4', 'ML_output')
