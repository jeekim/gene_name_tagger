from nltk.stem import RegexpStemmer


class FeatureBuilder:
    def __init__(self):
        self.st = RegexpStemmer('s$', min=4)

    def generate(self, token):
        features = list()

        features.append(token)
        # stemming
        features.append(self._stem(token))

        return " ".join(features)

    def _stem(self, token):
        stemmed = self.st.stem(token)
        return stemmed


if __name__ == "__main__":
    fb = FeatureBuilder()
    print(fb.generate('inteferones'))
