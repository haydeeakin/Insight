# Insight
# Red Carpet in short
Red Carpet provides data insights about a director’s trajectory that have participated at Cannes, Berlin and Venice film festival for the past 70 years (1932-2017). It provides information on how features related to a director's trajectory can influence the probability of becoming a successful director using machine learning.

# Technical Summary
I utilized a supervised learning method, logistic regression, to classify filmmaker’s trajectory. Prior to achieve that and making sense of the data I created an index of director nomination which helped me to capture the relationship between the number of films done by each director and the number of nominations for every given year. This engineered feature was included in the final model.

The dataset has a heavy male bias (only 5% of all film directors for all three film festivals, over a course of 70 years, were female) and decided to not include gender in the final model. I validated the model by testing the train model on a random subset of 30% of all observations. The ideal situation, however, would be to test the model on a test set with information of new emerging directors.

This has two approaches that I would like to tackle in the near future. The first one includes: a) collecting information from emerging directors that have been able to screen their films and win awards at local film festivals; b) weighting the importance of the type of awards won/or nominations in the past for the new directors. A second approach would be to produce a data product based on natural language processing (sentiment analysis) using film plots and or scripts. This last idea is by far my most preferred type of project which I would like to work on eventually. I will keep you posted with it.  

# Context and Use case
A film festival receives an average of 5,000 film submissions per year. How festival organizers choose what films to screen is a daunting task in terms of time and costs. It requires 7,500 hrs of film previewing. At Insight, I used historical data of 4,600 film directors from Cannes, Berlin and Venice Film Festival to create a webapp based-report that facilitates film organizers to decide on what to screen based on filmmakers trajectory. It also provides insight to those early stage film directors wanting to increase their chances to be screen at prestigious film festivals.
