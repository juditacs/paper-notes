# Neural networks in general

These papers are related to neural networks in general.
I also put old-school neural net stuff here.

## Why Self-Attention? A Targeted Evaluation of Neural Machine Translation Architectures

### Tang et al., 2018

[arXiv](https://arxiv.org/abs/1808.08946)

- Transformer and CNN outperform traditional RNN in machine translation
- argued: this is due to shorter network paths make them better at modeling
  long-range dependencies
- has not been tested empirically, **main contribution of the paper**
- difficult to attribute architectural changes to improvement in BLEU
- their hypothesis: CNN and Transformer are good semantic feature extractors,
  rather than better at long-range dependencies
- contrastive evaluation of NMT tasks (*bad* examples should score lower than
  *good* examples)
  1. subject-verb agreement
  2. word sense disambiguation
  3. (NMT BLEU - mostly for sanity checking)

#### Models

1. RNNS2S with attention: exact formulation for attention is not given
2. ConvS2S
3. Transformer
4. RNN-bideep: SOTA for NMT with RNN

#### Results

1. NMT BLEU/PPL: Transformer best, ConvS2S worst
2. subject-verb agreement: ConvS2S is much worse than the others and the
   difference gets larger as the distance increases
3. WSD: Transformer is far better than the others - because it extracts
   semantic features?

- Extra model: TransRNN (Transformer encoder, RNN decoder)
- tested on WSD, Transformer is better, RNNS2S is worse -> decoder affects WSD

## Extracting Automata from Recurrent Neural Networks Using Queries and Counterexamples

### Weiss et al., 2017

They extract automata from trained RNNs.

The expression 'as an abuse of notation' appears at least 3 times.

TODO

## Localist Attractor networks

### Zemel and Mozer, 2001

- attractor networks
  - _map an input space, usually continuous, to a sparse output space_
  - states = attractor basins
  - priming: recent history of the network
  - gang affect: an attractor pulls stronger if there are more attractors in its neighborhood
  - applications: pattern completion
- comparison to nearest neighbor classifier
  - no need to enumerate the states, they are implicitely encoded in the weights of the network
  - some degree of biological plausibility (?)
  - _in most formulaition, the dynamics can be characterized by gradient descent in an energy landscape_
- three sets of simulation
  1. random state-space
  2. faces
  3. words: three letter English words. Query partially contrained words (i.e. must end with E)
- they demonstrate robust convergence by testing random 1000 queries on the 3-letter word network (random with 80% 0, 10% 1 and 10% -1) and all but 1 converged to an attractor
  - these are no longer words but random sparse vectors
- why isn't this cited more??? - even the authors seem to ignore it

