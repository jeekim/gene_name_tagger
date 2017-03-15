import sys
import os
# sys.path.append('/home/jee/Projects/gene_name_tagger/lib/python/features')
# print(sys.path)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from nltk.tokenize import WordPunctTokenizer
from lib.python import features
# import lib.python.features

fb = features.FeatureBuilder()

f = open('data/protein-test.txt')

lines = f.readlines()
a = "".join(lines)
it = WordPunctTokenizer().span_tokenize(a)
spans = list(it)

gene_end = 0
for span in spans:
    s, e = span  # span
    tok = a[s:e]
    if a[s:e] is ".":
        print(tok, "\n")
    else:
        print(fb.generate(tok))

