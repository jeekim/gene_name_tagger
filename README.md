# gene_name_tagger

### Task and How to Approach?

### What is CRF and why use it?


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

- v4: number
```
Evaluator iteration=500 cost=NA (not Optimizable.ByValue)
Per-token results for Training
Training label O P 0.9613 R 0.9927 F1 0.9767
Training label GENE P 0.9019 R 0.6272 F1 0.7398
Macro-average (including non-used labels) P 0.9316 R 0.8099 F 0.8583
Macro-average (excluding non-used labels) P 0.9316 R 0.8099 F 0.8583
Per-token results for Testing
Testing label O P 0.962 R 0.9917 F1 0.9766
Testing label GENE P 0.8887 R 0.6292 F1 0.7368
Macro-average (including non-used labels) P 0.9254 R 0.8104 F 0.8567
Macro-average (excluding non-used labels) P 0.9254 R 0.8104 F 0.8567
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


##### BO

|             |        | train  |        |        | test   |        |
|-------------|--------|--------|--------|--------|--------|--------|
|             | P      | R      | F      | P      | R      | F      |
| base        | 0.8925 | 0.6168 | 0.7295 | 0.8804 | 0.6141 | 0.7235 |
| stem        | 0.8929 | 0.6219 | 0.7331 | 0.8791 | 0.6193 | 0.7267 |
| stem + num  | 0.9019 | 0.6272 | 0.7398 | 0.8887 | 0.6292 | 0.7368 |
| stem + num 2| 0.8968 | 0.5456 | 0.6785 | 0.8886 | 0.5511 | 0.6803 |


##### number of iterations  (stem + num) learning curve?

|      |        | train  |        |        | test   |        |
|------|--------|--------|--------|--------|--------|--------|
|      | P      | R      | F      | P      | R      | F      |
| 500  | 0.9019 | 0.6272 | 0.7398 | 0.8887 | 0.6292 | 0.7368 |
| 1000 | 0.9157 | 0.7224 | 0.8076 | 0.8971 | 0.7137 | 0.7950?|
| 2000 | 0.9159 | 0.7442 | 0.8211 | 0.8973 | 0.7308 | 0.8055 |
| 3000 | 0.9159 | 0.7442 | 0.8211 | 0.8973 | 0.7308 | 0.8055 |

- 3000
real	17m22.422s
user	27m30.456s
sys	0m18.440s

##### BIO

### Discussion

- Use word2vec or glove to improve recall?
- Does it work on full-text articles?
- How to adapt to chemical names?
- continuous learning?
- cross-validation for more reliable evaluation?
- visualization?
- three letter ...
- three letter ...

### References and Resources
- Mallet: http://mallet.cs.umass.edu/
- NLTK 3.0: http://www.nltk.org/