---
layout: post
title: November 13, 2019 - Growth Rate Based On Size Distributions
---
###Recap of Yesterday

Yesterday, Shelly and I did some really fascinating analysis on the juvenile geoduck measurements made on ImageJ (see last post [here](https://h-ra.github.io/2-juvenilegeoduckdataanalysis/)) and we found that the juvenile geoducks in both var.low parental and var.low current treatments had a larger size distribution than all other treatments. 

This interesting discovery prompted us to delve into this a little more and to possibly find a growth rate for these treatments in order to account for this. But, the size of the geoducks in the beginning of the experiment are based on three "size classes" that were proportioned to keep the size distribution of the geoducks in all treatments the same at the start of the experiment (see associated post [here](https://shellytrigg.github.io/166th-post/)). 

So, ideally, we would want to find a way to calculate the growth rate of the geoducks based on the size distributions collected in the beginning and end of the experiement (Shelly has posted an [issue](https://github.com/RobertsLab/resources/issues/794) on Github to possibly find a solution to this). 

---

###Current Lab Work

Today, I have been looking online to possibly find a way to calculate growth rate based on the information we have. I have found a few sources that could possibly help us with this (at least as a starting point of some kind):

1. [Estimation of growth and mortality
parameters from size frequency distributions
lacking age patterns: the red sea urchin
(Strongylocentrotus franciscanus) as an
example](http://www.sfu.ca/biology/wildberg/smithbd/vb%20apps/Smith_et_al_(Size_Frequency_Analysis).pdf)
2. [Age- and size- dependent growth and mortality in a population of *Fucus distichus*](https://www.int-res.com/articles/meps/78/m078p173.pdf)
3. [Fitting growth models to length frequency data](https://academic.oup.com/icesjms/article/61/2/218/620849)
4. [Estimating Growth and Mortality in Steady-State Fish Stocks from Length-Frequency Data](https://pdfs.semanticscholar.org/c089/12c640acd9a7c4ed723314c84cd2aa0b650a.pdf)
5. [Comparative Performance of Three Length-Based Mortality Estimators](https://afspubs.onlinelibrary.wiley.com/doi/full/10.1002/mcf2.10027)
6. [Use of length-frequency data in the estimation of growth parameters of three Mediterranean fish species: bogue (*Boops boops* L.), picarel (*Spicara smaris* L.) and horse mackerel (*Trachurus trachurus* L.)](https://reader.elsevier.com/reader/sd/pii/0165783691900136?token=1AE90E046175EF664466CC4EB7B5D8CF45B7ECC2017B2B8B8C3485FECD8975ADDBAA64676EE40C09C22FB7D0070F24C1)

An equation that seemed to frequently occur when analyzing papers was the von Bertalanffy growth function (which could potentially be a start in formulating an equation?).

More time will have to be put in analyzing the papers and finding a viable equation to use that ultimately uses length measurement distribution as an indicator of growth rate, while also taking into consideration mortality.

