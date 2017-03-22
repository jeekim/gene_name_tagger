import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from nltk.tokenize import WordPunctTokenizer
from lib.python import features


class CorpusBuilder:

    def __init__(self):
        self.fb = features.FeatureBuilder()

    def training(self, filename):
        ann = open('data/{}.ann'.format(filename))

        # build a dictionary for annotations
        d = {}
        for l in ann.readlines():
            k, v = l.split()[2:4]
            d[k] = int(v) - int(k)

        f = open('data/{}.txt'.format(filename))
        lines = f.readlines()
        corpus = "".join(lines)
        spans = WordPunctTokenizer().span_tokenize(corpus)
        train_corpus = ""

        gene_end = 0
        for span in spans:
            s, e = span  # span
            tok = corpus[s:e]
            if d.get(str(s)):
                gene_end = s + int(d.get(str(s)))
                # print(self.fb.generate(tok), "GENE")  # TODO: tokens?
                train_corpus += '{} GENE\n'.format(self.fb.generate(tok))
            elif e <= gene_end:
                # print(self.fb.generate(tok), "GENE")
                train_corpus += '{} GENE\n'.format(self.fb.generate(tok))
            else:
                if tok == ".":
                    # print(tok, "O", "\n")
                    train_corpus += '{} O\n\n'.format(tok)
                else:
                    # print(self.fb.generate(tok), "O")
                    train_corpus += '{} O\n'.format(self.fb.generate(tok))

        o = open('data/{}.trn'.format(filename), 'w')
        o.write(train_corpus)
        return train_corpus

    def testing(self, filename):
        f = open('data/{}.txt'.format(filename))
        lines = f.readlines()
        corpus = "".join(lines)
        spans = WordPunctTokenizer().span_tokenize(corpus)
        test_corpus = ""

        for span in spans:
            s, e = span  # span
            tok = corpus[s:e]
            if tok is ".":  # TODO: better algorithm for sentence detection
                # print(tok, "\n")
                test_corpus += '{}\n\n'.format(tok)
            else:
                # print(self.fb.generate(tok))
                test_corpus += '{}\n'.format(self.fb.generate(tok))

        o = open('data/{}.tst'.format(filename), 'w')
        o.write(test_corpus)

        return test_corpus


def main():
    if not len(sys.argv) == 3:
        print('usage: program train|test file_basename')
        sys.exit()

    cb = CorpusBuilder()
    filename = sys.argv[2]

    if sys.argv[1] == "train":
        print(cb.training(filename)[:50])
    elif sys.argv[1] == "test":
        print(cb.testing(filename)[:50])
    else:
        print('option must be either train or test!')
        sys.exit()


if __name__ == "__main__":
    main()

#