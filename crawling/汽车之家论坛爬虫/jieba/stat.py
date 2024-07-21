#encoding=utf-8
# author = evan

import jieba
import jieba.analyse

def cut(fpath, w_path):
    wf = open(w_path, 'w+', encoding = 'utf-8')
    r = open(fpath, encoding = 'utf-8')
    for line in r:
        #item = line.strip('\n\r').split('\t')  # 制表格切分
        tags = jieba.analyse.extract_tags(line)  # jieba分词
        tagsw = ",".join(tags)  # 逗号连接切分的词
        wf.write(tagsw)
    wf.close()
    r.close()

def stat(w_path, r_path):
    word_lst = []
    word_dict = {}
    with open(w_path, encoding = 'utf-8') as wf, open(r_path, "w+", encoding = 'utf-8') as wf2:
        for word in wf:
            word_lst.append(word.split(',')) #使用逗号进行切分
            for item in word_lst:
                for item2 in item:
                    if item2 not in word_dict: #统计数量
                        word_dict[item2] = 1
                    else:
                        word_dict[item2] += 1
        sorted_key_list = sorted(word_dict, key=lambda x: word_dict[x], reverse=True)
        sorted_dict = map(lambda x: {x: word_dict[x]}, sorted_key_list)
        for d in sorted_dict:
            wf2.write(str(d.items()) + '\n' ) #写入文档





def main():
    fpath = 'ConMJ.txt'
    w_path = 'conMJ-w.txt'
    r_path = 'conMJ-r.txt'
    cut(fpath, w_path)
    stat(w_path, r_path)

main()