from TfIdfVectorizer import TfIdfVectorizer


def main():
    """
    Function for modeling application work
    """
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    tf_idf_vectorizer = TfIdfVectorizer()
    result = tf_idf_vectorizer.fit_transform(corpus)

    print(result)

    print(tf_idf_vectorizer.get_feature_names())


if __name__ == "__main__":
    main()
