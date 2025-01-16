# Study on Machine Learning Bias Through the Analogy of Judgemental Frogs

## Study

### <b style='color: red; display: flex;'>Is confounding variable the right term for this? <h1>&#8595;</h1></b>

### Goal

This work builds on the work of [Marzyeh Ghassemi](https://healthyml.org/) who found that medical data can often inadvertently encode the patient's race<sup>1&2</sup> and David Bau's work (<b style='color: red;'>Needs citation</b>) which focuses on mechanistic interpretability. We want to study the effect of the leakage of a patient's race, which can act as a confounding variable, on the performance of diagnostic machine-learning models through the analogy of a synthetic dataset aiming to predict the wealth of a frog in Lilyland.

### Questions

1. Does a model trained on a biased dataset perform differently when evaluated on a non-biased dataset compared to the reverse?

2. Does changing the variance of the disenfranchised population lead to less bias?

3. What models and hyperparameters are more susceptible to biased data?

4. Can we isolate the model parameters that lead to bias?

5. If we remove variation in the confounding variable post-training (set all evaluation points to the non-disenfranchised population), does that change the model bias?

### Experimental Setup

In Lilyland there are two populations, the Red frogs and the Blue frogs, in which the difference can act as a confounding variable. Each frog's outfit is a signifier of their wealth (described more in [Data](#data)). In Frogtopia, the capital of Lilyland, the distributions of the wealth of both populations are equal ($\mu$<sub>Red</sub>==$\mu$<sub>Blue</sub> && $\sigma^2$<sub>Red</sub> == $\sigma^2$<sub>Blue</sub>). But in Pond Place the Blue frogs are disenfranchised ($\mu$<sub>Red</sub>>$\mu$<sub>Blue</sub> && $\sigma^2$<sub>Red</sub> == $\sigma^2$<sub>Blue</sub>).

#### Question 1
First, we assess whether a model trained on a Pond Place (biased) will perform differently when evaluated on a Frogtopia (unbiased) compared to the reverse. To do this we will train two Random Forests, one in each city, test it on the training data from that city, then validate it on the non-seen city. We hypothesize that the difference in distributions will cause the model trained on Pond Place to over-emphasize the confounding variable, leading it to fail validation on Frogtopia. In contrast, the lack of difference in Frogtopia will lead to a fair model that will succeed on Pond Place and can be used across distributions.

#### Question 2
Then we will assess the effect of changing the variance of the Blue population in Pond Place on the validation score of Frogtopia using a Random Forest model. To increase the variance we will remove samples from within the 1st standard deviation and to decrease it we will remove samples from beyond the 2nd standard deviation. We hypothesize that increasing the variation will increase the Pond Place model's validation score on Frogtopia by reducing the value of splitting the dataset by the confounding variable.

#### Question 3
Furthermore, we will asses what models and hyperparameters are more susceptible to biased data through a grid search (described more in [Grid Search](#grid-search)). We will use the search results to rank the models and hyperparameters on their susceptibleness. Then we will run tests and look into the literature to provide explanations for their scores. <b style='color: yellow;'>Hypothesis?</b>


#### Question 4
Additionally, we will look into ways of removing the influence of the confounding variable post-training. Building off of David Bau's work we will ... <b style='color: yellow;'>Find parts of the model that account for the confounding variable?</b>

#### Question 5
Continuing with this line of thinking, can we gain accurate predictions on the disenfranchised population by removing variation in the confounding variable, in this case by setting the population given to the model to always be Red? We hypothesize that this method would work only if the distribution of the disenfranchised population in the validation set matches that of the non-disenfranchised population in the training set.

### Data

### Grid Search

## Citations

 1. ([Medical Imaging Predicting Race](https://pubmed.ncbi.nlm.nih.gov/35568690/)) Gichoya JW, Banerjee I, Bhimireddy AR, Burns JL, Celi LA, Chen LC, Correa R, Dullerud N, Ghassemi M, Huang SC, Kuo PC, Lungren MP, Palmer LJ, Price BJ, Purkayastha S, Pyrros AT, Oakden-Rayner L, Okechukwu C, Seyyed-Kalantari L, Trivedi H, Wang R, Zaiman Z, Zhang H. AI recognition of patient race in medical imaging: a modeling study. Lancet Digit Health. 2022 Jun;4(6):e406-e414. doi: 10.1016/S2589-7500(22)00063-2. Epub 2022 May 11. PMID: 35568690; PMCID: PMC9650160.

 2. ([AI Determines Race from Medical Notes](https://arxiv.org/pdf/2205.03931)) H Adam, MY Yang, K Cato, I Baldini, C Senteio, LA Celi, J Zeng, M Singh, M Ghassemi. Write It Like You See It: Detectable Differences in Clinical Notes By Race Lead To Differential Model Recommendations. Arxiv. Epub 2022 Nov 1

 3. <b style='color: red;'>David Bau's Paper Citation Needed</b>

 4. ([Spurious Features](https://openreview.net/forum?id=Tkvmt9nDmB)) @article{
murali2023beyond,
title={Beyond Distribution Shift: Spurious Features Through the Lens of Training Dynamics},
author={Nihal Murali and Aahlad Manas Puli and Ke Yu and Rajesh Ranganath and kayhan Batmanghelich},
journal={Transactions on Machine Learning Research},
issn={2835-8856},
year={2023},
url={https://openreview.net/forum?id=Tkvmt9nDmB},
note={}
}
