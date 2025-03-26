# Arabic Video Translation Pipeline

## Overview
This repository contains the code and methodology for an AI-powered Arabic video translation pipeline, incorporating speech-to-text, machine translation, text-to-speech, and lip-syncing. This system enables real-time Arabic video dubbing with high-quality lip synchronization and natural voice cloning.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Results](#results)

## Features
- **Speech-to-Text**: Converts Arabic speech to text with high accuracy.
- **Machine Translation**: Translates Arabic text into the target language.
- **Text-to-Speech**: Generates natural-sounding speech from translated text.
- **Lip-Syncing**: Aligns lip movements with the generated speech for realistic dubbing.


##Usage
Run the pipeline using the following command:
python main.py --input video.mp4 --language en
This command takes an Arabic video (video.mp4), processes it, and generates an English-dubbed version with synchronized lip movements.

## Evaluation
We assess the pipeline's performance using industry-standard metrics:
-Word Error Rate (WER): Measures the accuracy of speech-to-text conversion.
-BLEU Score: Evaluates machine translation quality.
-Lip-Sync Accuracy: Assesses how well the generated speech matches lip movements.



## Installation
To install dependencies, run:
```sh
pip install -r requirements.txt


