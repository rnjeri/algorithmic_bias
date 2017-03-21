# Machine Bias

## Business Understanding
This project has two scopes. The first one is to arrive at an estimate of the true cost of incarceration, and the second is to come up with a precise and sensitive way to predict recidivism. The end goal is to create a cost benefit analysis for the Post Prison Education Program that shows how investment in PPEP could ultimately lower the total cost of incarceration by lowering recidivism rates, but also by providing skills and social networks that are lost while one is incarcerated.

Recidivism prediction isn't a new field of study. There are researchers who have developed risk assessment tools that estimate the probability that a person will reoffend. These tools are used at all levels of the justice system from pre-trial to sentensing. However, a study by prorepublica found that while these models have an accuracy score of 71%, they output a lot higher False Positives for African Americans and False Negatives for whites when it comes to prediciting the likelihood of someone to commit a violent crime in the future. The prorepublica study found that the model has a lot more false positives, 44.9% for African Americans, compared to 23.5% for whites. At the same time, the algorithm has a 47.7% False Negative rate for whites compared to a 28.0% False Negative rate for blacks. 

Use of a faulty algorithm in the justice system results in a misallocation of resources by identifying as high risk people who aren't high risk and vice versa.

Can an algorithm that predicts recidivism and risk levels with higher precision and recall be built?


## Cost of Incarceration
What is the true cost of incarceration?
    -How can better predictions of the rate of recidivism affect the cost of incarceration?
    -How can investment in PPEP and similar programs impact recidivism, and consequently, the cost of incarceration?
What features are most correlated with recidivism?

## Data Understanding
The data set is very small.

## Building Better Prediction Models
- How do we prevent bias from leaking into the prediction models while so many factors considered to be predictors are correlated with race?
- The original recidivism prediction models were done using random forest classifiers. I used gradient boosting classifiers which have a higher accuracy on the test data than the random forest classifiers. 

## Deployment
- A web app that predicts recidivism probability given the profile of a person. A user can input data for each of the features that were used in creating the model. The goal is that with access to more data, the precision of the model can be improved to provide more accurate recidivism predictions. 