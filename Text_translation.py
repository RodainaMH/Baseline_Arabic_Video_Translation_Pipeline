def marianbig(input):
  pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-ar")
  translation = pipe(">>ara<< " + input)[0]['translation_text']
  return translation

def marian (input):
  mname = "marefa-nlp/marefa-mt-en-ar"
  tokenizer = MarianTokenizer.from_pretrained(mname)
  model = MarianMTModel.from_pretrained(mname)
  translated_tokens = model.generate(**tokenizer.prepare_seq2seq_batch([input], return_tensors="pt"))
  translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated_tokens]
  return translated_text[0]
def translate_text(sentences_ar):

  for i in range(len(sentences_ar)):
    text = sentences_ar[i]['text']
    translation = marianbig(text)
    sentences_ar[i]['text'] = translation

  return sentences_ar