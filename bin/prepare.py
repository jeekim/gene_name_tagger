from nltk.tokenize import WordPunctTokenizer

gold = open('data/protein-train.ann')

# build a dictionary for annotations
d = {}
for l in gold.readlines():
    k, v = l.split()[2:4]
    d[k] = int(v) - int(k)

#
f = open('data/protein-train.txt')

lines = f.readlines()
a = "".join(lines)
it = WordPunctTokenizer().span_tokenize(a)
t = list(it)

gene_end = 0
for span in t:
    s, e = span  # span
    if d.get(str(s)):
        gene_end = s + int(d.get(str(s)))
        print(a[s:e], "GENE")
    elif e <= gene_end:
        print(a[s:e], "GENE")
    else:
        if a[s:e] is ".":
            print(a[s:e], "O", "\n")
        else:
            print(a[s:e], "O")

