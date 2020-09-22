from word_segment import load_data, segment
from LDA import LDA
from output import output

data_file = ""

data = load_data(data_file)

texts = segment(data)

patent = LDA(texts)

patent.dic_cor_generation()

patent.choose_topic()

patent.