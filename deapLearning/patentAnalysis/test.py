from word_segment import load_data, segment

datafile = './patent.json'

data = load_data(datafile)

text = segment(data)

print(text)
