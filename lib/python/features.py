import re
from nltk.stem import RegexpStemmer


class FeatureBuilder:
    """
    A class to generate features.
    """
    def __init__(self):
        self.st = RegexpStemmer('s$', min=4)

    def generate(self, token):  # TODO: tokens?
        features = list()

        features.append(token)
        # stemming
        features.append(self._stem(token))  # non-static
        features.append(FeatureBuilder._number(token))  # static

        features = filter(lambda x: x != "", features)
        # features = list(set(features))

        return " ".join(features)

    def _stem(self, token):
        stemmed = self.st.stem(token)
        return stemmed

    def _number(token):
        p = re.compile('^\d+$')
        if p.match(token):
            return "NUMBER"
        else:
            return ""


if __name__ == "__main__":
    fb = FeatureBuilder()
    print(fb.generate('inteferones'))
