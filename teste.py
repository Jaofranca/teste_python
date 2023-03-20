import string

file = open("lorem.txt", "r")
text = file.read()
lowerText = text.lower()
text_without_punctuation = lowerText.translate(str.maketrans('', '', string.punctuation))
words_dict = {}

for word in text_without_punctuation.split():
  values = words_dict.values()
  if word in words_dict:
    words_dict[word] += 1
  else:
    words_dict.update({word: 1})
print(words_dict)
