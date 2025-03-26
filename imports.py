# General use
import os

# Voice extraction imports
from pydub import AudioSegment

# Text extraction imports
import json
from deepgram import DeepgramClient, PrerecordedOptions, FileSource

# Translation imports
from transformers import MarianTokenizer, MarianMTModel, pipeline
import time

# Text to speech imports
import torch
from TTS.api import TTS
import soundfile as sf
import pyrubberband as pyrb
import librosa
from audiostretchy.stretch import stretch_audio

# Lip sync imports
from tqdm import tqdm
from IPython.display import HTML, clear_output
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import locale
locale.getpreferredencoding = lambda: "UTF-8"