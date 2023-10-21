import math


class TfIdfTransformer():
    """
    Class for calculating tf-idf metric for matrix of frequencies (result of
    CountVectorizer, for example) and transform into tf-idf matrix
    ------
    :method: tf_transform - calculating matrix of frequencies for each document
    in corpus
    :method: idf_transform - calculating idf metric for each 'word' in coprus
    :method: fit_transform - calculating tf-idf matrix for corpus
    """

    @staticmethod
    def tf_transform(freq_corpus: list[list]):
        """
        Static method for calculating tf matrix for each 'document' in corpus
        ------
        :param: freq_corpus - matrix with absolute frequencies for each word in
        corpus
        :type: list[list]
        ------
        :raises: TypeError if corpus not list

        :raises: ValueError if element(s) in corpus not int
        ------
        :rtype: list[list]
        :return: matrix of frequencies for each word in document
        """
        if not isinstance(freq_corpus, list):
            raise TypeError("Corpus must be list")
        for corpus_elem in freq_corpus:
            if sum([isinstance(elem, int) for elem in corpus_elem]) != len(
                    corpus_elem):
                raise ValueError("Corpus must contain only int values")

        result_freq_corpus = []
        for lst in freq_corpus:
            result_freq_corpus.append(
                [elem / sum(lst) for elem in lst])

        return result_freq_corpus

    @staticmethod
    def idf_transform(freq_corpus):
        """
        Static method for calculating idf list for each 'document' in corpus
        ------
        :param: freq_corpus - matrix with absolute frequencies for each word in
        corpus
        :type: list[list]
        ------
        :raises: TypeError if corpus not list

        :raises: ValueError if element(s) in corpus not int
        ------
        :rtype: list
        :return: list of idf-metric for each word in corpus
        """
        if not isinstance(freq_corpus, list):
            raise TypeError("Corpus must be list")
        for corpus_elem in freq_corpus:
            if sum([isinstance(elem, int) for elem in corpus_elem]) != len(
                    corpus_elem):
                raise ValueError("Corpus must contain only int values")

        total = len(freq_corpus)
        cur_lst = [0 for _ in range(len(freq_corpus[0]))]
        for lst in freq_corpus:
            cur_lst = [cur_lst[i] + int(lst[i] != 0) for i in
                       range(len(cur_lst))]

        result_idf = [math.log((total + 1) / (elem + 1)) + 1 for elem
                      in cur_lst]
        return result_idf

    def fit_transform(self, freq_corpus):
        """
        Method for calculating tf-idf matrix for corpus
        ------
        :param: self - reference to current object of this class
        :type: TfIdfTransformer

        :param: freq_corpus - matrix with absolute frequencies for each word in
        corpus
        :type: list[list]
        ------
        :rtype: list[list]
        :return: matrix of tf-df metric for each word in document
        """
        tf_corp = self.tf_transform(freq_corpus)
        idf_corp = self.idf_transform(freq_corpus)

        tf_idf_result = [[round(lst[i] * idf_corp[i], 3) for i in
                          range(len(lst))] for lst in tf_corp]

        return tf_idf_result
