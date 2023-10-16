class CountVectorizer:
    def __init__(self) -> None:
        """
        Constructor: initialize __feat_names: list which contains unique words
        from corpus of text
        ------
        :param self: reference to current object of this class
        :type self: CountVectorizer
        """
        self.__feat_names = []

    def fit_transform(self, corpus: list[str]) -> list[list]:
        """
        Method for getting matrix of our corpus of documents
        ------
        :param self: reference to current object of this class
        :type self: CountVectorizer

        :param corpus: corpus of documents for transforming
        :type corpus: list[str]
        ------
        :raises: TypeError if corpus not list

        :raises: ValueError if element(s) in corpus not string

        :raises: ValueError if element(s) in corpus contains symbols except
        letters or numbers
        ------
        :rtype: list[list]
        :return: vectorized corpus of documents by BOW algorithm
        """
        self.__feat_names.clear()
        if not isinstance(corpus, list):
            raise TypeError("Corpus must be list")
        for corpus_elem in corpus:
            if not isinstance(corpus_elem, str):
                raise ValueError("Corpus must contain only string values")
            for symbol in ',;!?".-=+*:/\\':
                if symbol in corpus_elem:
                    raise ValueError(
                        "Corpus must contain only-letters string values"
                    )
            for word in corpus_elem.lower().split(" "):
                if word not in self.__feat_names:
                    self.__feat_names.append(word)

        result_word_matrix = []
        for corpus_elem in corpus:
            dict_for_matrix = {word: 0 for word in self.__feat_names}
            for word in corpus_elem.lower().split(" "):
                dict_for_matrix[word] += 1
            result_word_matrix.append(list(dict_for_matrix.values()))

        return result_word_matrix

    def get_feature_names(self) -> list[str]:
        """
        Method for getting dictionary of corpus
        ------
        :param self: reference to current object of this class
        :type self: CountVectorizer
        ------
        :rtype: list[str]
        :return: dictionary of corpus
        """
        return self.__feat_names
