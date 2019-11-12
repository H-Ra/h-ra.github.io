---
layout: post
title: November 12, 2019 - Juvenile Geoduck Data Analysis
---

Since I have completed all of the geoduck measurements on ImageJ and have put them all in the [shell length google spreadsheet](https://docs.google.com/spreadsheets/d/1Y75kqmWWuAink48U4vHjgaEWLgbKEyJRrspbAxzW3jc/edit#gid=1208042429) (refer to my [last post](https://h-ra.github.io/1-firstpost/)), I will begin analyzing this data with Shelly using R. 

---

### Goals of the Day
1. Refamiliarize myself with R 
2. Begin doing juvenile geoduck data analysis with Shelly
3. Find a way to link posts from my notebook to the collective [Genefish wordpress site](https://genefish.wordpress.com/). 

---

### Current Lab Work

__*R Review*__

Although I have used R in the past, I am refreshing my memory on R by looking up R tutorials [online](http://web.cs.ucla.edu/~gulzar/rstudio/basic-tutorial.html). I have refreshed my memory on: 

1. Importing files
2. Doing basic statistical analyses (such as finding the mean, median, standard deviation, etc...)
3. Creating basic graphs (scatter plots and histograms)

Here is an example of a histogram that I created:

![20191112_LengthHistogramExample.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20191112_LengthHistogramExample.png?raw=true)

__*Juvenile Geoduck Data Analysis*__

I worked with Shelly to analyze the juvenile geoduck shell measurements by working on a script in R. I learned how to compile an excel document with multiple tabs into one data file as well as create complex graphs and analyze the statistical significance of the data collected (The script that we worked together can be found [here](https://github.com/shellytrigg/P_generosa/blob/master/amb_v_varlowpH_juvis/analyses/20191018_ShellLength/20191018_ShellLength.R))!

We created several different graphs together using ggplot2, but the type of plot we decided to use in the end was a density plot showing the 4 different treatments in different colors (as seen below): 

![Density Plot of Experimental Groups.jpeg](https://github.com/shellytrigg/P_generosa/blob/master/amb_v_varlowpH_juvis/analyses/20191018_ShellLength/Density%20Plot%20of%20Experimental%20Groups.jpeg?raw=true)

We noticed that the geoduck that were in the var.low parental and the var.low current treatment (the purple graph) had the highest density of the longest shell lengths, which is surprising since I had assumed that the geoducks grown in the low pH conditions would have mostly smaller shells. So, a possible next step could be to find a way to see the growth rate of geoducks in the treatment conditions by comparing start and end size distributions (Shelly created an [issue](https://github.com/RobertsLab/resources/issues/794) to get some input on finding a way to do this).

__*Linking Journal Posts to Genefish Wordpress*__ 

I still haven't found a way to connect my journal posts to the Genefish wordpress, so I have created an [issue](https://github.com/RobertsLab/resources/issues/795) to find out if there is a way to do this. 















 

