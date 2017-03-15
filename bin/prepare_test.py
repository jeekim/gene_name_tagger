from nltk.tokenize import WordPunctTokenizer
#
f = open('data/protein-test.txt')

lines = f.readlines()
a = "".join(lines)
it = WordPunctTokenizer().span_tokenize(a)
spans = list(it)

gene_end = 0
for span in spans:
    s, e = span  # span
    if a[s:e] is ".":
        print(a[s:e], "\n")
    else:
        print(a[s:e])

