# Morphological reinflection

These papers are related to morphological (re)inflection.


## Morphological Inflection Generation Using Character Sequence to Sequence Learning

### Faruqui et al. 2016

- semi-supervised learning
  1. use language model for output reranking - integrated to beam search
  2. interpolate LM probability with their inflection generation model and use this as the loss function
- dataset

TODO


## Morphological Inflection Generation with Hard Monotonic Attention

### Aharoni and Goldberg, 2017

[Paper](https://arxiv.org/abs/1611.01487)
[Code (dynet) and data](https://github.com/roeeaharoni/morphological-reinflection)

- hard attention: attends to a single position in the input sentence in one decoding step as opposed 
to soft attention which attends to a convex combination of input sequences
- sequence transduction is modeled as a sequence of two actions: _write_ and
  _step_
    - **monotonic**: _step_ can only be a forward step
    - _write_: write a symbol of the output vocabulary

- training data is converted to action sequences by a simple deterministic
  algorithm
- results: they beat soft attention for most languages

