# gene_name_tagger


### how to improve

- v1: baseline
```
Evaluator iteration=500 cost=NA (not Optimizable.ByValue)
Per-token results for Training
Training label O P 0.9602 R 0.992 F1 0.9759
Training label GENE P 0.8925 R 0.6168 F1 0.7295
Macro-average (including non-used labels) P 0.9263 R 0.8044 F 0.8527
Macro-average (excluding non-used labels) P 0.9263 R 0.8044 F 0.8527
Per-token results for Testing
Testing label O P 0.9605 R 0.9912 F1 0.9756
* Testing label GENE P 0.8804 R 0.6141 F1 0.7235
Macro-average (including non-used labels) P 0.9205 R 0.8026 F 0.8496
Macro-average (excluding non-used labels) P 0.9205 R 0.8026 F 0.8496
```
- v2: stemming
```
Evaluator iteration=500 cost=NA (not Optimizable.ByValue)
Per-token results for Training
Training label O P 0.9607 R 0.992 F1 0.9761
Training label GENE P 0.8929 R 0.6219 F1 0.7331
Macro-average (including non-used labels) P 0.9268 R 0.8069 F 0.8546
Macro-average (excluding non-used labels) P 0.9268 R 0.8069 F 0.8546
Per-token results for Testing
Testing label O P 0.961 R 0.991 F1 0.9758
* Testing label GENE P 0.8791 R 0.6193 F1 0.7267
Macro-average (including non-used labels) P 0.9201 R 0.8052 F 0.8512
Macro-average (excluding non-used labels) P 0.9201 R 0.8052 F 0.8512
```
- v3: BIO
```
Evaluator iteration=500 cost=NA (not Optimizable.ByValue)
Per-token results for Training
Training label O P 0.9616 R 0.992 F1 0.9766
Training label BGENE P 0.9172 R 0.5377 F1 0.678
Training label IGENE P 0.8588 R 0.7024 F1 0.7728
Macro-average (including non-used labels) P 0.9126 R 0.744 F 0.8091
Macro-average (excluding non-used labels) P 0.9126 R 0.744 F 0.8091
Per-token results for Testing
Testing label O P 0.9623 R 0.9911 F1 0.9765
Testing label BGENE P 0.9122 R 0.5377 F1 0.6766
Testing label IGENE P 0.8444 R 0.7036 F1 0.7676
Macro-average (including non-used labels) P 0.9063 R 0.7442 F 0.8069
Macro-average (excluding non-used labels) P 0.9063 R 0.7442 F 0.8069
```
- etc.

### how to run?
```
java -cp "lib/mallet.jar:lib/mallet-deps.jar" cc.mallet.fst.SimpleTagger --train true --test lab --threads 2 ner2.txt
```

### how to evaluate?

- accuracy vs. precision and recall

### results

|      |        | train  |        |        | test   |        |
|------|--------|--------|--------|--------|--------|--------|
|      | P      | R      | F      | P      | R      | F      |
| base | 0.8925 | 0.6168 | 0.7295 | 0.8804 | 0.6141 | 0.7235 |
| stem | 0.8929 | 0.6219 | 0.7331 | 0.8791 | 0.6193 | 0.7267 |
| bio  |        |        |        |        |        |        |