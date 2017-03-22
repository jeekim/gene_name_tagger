lazy val train = taskKey[Unit]("Prints 'training gene tagger ...'")

train := {
  "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --test perclass --iterations 1000 --threads 4 data/protein-train.trn" !
  // "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --test perclass --orders 2 --iterations 1000 --threads 2 data/gene_v4.txt" !
  // "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --test perclass --threads 2 data/gene_v3.txt" !
  // "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --test lab --threads 2 data/gene_v2.txt" !
}

lazy val generate = taskKey[Unit]("Prints 'generating a gene tagger model ...'")

generate := {
  // "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file model/genecrf_v4 data/gene_v4.txt" !
  "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file model/genecrf --iterations 1000 --threads 4 data/protein-train.trn" !
}

lazy val annotate = taskKey[Unit]("Prints 'annotating genes ...'")

annotate := {
  "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file model/genecrf --include-input true data/protein-test.tst" !
  // "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file model/genecrf --include-input true data/gene_v2_test.txt" !
}