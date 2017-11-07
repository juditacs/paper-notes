# Adversarial Generation of Natural Language

## Rajeswar et al., 2017

This paper started a flamewar between Yoav Goldberg and Yann Lecun.
[Goldberg's original adversarial review](https://medium.com/@yoav.goldberg/an-adversarial-review-of-adversarial-generation-of-natural-language-409ac3378bd7)

- abstract: natural language generation using GANs
- how they handle the discrete output problem (i.e. words are one-hot vectors): _In this work, we address the discrete output space problem by simply forcing the discriminator to operate on continuous valued output distributions_
  - Goldberg heavily critized this because the generator may only learn to output distributions that are near-one hot vectors to fool the discriminator. Bahdanau points out that WGAN might solve this problem. - The authors also mention this and claim that WGAN solves it. They claim this is evidences by the results. They do not investigate this specific problem in more detail.
- they compare several GAN architectures: 
  - generator: LSTM, LSTM-P (with peephole), CNN
  - discriminator: LSTM, CNN
  - objective: WGAN, WGAN-GP, GAN-GP, LSGAN
- dataset: Penn TreeBank, Chinese poetry
- results: they present high accuracies according to a PCFG but the example sentences are unimpressive
- they experiment with both **character** and **word** level generation
- stuff I learned:
  - teacher forcing (Williams and Zipser, 1989): the inputs to the network are fixed and the model is trained to predict only the next item in the sequence given all previous observations
  - exposure bias: a model is only trained conditioned on groundtruth contexts and is not exposed to its own errors (Wiseman and Rush, 2016)
  

# Localist Attractor networks

## Zemel and Mozer, 2001

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
- why isn't this cited more???


# Morphological Inflection Generation Using Character Sequence to Sequence Learning

## Faruqui et al. 2016

- semi-supervised learning
  1. use language model for output reranking - integrated to beam search
  2. interpolate LM probability with their inflection generation model and use this as the loss function
- dataset

## Word and morpheme segmentation

[Liu and Liu, 2017. Introduction to the Shared Tasks on Cross-lingualWord Segmentation and Morpheme Segmentation](segmentation.md#introduction-to-the-shared-tasks-on-cross-lingual-word-segmentation-and-morpheme-segmentation)

[Shao, 2017. Cross-lingual Word Segmentation and Morpheme Segmentation as Sequence Labelling](segmentation.md#cross-lingual-word-segmentation-and-morpheme-segmentation-as-sequence-labelling)
