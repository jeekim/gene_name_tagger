import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from nltk.tokenize import WordPunctTokenizer
from lib.python import features


class CorpusBuilder:

    def __init__(self):
        self.fb = features.FeatureBuilder()

    def training(self):
        gold = open('/home/jee/Projects/gene_name_tagger/data/protein-train.ann')

        # build a dictionary for annotations
        d = {}
        for l in gold.readlines():
            k, v = l.split()[2:4]
            d[k] = int(v) - int(k)

        f = open('/home/jee/Projects/gene_name_tagger/data/protein-train.txt')
        lines = f.readlines()
        corpus = "".join(lines)
        spans = WordPunctTokenizer().span_tokenize(corpus)

        gene_end = 0
        for span in spans:
            s, e = span  # span
            tok = corpus[s:e]
            if d.get(str(s)):
                gene_end = s + int(d.get(str(s)))
                print(self.fb.generate(tok), "GENE")  # TODO: tokens?
            elif e <= gene_end:
                print(self.fb.generate(tok), "GENE")
            else:
                if tok is ".":
                    print(tok, "O", "\n")
                else:
                    print(self.fb.generate(tok), "O")

    def testing(self):
        f = open('data/protein-test.txt')

        lines = f.readlines()
        corpus = "".join(lines)
        spans = WordPunctTokenizer().span_tokenize(corpus)
        # spans = list(it)
        # gene_end = 0
        for span in spans:
            s, e = span  # span
            tok = corpus[s:e]
            if tok is ".":
                print(tok, "\n")
            else:
                print(self.fb.generate(tok))

    def testing_with_offset(self):
        pass

def main():
    if not len(sys.argv) == 2:
        print('usage: program train|test')
        sys.exit()

    cb = CorpusBuilder()

    if sys.argv[1] == "train":
        cb.training()
    elif sys.argv[1] == "test":
        cb.testing()
    else:
        print('option must be either train or test!')
        sys.exit()


if __name__ == "__main__":
    main()
    # cb = CorpusBuilder()
    # cb.training()
    # cb.testing()