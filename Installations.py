! pip install deepgram-sdk
! pip install requests ffmpeg-python
! pip install pydub
! pip install transformers
! pip install sacremoses
! pip install datasets
! pip install TTS
! pip install soundfile
! pip install AudioSegment
! pip install audiostretchy
! pip install pyrubberband
!pip install --upgrade numpy
!pip install --upgrade transformers
------------------------------------------------
!pip install --upgrade transformers
------------------------------------------------
!git clone https://github.com/justinjohn0306/Wav2Lip
%cd /content/Wav2Lip

!wget 'https://github.com/justinjohn0306/Wav2Lip/releases/download/models/wav2lip.pth' -O 'checkpoints/wav2lip.pth'
!wget 'https://github.com/justinjohn0306/Wav2Lip/releases/download/models/wav2lip_gan.pth' -O 'checkpoints/wav2lip_gan.pth'
!wget 'https://github.com/justinjohn0306/Wav2Lip/releases/download/models/resnet50.pth' -O 'checkpoints/resnet50.pth'
!wget 'https://github.com/justinjohn0306/Wav2Lip/releases/download/models/mobilenet.pth' -O 'checkpoints/mobilenet.pth'
a = !pip install https://raw.githubusercontent.com/AwaleSajil/ghc/master/ghc-1.0-py3-none-any.whl
!pip install git+https://github.com/elliottzheng/batch-face.git@master
%cd ..