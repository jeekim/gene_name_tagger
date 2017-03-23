import sys
import os
import subprocess
from nltk.tokenize import WordPunctTokenizer
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.corpus import CorpusBuilder


def build(filename):
    """ Generates a CRF model given a training file (file_basename.txt). """
    cb = CorpusBuilder()
    # generate a training file for Mallet (file_basename.trn).
    cb.training(filename)

    #p = subprocess.Popen(['java', '-cp', 'lib/mallet.jar:lib/mallet-deps.jar', 'cc.mallet.fst.SimpleTagger', '--train', 'true',
     #                     '--model-file', 'model/genecrf', '--iterations', '500', 'data/{}.trn'.format(filename)]
      #                   , stdout=subprocess.PIPE)
    # p.stdout.close()

    subprocess.call(
        ['java', '-cp', 'lib/mallet.jar:lib/mallet-deps.jar', 'cc.mallet.fst.SimpleTagger', '--train', 'true',
         '--model-file', 'model/genecrf', '--iterations', '500', 'data/{}.trn'.format(filename)])


def train(filename):
    """ Validates a CRF model on 50% training and 50% test sets. Provides precision, recall, and f1 measure. """
    cb = CorpusBuilder()
    # generate a training file for Mallet (file_basename.trn).
    cb.training(filename)

    subprocess.call(
        ['java', '-cp', 'lib/mallet.jar:lib/mallet-deps.jar', 'cc.mallet.fst.SimpleTagger', '--train', 'true',
         '--test', 'perclass', '--iterations', '500', 'data/{}.trn'.format(filename)]
        , stdout=subprocess.PIPE)
    # p.stdout.close()


def test(filename):
    """ Generates protein annotation given a test file (file_basename.txt). """
    cb = CorpusBuilder()

    # generate a test file for Mallet (file_basename.tst).
    cb.testing(filename)

    f = open('data/{}.txt'.format(filename))
    lines = f.readlines()
    corpus = "".join(lines)
    spans = WordPunctTokenizer().span_tokenize(corpus)

    # java command to run a mallet model.
    p = subprocess.Popen(['java', '-cp', 'lib/mallet.jar:lib/mallet-deps.jar', 'cc.mallet.fst.SimpleTagger',
                          '--model-file', 'model/genecrf', '--include-input', 'true', 'data/{}.tst'.format(filename)]
                         , stdout=subprocess.PIPE)
    out = p.stdout

    # producing annotations from CRF outputs.
    p_gene_s, p_gene_e = -1, -1
    p_name = {}
    t = 1
    for span in spans:
        s, e = span
        tok = out.readline().decode("utf-8").rstrip('\n').strip(' ')
        if tok == "":
            tok = out.readline().decode("utf-8").rstrip('\n').strip(' ')

        if tok.startswith("GENE"):
            if not s == p_gene_e:  # new gene starts.
                p_name = {'name': corpus[s:e], 's': s, 'e': e}
            else:  # the same gene continues.
                p_name['name'] += corpus[s:e]
                p_name['e'] = e
            p_gene_s, p_gene_e = s, e
        else:  # not a gene
            if p_name:
                print('T{}\tProtein {} {}\t{}'.format(t, p_name['s'], p_name['e'], p_name['name']))
                p_name = {}
                t += 1
    out.close()

if __name__ == "__main__":
    if not len(sys.argv) == 3:
        print("usage: program train|build|test file_basename")
        sys.exit()

    filename = sys.argv[2]

    if sys.argv[1] == "test":
        test(filename)
    elif sys.argv[1] == "build":
        build(filename)
        # print("building a model is done.")
    elif sys.argv[1] == "train":
        train(filename)
    else:
        print(sys.argv[1], "is not a supported option.")
#