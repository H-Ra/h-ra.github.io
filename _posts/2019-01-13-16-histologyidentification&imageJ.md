---
layout: post
title: January 13, 2019 - Histology Identification Practice and ImageJ
---

### Lab Work 

Today I went over what method Laura has used to identify gonad sex and stage of oysters in a past paper (link to paper is [here](https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1002/eap.2060)), and thus, it will be the same format that we will be using for identification with the histology images of O. angasi. The method that is used is very similar to the da Silva paper except for 1 main thing: for gonad stage, the da Silva paper laid out 6 different stages (Inactive or resting gonad, Early gametogenesis, Advanced gametogenesis, Ripe gonad, Partially spawned gonad, and Reabsorbing gonad), but in Laura's paper, she decides to combine the Partially spawned gonad and Reabsorbing gonad to be one stage instead of two separate stages (laid out in the supporting information section [here](https://esajournals.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Feap.2060&file=eap2060-sup-0001-AppendixS1.pdf)). 

The main goals for quantifying the presence and stage of the gonads present in the histology images are: 

* For female gonads: identify if present and measure through ImageJ
* For male gonads: identify if present and identify stage of development (spermatogonia vs spermatids, etc...)

Thus, I tried to learn more about how to identify different stages of development for the male gonads - this will be the most difficult thing to differentiate since they are very small, so it is difficult to tell when a gonad is a spermatogonia versus a spermatocyte, etc... The main things that I noticed were the same things that I noticed from my last post (link is [here](https://h-ra.github.io/15-HistologyPapersPt2&DeterminationPractice/)) under the section "Gonad Stage determination". 

Possible tools to use in order to achieve goals laid out in "Next Steps" (at the end of this post):

* ImageJ
* Fiji (fiji is just imageJ)
* BioVoxxel Toolbox
* TWS (Trainable Weka Segmentation)
* ZEN Intellesis

Some interesting things that I learned and/or realized when looking up what types of programs/packages we could possibly use to achieve our goals include:

* Technique that we want to use in order to differentiate different gametes is known as "segmentation".
* We could also find a way to identify different stages of development of male gonads in a more quantitative way -- depends on the identification technique used to differentiate stages of spermatogenesis.  

---

### Next Steps

1. Figure out how we can possibly measure eggs for female stage identification on ImageJ
2. Figure out how we can associate gonads by color so that we can quantifiably see what percentage of each type of gonad is present (can identify what sex it is [hermaphrodite predominantly male, hermaphrodite predominantly female, hermaphrodite both sexes equally present]) on ImageJ