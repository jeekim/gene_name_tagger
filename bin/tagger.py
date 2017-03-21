import subprocess


class Tagger:
    pass


#  https://github.com/sam-clark/Twitter-NER/blob/master/python/ner/extractEntities2.py

if __name__ == "__main__":
    # out = os.system("java --version")
    # print(out)
    # f = open('data/gene_v4_test.txt')
    p = subprocess.Popen(['java', '-cp', 'lib/mallet.jar:lib/mallet-deps.jar', 'cc.mallet.fst.SimpleTagger',
                          '--model-file', 'model/genecrf_v4', '--include-input', 'true', 'data/gene_v4_test.txt'],
                         # stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    # p.stdin.write("".join(f.readlines()))
    out = p.stdout.readlines()
    for o in out:
        token = o.decode("utf-8").rstrip('\n').strip(' ')
        if token.startswith("GENE"):
            print(token)
        else:
            print(token)