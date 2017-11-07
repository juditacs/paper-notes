# Word and morpheme segmentation

# Introduction to the Shared Tasks on Cross-lingualWord Segmentation and Morpheme Segmentation
(#liu:2016)

## Chao-Hong Liu and Qun Liu

Describes the  MLP 2017 shared task

### MLP 2017 shared task

1. morpheme segmentation: Amharic, Basque, Farsi, Filipino, Finnish, Kazakh, Marathi, and Uyghur
2. word segmentation: Japanese, traditional Chinese and Vietnamese

### Dataset

#### Notation

- `\\`: morpheme boundary
- ` `: word boundary
- `_`: 'used to indicate if a ‘word’ was concate- nated with its previous word as a morpheme' (Vietnamese only)

#### Preprocessing

- the Amharic corpus contained annotation for 'morpheme clusters' rather than morphemes
- the Filipino corpus contained prefix, root, infix, suffix information too
- all converted to the same format
- reviewed by language experts

### Baselines

- morpheme segmentation: Morfessor v. 2.0
- Japanese: MeCab v. 0.996 with ipadic 102 dictionary
- Chinese: Longest-word-first (LWF)
- Vietnamese: Learnt-rules (L-Rules)

### Results

- evaluation: F1 on boundary position detection
- 4 submissions
- BiRNN-CRF systems performed best for all languages (Shao, 2017)
  - baseline outperformed significantly
- unsupervised segmentation (Amharic, Basque, Farsi, Finnish, Uygur) also outperform the baseline (Passban et al., 2017)
- trigram-based for Japanese (No, 2017)
- CRF for Chinese (Sutantayawalee and Supnithi, 2017)


# Cross-lingualWord Segmentation andMorpheme Segmentation as Sequence Labelling

## Yan Shao

MLP 2017, highest ranking solution for all languages.
Used biRNN-CRF and ensemble decoding.

[Code](https://github.com/yanshao9798/segmenter)
[Paper](https://arxiv.org/pdf/1709.03756)
[Presentation video](https://www.youtube.com/watch?v=XQC_kxkk4rM)

### Feature extraction

- character-level sequential tagging
- for each character ($c_i$):
  1. the character itself - 50 dim
  2. the bigram $c_{i-1},c_i$ (not both bigrams, according to the video) - 50 dim
  3. the trigram $c_{i-2},c_{i-1},c_i$  - 50 dim
- BIES tagging + X for word boundaries (if available)
- sentence level instead of word level

### Experiments and results

- they used the same hyperparameters for each language
- trained for 30 epochs, adopt the best epoch after the model is trained for at least 5 epochs
- baseline: biRNN+CRF (viterbi for decoding)
- ensemble decoding: they train 4 models with the same parameters but different initialization
  - transition and conditional scores are averaged over the models
  - slight improvement over the baseline
- 90+ F-scores for all languages except Basque and Farsi, both had small training sets
