import json
from tqdm import tqdm
import nltk


def load_data(file_path):
    """
    @description: load raw data from original file
    @param: data file address
    @return: raw data
    """
    with open(file_path) as file:
        data = file.read()
    data = json.loads(data)
    return data


def segment(data):
    """
    @description: segment the text into words
    @param: raw data in the format of [a1,a2,a3,...]
    @return: segmented data, [['xx','xx'],['xx','xx'],...,['xx','xx']]
    """
    jp_char_type_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')
    text = []
    with open('./stopwords-ja.txt') as file:
        stop_word_list = file.read()
    for item in tqdm(data):
        tmp = jp_char_type_tokenizer.tokenize(item['weibo_cont'])
        for i in tmp:
            if i in stop_word_list:
                tmp.remove(i)
        text.append(tmp)
    return text
