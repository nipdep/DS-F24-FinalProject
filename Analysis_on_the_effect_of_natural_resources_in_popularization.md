  ## Analysis on the effect of the natural resource in the human population change 

### Feature analysis

#### 2003 County type labels
- Metro2003 
- Micropolitan2003
- Nonmetro2003
- NonmetroAdj2003  <Nonmetro, adjacent to metro area, 2003>
- NonmetroNotAdj2003
- UrbanInfluenceCode2003
- RuralUrbanContinuumCode2003

#### 2013 County type labels
- Metro2013
- Micropolitan2013
- Nonmetro2013
- Metro_Adjacent2013 <Nonmetro, adjacent to metro area, 2013>
- ...
- UrbanInfluenceCode2013
- RuralUrbanContinuumCode2013

#### Natural resource features
- HiAmenity
- Gas_Change [2000-2011]
- Oil_Gas_Change [2000-2011]
- Oil_Change [2000-2011]

---
#### Rural-Urban Continuum Code (RUCC) 2003
The Rural-Urban Continuum Codes categorize counties based on the size of their urban population and their metro/nonmetro status. The RUCC places a stronger focus on population density than proximity to metro areas.

##### Metro counties
- Code 1: Counties in metro areas with a population of 1 million or more.
- Code 2: Counties in metro areas with a population of 250,000 to 1 million.
- Code 3: Counties in metro areas with fewer than 250,000 people.
##### Nonmetro counties
- Code 4: Urban population of 20,000 or more, adjacent to a metro area.
- Code 5: Urban population of 20,000 or more, not adjacent to a metro area.
- Code 6: Urban population of 2,500 to 19,999, adjacent to a metro area.
- Code 7: Urban population of 2,500 to 19,999, not adjacent to a metro area.
- Code 8: Completely rural or less than 2,500 urban population, adjacent to a metro area.
- Code 9: Completely rural or less than 2,500 urban population, not adjacent to a metro area

---

#### Urban Influence Code (UIC) 2013

##### Metro counties
- Code 1: Large metro areas with a population of 1 million or more.
- Code 2: Small metro areas with a population of less than 1 million.

##### Nonmetro, micropolitan counties (with urban population between 10,000 and 49,999)
- Code 3: Micropolitan counties adjacent to large metro areas.
- Code 4: Micropolitan counties adjacent to small metro areas.
- Code 5: Micropolitan counties not adjacent to metro areas.

##### Nonmetro, noncore counties (with an urban population of less than 10,000)
- Code 6: Noncore counties adjacent to large metro areas.
- Code 7: Noncore counties adjacent to small metro areas.
- Code 8: Noncore counties adjacent to micro areas.
- Code 9: Noncore counties not adjacent to metro or micro areas, with a town of at least 2,500 people.
- Code 10: Noncore counties not adjacent to metro or micro areas, without a town of at least 2,500 people.
- Code 11: Noncore counties not adjacent to large metro areas, with a town of at least 1,000 but fewer than 2,500 people.
- Code 12: Noncore counties not adjacent to metro areas, with no town of more than 1,000 people.

---

#### Natural Oil and Gas 
The "Change in the value of onshore natural gas production, 2000-11" with categories [0, 2] likely indicates two distinct levels or statuses of change in natural gas production value in onshore regions within that timeframe. Here’s what these values typically represent:

1. Code 0: Indicates no significant change or no production of onshore natural gas within the 2000–2011 period. Counties with this code may not have produced natural gas or did not see a notable increase or decrease in production value during this timeframe.

2. Code 2: Denotes moderate or significant increase in the value of natural gas production. Counties with this code likely experienced growth in natural gas production or value, possibly due to new drilling technologies, increased demand, or economic incentives that led to expanded extraction.

3. Code 9: Typically used as a code for data not available, suppressed, or not applicable. This may apply to counties where data on natural gas production was not collected, where production was minimal and thus not recorded, or where data was omitted to protect proprietary information.

## Feature engineering

1. Build a categorical feature on RUCC 2003 /2013 codes, then it is easier to analyze.
2. Build another set of catagories on code transition between 2003-2013
3. create a single feature on natural resource change in 2000-2011 

## Modeling 

### Analyze relationship between county type change and natural resource appearance  

#### Model-1 : Analyze by distribution shift with natural resources
> ideally we would use a ANOVA or two-tail t-test to analyze the behaviour 
However, since all features that we are interested in being categorical, we plan to use chi-square test.

#### Model-2 : Test for significance of the effect factor 
> ideally we would use linear regression and test for parameter coffience and p-values of those.
However, here we are planing to use decision tree and planing to use decision boundaries and information gain factor analyze the effect

#### Model-3 : Test for the causality 
> ideally we would use difference-in-difference test
However, since we don't have control/pitol staged data up-front, plan is to go with propensity based method first and then to DiD on top of it.

## Report

### Experiment setup -1 : 
Description : here we are trying to analyze the human population difference best on the oil or gas presence differnce. 

#### Method -1 : Chi-square test

> setup 
* create a categorical feature column from the one-hot encoded 3 columns
* do the above process for 2003 population features and 2013 population features 
* then engineer population type change feature by combining to columns
* build a contigency table / crosstab between population change and oil or gas production change
* run the chi-square test on the build crosstab

> results 

| Pop 3 to 13    | Metro to Metro | Metro to Nonmetro | Nonmetro to Metro | Nonmetro to Nonmetro |
|----------------|----------------|-------------------|-------------------|----------------------|
| Oil_Gas_Change |                |                   |                   |                      |
| 0              | 906            | 92                | 33                | 1626                 |
| 2              | 71             | 10                | 1                 | 129                  |
| 9              | 61             | 7                 | 1                 | 132                  |



Chi2: 4.08297353494696
P-value: 0.6654487632303545
Degrees of Freedom: 6

> result analysis and explanation 

Null Hypothesis (H0): There is no association between population change and oil presence (they are independent).
Alternative Hypothesis (H1): There is an association between population change and oil presence (they are not independent). 


The Chi-Square test result shows a Chi2 statistic of 4.08 with 6 degrees of freedom and a p-value of 0.665. Since the p-value (0.665) is much greater than the typical significance level of 0.05, we fail to reject the null hypothesis. This suggests that there is no significant association between population change and oil presence in this data, meaning that any observed differences are likely due to chance, and the variables are statistically independent.


__Since we our assumption is wrong in here we conclude the current experiment stating that in the give data, inter-state human migration is independent from the natural resource (oil, gas) production improvements.__

### Experiment setup -2: 
Now we are trying to analyze the association between county type and county population to analyze the whether there is a significant relationship between main income source of a county with the population. 

We analyze for 6 county types: 
* Farming
* Manufacturing
* Mining
* Government
* Recreation
* Retirement Destination

#### Method -1 : chi-square test

> setup 
* Since we have UUIC categorization of the county in this setting, we had to map UUIC code to ['metro', 'micropolitant', 'non-metro'] following the UUIC documentation 
* Name map on population category column and county type column
* * build a contigency table / crosstab between population category and county type
* run the chi-square test on the build crosstab

> results 

| Pop_Cat                            | Metro | Micropolitan | Nonmetro |
|------------------------------------|-------|--------------|----------|
| Category_type                      |       |              |          |
| Federal/State government-dependent | 93    | 111          | 203      |
| Manufacturing-dependent            | 101   | 108          | 292      |
| Mining-dependent                   | 18    | 27           | 176      |
| Nonspecialized                     | 504   | 234          | 499      |
| Recreation county                  | 74    | 57           | 202      |
| farm-dependent                     | 21    | 33           | 390      |

Chi2: 435.1355024983539
P-value: 3.0882621861617907e-87
Degrees of Freedom: 10

> result analysis and explanation 

Null Hypothesis (H0): There is no association between county population category and county type (they are independent).
Alternative Hypothesis (H1): There is an association between county population category and county type (they are not independent). 

The Chi-Square test result shows a Chi2 statistic of 435.14 with 10 degrees of freedom and a p-value of 3.09e-87 (essentially 0). Given that the p-value is far below the significance level of 0.05, we reject the null hypothesis. This indicates a strong and statistically significant association between county population category and county type, suggesting that the distribution of county types is meaningfully different across population categories and not due to chance.

#### Method -2: 
Description: Here the idea is to analyze further from seen association to check how different county types would effects the population could and what county type has what effect the counties population.

> setup 
* first we one-hot encode the county type feature to consider that as the independent variable 
* then we get encoded county population type as the target feature 
* fit a decision tree model, on selected independent to predict the target feature.

> results 
> First check for the model performance to understand where selected independent features are related enough to generate good target predictions.

__Accuracy report__

| | precision  |  recall | f1-score |  support    |
|--------------|----------|---------|--------------|--------|
|     Nonmetro   |    0.66   |   0.72   |   0.69    |   355 |
| Micropolitan   |    0.00   |   0.00   |   0.00    |  106 |
|        Metro   |    0.40   |   0.57   |   0.47    |   168 |
|     accuracy   |           |          |   0.56    |   629 |
|    macro avg   |    0.35   |   0.43   |   0.39    |   629 |
| weighted avg   |    0.48   |   0.56   |   0.51    |   629 |

__Confusion matrix__
| --- | --- | --- |
| 255 | 0   | 46  | 
| 60  | 0   | 46  |
| 72  | 0   | 96  |

> result analysis & explanation 

Overall accuracy is 59% implies that the performance is slightly better than the random prediction model. 
However, when we checking the performance in class-level it is shown that trained model haven't any prediction on `micropolitant` class. 
Therefore, this performance implies that the current feature set in use is not related to the city population size, even though there is a 
categorical data correlation between the classes.

> results 

Feature Importances:

|      Feature  | Importance |
| ---           |  ---       |
|      Farming  | 0.506848   |
|       Mining  |  0.199280  |
|   Recreation  |  0.113775  |
|   Government  |  0.091891  |
|Manufacturing  |  0.088206  |

> results analysis and explanation 

Even though the results are too low, the expected feature importance are high, and empirically `farming` of status of the state is most deteministic factor in the deciding 
county population type. 

__Based on the results it is evident that modeling for city population category prediction is considerably challenging task with the interested features. 
Therefore, we had to divert the target from population category to population loss in 2015 in the dataset, and this is a binary feature.__

#### Method -3:
Since, the target as county population type is not that supportive in predictive modelling we divert the predictive modeling to predict on `population loss`
base on county categories. 

> setup 
* Filter out 2015 county main income type categorization features as before and the county population loss binary feature
* Like in the previous modeling process set county type features as the models' independent features and county population loss as the target feature. 
* Split the dataset into train-test with 80%-20% 
* Fit the decision tree model

> results 

__Accuracy report__

| | precision  |  recall | f1-score  | support |
| --- | --- | --- | --- | --- | --- |
| 0.0    |   0.87   |   0.92   |   0.90   |    520 |
| 1.0     |  0.48   |   0.35   |   0.40   |    109 |
| accuracy   |   --- | --- |                 |  0.82   |    629 |
| macro avg   |    0.68  |    0.63   |   0.65   |    629 |
| weighted avg  |     0.80   |   0.82   |   0.81   |    629 |

__Confusion matrix__
| 479 |  41 |
| 71 | 38 |

> result analysis and explanation

Overall performance is decent. ...


> results 

__feature importance__

| Feature | Importance |
| --- | --- |
|  Farming  |  0.841072 |
| Retirement Destination  |  0.077849 |
| Mining  |  0.062143 |
| Recreation |   0.010779 |
| Government |   0.007915 |
|  Manufacturing  |   0.000243 |

> result analysis and experiment 

farming and ...