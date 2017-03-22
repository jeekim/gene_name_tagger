# Protein Name Recognition

### Task and approach
Finding protein names in sentences is a sequence tagging problem in which
previous tagging results affect following words. Conditional Random Fields
(CRF) algorithm is known to perform several problems such as named entity
recognition, POS tagging, etc. []. In this task, I have 

### Problem representation

##### Tokenization

##### Features
In machine learning, selecting features is one of the most important steps
in developing classifiers. For this task, I selected simple features:
word, stem

#####
```
Cross Cros O
- - O
linking linking O
CD40 CD40 GENE
on on O
B B O
cells cell O
can can O
lead lead O
to to O
homotypic homotypic O
cell cell O
adhesion adhesion O
, , O
IL IL GENE
- - GENE
6 6 NUMBER GENE
production production O
, , O
```


##### Experimental results

### How to evaluate?

- Accuracy is a popular measure. However, when classes are unbalanced,
precision and recall are more commonly used.

### How to train?

- I divided the provided set (protein-train.txt) into 50% for training and
50% for testing. 10 cross-validation can be an option.


##### different sets of features

|                       |        | train  |        |        | test   |        |
|-----------------------|--------|--------|--------|--------|--------|--------|
|                       | P      | R      | F      | P      | R      | F      |
| base                  | 0.8925 | 0.6168 | 0.7295 | 0.8804 | 0.6141 | 0.7235 |
| base + stem           | 0.8929 | 0.6219 | 0.7331 | 0.8791 | 0.6193 | 0.7267 |
| base + stem + number  | 0.9019 | 0.6272 | 0.7398 | 0.8887 | 0.6292 | 0.7368 |

##### number of iterations for base + stem + number

|      |        | train  |        |        | test   |        |
|------|--------|--------|--------|--------|--------|--------|
|      | P      | R      | F      | P      | R      | F      |
| 500  | 0.9019 | 0.6272 | 0.7398 | 0.8887 | 0.6292 | 0.7368 |
| 1000 | 0.9157 | 0.7224 | 0.8076 | 0.8971 | 0.7137 | 0.7950?|
| 2000 | 0.9159 | 0.7442 | 0.8211 | 0.8973 | 0.7308 | 0.8055 |
| 3000 | 0.9159 | 0.7442 | 0.8211 | 0.8973 | 0.7308 | 0.8055 |



### Discussion

- Use word2vec or glove to improve recall?
- Does it work on full-text articles?
- How to adapt to chemical names?
- continuous learning?
- cross-validation for more reliable evaluation?
- visualization?
- three letter ...
- three letter ...
- BIO

### how to run?
```
python bin/tagger.py protein-test
```

### References and Resources
- Mallet: http://mallet.cs.umass.edu/
- NLTK 3.0: http://www.nltk.org/