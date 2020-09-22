from gensim import corpora, models
import matplotlib as plt
import pyLDAvis


class LDA:
    def __init__(self, articles):
        self.data = articles

    def dic_cor_generation(self):
        """
        @description: generate dictionary and corpus in LDA
        @return: dictionary {index : word} and corpus {index : frequency of word}
        """
        text = self.data
        dictionary = corpora.Dictionary(text)
        corpus = [dictionary.doc2bow(tmp) for tmp in text]
        return dictionary, corpus

    def choose_topic(self):
        """
        @description: define the numbers of the topics
        @return:
        """
        dictionary, corpus = self.dic_cor_generation()
        texts = self.data
        for i in range(1, 3):
            print('number of topics: {}'.format(i))
            print('data size:{}'.format(len(texts)))
            temp = 'lda_{}_{}'.format(i, len(texts))
            tmp = models.ldamodel.LdaModel(corpus, num_topics=i, id2word=dictionary, passes=20)
            file_path = './{}.model'.format(temp)
            tmp.save(file_path)
            print('------------------')

    def perplexity_model(self, topic_num, data_num):
        """
        @description: 绘制困惑度-主题数目曲线
        @param {type}
        @return:
        """
        _, corpus = self.dic_cor_generation()
        x_list = []
        y_list = []
        for i in range(1, topic_num):
            model_name = './lda_{}_{}.model'.format(i, data_num)
            try:
                lda = models.ldamodel.LdaModel.load(model_name)
                perplexity = lda.log_perplexity(corpus)
                print(perplexity)
                x_list.append(i)
                y_list.append(perplexity)
            except Exception as e:
                print(e)
        plt.plot(x_list, y_list)
        plt.xlabel('num topics')
        plt.ylabel('perplexity score')
        plt.legend('perplexity_values', loc='best')
        plt.show()

    def coherence_model(self, topic_num, data_num):
        """
        @description: 可视化模型
        @param :topic_num:主题的数量
        @param :data_num:数据的量
        @return: 可视化lda模型
        """
        dictionary, _ = self.dic_cor_generation()
        texts = self.data
        x_list = []
        y_list = []
        for i in range(1, topic_num):
            model_name = './lda_{}_{}.model'.format(i, data_num)
            try:
                lda = models.ldamodel.LdaModel.load(model_name)
                cv_tmp = models.CoherenceModel(model=lda, texts=texts, dictionary=dictionary, coherence='c_v')
                x_list.append(i)
                y_list.append(cv_tmp.get_coherence())
            except:
                print('没有这个模型:{}'.format(model_name))
        plt.plot(x_list, y_list)
        plt.xlabel('num topics')
        plt.ylabel('coherence score')
        plt.legend('coherence_values', loc='best')
        plt.show()

    def visualize(self, topic_num, data_num):
        """
        @description: 可视化模型
        @param {type}
        @return:
        """
        dictionary, corpus = self.dic_cor_generation()
        model_name = './lda_{}_{}.model'.format(topic_num, data_num)
        lda = models.ldamodel.LdaModel.load(model_name)
        vis_data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
        pyLDAvis.show(vis_data, open_browser=False)
