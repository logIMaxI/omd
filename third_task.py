from CountVectorizer import CountVectorizer


def main():
    """
    Function for modeling application work
    """
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())

    print(count_matrix)


if __name__ == "__main__":
    main()
