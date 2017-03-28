# Algorithmic Bias
"A vetted methodology for avoiding discrimination against protected attributes in machine learning is lacking." -Hardt, Price, Srebro (Equality of opportunity in supervised learning.)

## How I Found Myself Here
I found myself here accidentally on purpose. I began this project as a volunteer for the Post Prison Education program which aims to reduce recidivism among former inmates.Once I had access to the data, the first thing I did was create a recidivism prediction model, with the aim of showing reduced recidivism rates against the general population. After I had developed a terribly performing model due to data limitations, I discovered that the existing recidivism prediction models are critiqued for their inherent bias. Why is an algorithm that has a racially disparate impact implemented in the judicial system? Why can't these algrothims be improved to correct bias? I discovered that there are not only disparate accuracy models for black versus white individuals, but also for black versus white neighborhoods. Heat maps produced by PredPol increase policing of black neighborhoods.

## Business Understanding
This project has two scopes. The first one is to arrive at an estimate of the true cost of incarceration, and the second is to come up with a precise and sensitive way to predict recidivism. The end goal is to create a cost benefit analysis for the Post Prison Education Program that shows how investment in PPEP could ultimately lower the total cost of incarceration by lowering recidivism rates, but also by providing skills and social networks that are lost while one is incarcerated.

Recidivism prediction isn't a new field of study. There are researchers who have developed risk assessment tools that estimate the probability that a person will reoffend. These tools are used at all levels of the justice system from pre-trial to sentensing. However, a study by prorepublica found that while these models have an accuracy score of 71%, they output a lot higher False Positives for African Americans and False Negatives for whites when it comes to prediciting the likelihood of someone to commit a violent crime in the future. The pro publica study found that the model has a lot more false positives, 44.9% for African Americans, compared to 23.5% for whites. At the same time, the algorithm has a 47.7% False Negative rate for whites compared to a 28.0% False Negative rate for blacks.

Use of a faulty algorithm in the justice system results in a misallocation of resources by identifying as high risk people who aren't high risk and vice versa. Can an algorithm that predicts recidivism and risk levels with higher precision and recall be built?

"What they additionally need to do is to measure accuracy within different subgroups. Wildly differing performance across different groups of the population can indicate a problem... Indeed, some observers have called on the organizations that write and use algorithms to be more transparent in terms of clearly spelling out the data collected, identifying which pieces of data are used in the algorithm, and disclosing how this data is weighted or used in the algorithm. Such insights may help to pinpoint areas of discrimination that may not be apparent otherwise."

## Cost of Incarceration
What is the true cost of incarceration?
    -How can better predictions of the rate of recidivism affect the cost of incarceration?
    -How can investment in PPEP and similar programs impact recidivism, and consequently, the cost of incarceration?
What features are most correlated with recidivism?

## Data Understanding & Methodolody
The first thing I needed to acknowledge about the data is that it is not representative of racial proportions in Washington state. I realized that the data set was a self selected group who had opted to apply to the Post Prison Education Program with the goal of changing their lives.
I tried to be very conscious of the effect the data set would have on the trained predictive algorithm. I wanted to understand the difference in recidivisms for each demographic that was represented in the data. After reading about what caused the disparate error rates in the recidivism prediction models, it seemed that training the entire population while ignoring the disparity in recidivism rates for different demographics led to creation of a biased model.

## Building Better Prediction Models
- How do we prevent bias from leaking into the prediction models while so many factors considered to be predictors are correlated with race?
- The original recidivism prediction models were done using random forest classifiers. I used gradient boosting classifiers which have a higher accuracy on the test data than the random forest classifiers.
- The goal is that with access to more data, the precision of the model can be improved to provide more accurate recidivism predictions.

## Deployment
- The model is deployed as an empathy building tool in the form of a web app where users can input their features, and receive an output of their predicted probability to commit a violent crime, and their probaility to recidivate in the future. The app also gives alternative predictions if a person was from another race.

### Resources and Further Reading
- [Machine Bias:](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)There’s software used across the country to predict future criminals. And it’s biased against blacks.
- [How Pro Publica Analyzed the COMPAS Recidivism Algorithm](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm)
- [Equality of Opportunity in Supervised Learning](https://arxiv.org/pdf/1610.02413.pdf)
- [Google's algorithm] (http://www.independent.co.uk/life-style/gadgets-and-tech/news/googles-algorithm-shows-prestigious-job-ads-to-men-but-not-to-women-10372166.html) shows prestigious job ads to men, but not to women.





