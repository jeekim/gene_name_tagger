import sys
import os
import subprocess
from nltk.tokenize import WordPunctTokenizer
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from bin.build_corpus import CorpusBuilder


class Tagger:
    pass


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("usage: program file_basename")
        sys.exit()

    filename = sys.argv[1]
    cb = CorpusBuilder()

    # generate a test file for mallet
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
#