import subprocess
from nltk.tokenize import WordPunctTokenizer


class Tagger:
    pass

#  https://github.com/sam-clark/Twitter-NER/blob/master/python/ner/extractEntities2.py

if __name__ == "__main__":

    f = open('data/protein-test.txt')

    lines = f.readlines()
    corpus = "".join(lines)
    spans = WordPunctTokenizer().span_tokenize(corpus)

    p = subprocess.Popen(['java', '-cp', 'lib/mallet.jar:lib/mallet-deps.jar', 'cc.mallet.fst.SimpleTagger',
                          '--model-file', 'model/genecrf_v4', '--include-input', 'true', 'data/gene_v4_test.txt'],
                         # stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    # p.stdin.write("".join(f.readlines()))
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