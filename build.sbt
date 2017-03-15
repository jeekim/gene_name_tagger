lazy val train = taskKey[Unit]("Prints 'training ...'")

train := {
  "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --test lab --threads 2 data/ner2.txt" !
}

lazy val trainGene = taskKey[Unit]("Prints 'training gene tagger ...'")

trainGene := {
  "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --test lab --threads 2 data/gene.txt" !
}

lazy val generateGene = taskKey[Unit]("Prints 'generating a gene tagger model ...'")

generateGene := {
  "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --train true --model-file model/genecrf data/gene.txt" !
}

lazy val annotateGene = taskKey[Unit]("Prints 'annotating genes ...'")

annotateGene := {
  "java -cp lib/mallet.jar:lib/mallet-deps.jar cc.mallet.fst.SimpleTagger --model-file model/genecrf --include-input true data/gene_test.txt" !
}
