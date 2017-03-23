import re
from nltk.stem import RegexpStemmer


class FeatureBuilder:
    """
    An instance of this class generates features for protein name recognition given a token.
    """
    def __init__(self):
        self.st = RegexpStemmer('s$', min=4)

    def generate(self, token):
        """ generates a list of features combining feature functions (e.g., _stem) """
        features = list()

        features.append(token)
        features.append(self._stem(token))
        # features.append(self._number(token))
        features.append(self._allcaps(token))

        features = filter(lambda x: x != "", features)

        return " ".join(features)

    def _stem(self, token):
        """ simple stemming by removing 's' at the end of a token. """
        stemmed = self.st.stem(token)
        return stemmed

    def _number(self, token):
        """ generates NUMBER feature is a token is a number. """
        p = re.compile('^\d+$')
        if p.match(token):
            return "NUMBER"
        else:
            return ""

    def _allcaps(self, token):
        """ generates ALLCAPS feature if a token consists of all the capital letters. """
        p = re.compile('^[A-Z]+$')
        if p.match(token):
            return "ALLCAPS"
        else:
            return ""

    def _initcap(self, token):
        """ generates INITCAP if a token starts with a capital letter. """
        pass  # TODO

    # TODO: add more features here.
    # e.g., _initcap, _twocaps, _twodisits, _greek, _roman, etc.

if __name__ == "__main__":
    fb = FeatureBuilder()
    print(fb.generate('inteferones'))
