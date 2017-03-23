# Protein Name Recognition

### How to run?
- requirements for python modules:
  * NLTK and a nltk model for 'punkt'
  
- install
```
git clone https://github.com/jeekim/gene_name_tagger.git
pip install nltk
python -m nltk.downloader
Downloader> d punkt
Downloader> q

cd gene_name_tagger
```
- test: annotates protein-test.txt file.
```commandline
python bin/tagger.py test protein-test
```
- train: shows precision, recall, and f1-measures after training.
```commandline
python bin/tagger.py train protein-train
```
- build: generates a CRF model used for test.
```commandline
python bin/tagger.py build protein-train
```

### Task and approach
Finding protein names in sentences is a sequence tagging problem in which
previous tagging results affect following words. Conditional Random Fields
(CRF) algorithm is known to perform well for several problems such as named entity
recognition, POS tagging, etc. [1]. In this task, I used a machine learning framework,
Mallet [2].

### Problem representation

##### Tokenization
Tokenization can affects performance. In this task, I used a simple punctuation-based
tokenizer in NLTK 3.0 [3].

##### Features
In machine learning, extracting and selecting features are one of the most important steps
in developing classifiers. For this task, I selected simple features:
- word
- stemmed word.
- number feature
- allcaps feature

##### Example
In Mallet, each line represents one token, and has the format:
feature_1 feature_2 ... feature_n label

For example, a sentence snippet
(, IL-6 production, and, in combination with cytokines, to Ig isotype switching.)
is represented as follows (token, token with s removed at the end, ALLCAPS if it exists, label): 

```
, , O
IL IL ALLCAPS GENE
- - GENE
6 6 GENE
production production O
, , O
and and O
, , O
in in O
combination combination O
with with O
cytokines cytokine O
, , O
to to O
Ig Ig O
isotype isotype O
switching switching O
. O
```

### Experimental results

##### How to train?
- I divided the provided set (protein-train.txt) into 50% for training and
50% for testing. 10 cross-validation can be an option.

##### How to evaluate?
- Accuracy is a popular measure. However, when classes are unbalanced,
precision and recall are more commonly used.

##### different sets of features

| Feature representation (FR)     |        | Train  |        |        | Test   |        |
|---------------------------------|--------|--------|--------|--------|--------|--------|
|                                 | P      | R      | F      | P      | R      | F      |
| base                            | 0.8925 | 0.6168 | 0.7295 | 0.8804 | 0.6141 | 0.7235 |
| base + stem                     | 0.8929 | 0.6219 | 0.7331 | 0.8791 | 0.6193 | 0.7267 |
| base + stem + number            | 0.9019 | 0.6272 | 0.7398 | 0.8887 | 0.6292 | 0.7368 |
| base + stem + allcaps           | 0.9493 | 0.9284 | 0.9387 | 0.91   | 0.8666 | 0.8878 |
| base + stem + number + allcaps  | 0.9505 | 0.909  | 0.9293 | 0.9165 | 0.8535 | 0.8838 |

- For training, token-based precision and recall were calculated.

##### Effects of a number of iterations for base + stem + allcaps representation

| FR   |        | Train  |        |        | Test   |        |
|------|--------|--------|--------|--------|--------|--------|
|      | P      | R      | F      | P      | R      | F      |
| 100  | 0.9272 | 0.8411 | 0.882  | 0.8943 | 0.7984 | 0.8436 |
| 200  | 0.9466 | 0.9219 | 0.9341 | 0.9064 | 0.8641 | 0.8847 |
| 500  | 0.9493 | 0.9284 | 0.9387 | 0.91   | 0.8666 | 0.8878 |
| 1000 | 0.9493 | 0.9284 | 0.9387 | 0.91   | 0.8666 | 0.8878 |

- This table shows training converges after 500 iterations.

### How to improve?
- Can I use word2vec or glove to improve recall
- Does it work on full-text articles?
- How can I adapt this approach to chemical names?
- Can I use cross validation for more reliable evaluation?



### References and Resources
[1] Sutton, Charles and McCallum, Andrew, An introduction to conditional random fields for relational learning,
Introduction to statistical relational learning, p93-128, 2006

[2] Mallet: http://mallet.cs.umass.edu/

[3] NLTK 3.0: http://www.nltk.org/
