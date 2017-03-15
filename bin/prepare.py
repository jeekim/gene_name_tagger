import sys
import os

# sys.path.append('/home/jee/Projects/gene_name_tagger/lib/python/features')
# print(sys.path)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from nltk.tokenize import WordPunctTokenizer
from lib.python import features

# import lib.python.features


fb = features.FeatureBuilder()
gold = open('/home/jee/Projects/gene_name_tagger/data/protein-train.ann')

# build a dictionary for annotations
d = {}
for l in gold.readlines():
    k, v = l.split()[2:4]
    d[k] = int(v) - int(k)

#
f = open('/home/jee/Projects/gene_name_tagger/data/protein-train.txt')

lines = f.readlines()
a = "".join(lines)
it = WordPunctTokenizer().span_tokenize(a)
t = list(it)

gene_end = 0
for span in t:
    s, e = span  # span
    tok = a[s:e]
    if d.get(str(s)):
        gene_end = s + int(d.get(str(s)))
        print(fb.generate(tok), "GENE")
    elif e <= gene_end:
        print(fb.generate(tok), "GENE")
    else:
        if tok is ".":
            print(tok, "O", "\n")
        else:
            print(fb.generate(tok), "O")
