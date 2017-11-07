# GAN

Everything related to adversarial networks.

## Adversarial Generation of Natural Language

### Rajeswar et al., 2017

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
