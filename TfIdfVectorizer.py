from CountVectorizer import CountVectorizer
from TfIdfTransformer import TfIdfTransformer


class TfIdfVectorizer(CountVectorizer):
    """
    Class for work with text by tf-idf vectorization
    ------
    :attr: __tf_idf_transformer - transformer for getting tf-idf matrix;
    TfIdfVectorizer object
    ------
    :method: __init__ - constructor
    :method: fit_transform: vectorization text
    """

    def __init__(self):
        """
        Constructor of class
        ------
        :param: self - reference to current object of this class
        :type self: TfIdfVectorizer
        """
        self.__tf_idf_transfromer = TfIdfTransformer()
        super(TfIdfVectorizer, self).__init__()

    def fit_transform(self, corpus: list[str]) -> list[list]:
        """
        Method for getting tf-idf matrix of our corpus of documents from text
        ------
        :param self: reference to current object of this class
        :type self: TfIdfVectorizer

        :param corpus: corpus of documents for transforming
        :type corpus: list[str]
        ------
        :rtype: list[list]
        :return: vectorized corpus of documents by tf-idf calculating
        """
        result_word_matrix = super(TfIdfVectorizer, self).fit_transform(corpus)
        return self.__tf_idf_transfromer.fit_transform(result_word_matrix)
