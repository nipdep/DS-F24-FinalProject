### Report

---

### Experiment Setup - 1

#### Description:
The goal is to analyze the human population change in relation to the presence of oil or gas. Specifically, we aim to determine if there is an association between population migration patterns and oil or gas production changes.

---

#### **Method - 1**: Chi-Square Test

##### Setup:
1. Create a categorical feature column from the one-hot encoded 3 columns (for 2003 and 2013 population features).
2. Engineer a population type change feature by combining the two columns.
3. Build a contingency table (crosstab) between population change and oil or gas production change.
4. Run the Chi-Square test on the contingency table.

##### Results:
| Pop 3 to 13    | Metro to Metro | Metro to Nonmetro | Nonmetro to Metro | Nonmetro to Nonmetro |
|----------------|----------------|-------------------|-------------------|----------------------|
| Oil_Gas_Change |                |                   |                   |                      |
| 0              | 906            | 92                | 33                | 1626                 |
| 2              | 71             | 10                | 1                 | 129                  |
| 9              | 61             | 7                 | 1                 | 132                  |

- **Chi2 Statistic**: 4.08  
- **P-value**: 0.665  
- **Degrees of Freedom**: 6  

##### Result Analysis and Explanation:

- **Null Hypothesis (H0)**: There is no association between population change and oil presence (they are independent).  
- **Alternative Hypothesis (H1)**: There is an association between population change and oil presence (they are not independent).

The Chi-Square test result shows a Chi2 statistic of 4.08 with 6 degrees of freedom and a p-value of 0.665. Since the p-value is much greater than the significance level of 0.05, we fail to reject the null hypothesis. This suggests that there is no significant association between population change and oil or gas presence, and any observed differences are likely due to chance.  

**Conclusion**:  
Given this outcome, we conclude that in the given data, inter-state human migration is independent of natural resource (oil or gas) production improvements.

---

### Experiment Setup - 2

#### Description:
The focus is to analyze the association between county type and county population category. The goal is to understand whether the main income source of a county (e.g., farming, mining, recreation) is significantly related to population type (e.g., metro, micropolitan, non-metro).

---

#### **Method - 1**: Chi-Square Test

##### Setup:
1. Map county type categorization using the provided UUIC codes to ['metro', 'micropolitan', 'non-metro'] based on the documentation.
2. Build a contingency table (crosstab) between population category and county type.
3. Run the Chi-Square test on the contingency table.

##### Results:
| Pop_Cat                            | Metro | Micropolitan | Nonmetro |
|------------------------------------|-------|--------------|----------|
| County Type                        |       |              |          |
| Federal/State government-dependent | 93    | 111          | 203      |
| Manufacturing-dependent            | 101   | 108          | 292      |
| Mining-dependent                   | 18    | 27           | 176      |
| Nonspecialized                     | 504   | 234          | 499      |
| Recreation county                  | 74    | 57           | 202      |
| Farm-dependent                     | 21    | 33           | 390      |

- **Chi2 Statistic**: 435.14  
- **P-value**: 3.09e-87  
- **Degrees of Freedom**: 10  

##### Result Analysis and Explanation:

- **Null Hypothesis (H0)**: There is no association between county population category and county type (they are independent).  
- **Alternative Hypothesis (H1)**: There is an association between county population category and county type (they are not independent).

The Chi-Square test result shows a Chi2 statistic of 435.14 with 10 degrees of freedom and a p-value close to 0. Since the p-value is far below the significance level of 0.05, we reject the null hypothesis. This indicates a strong and statistically significant association between county population category and county type. The results suggest that the distribution of county types differs significantly across population categories.

---

#### **Method - 2**: Decision Tree Analysis

##### Description:
The goal is to examine how different county types influence the population categories and identify which county types have the strongest effect.

##### Setup:
1. One-hot encode the county type feature as the independent variable.
2. Encode the population category feature as the target variable.
3. Fit a decision tree model to predict the target feature.

##### Results:

**Accuracy Report**:
|                | Precision | Recall | F1-score | Support |
|----------------|-----------|--------|----------|---------|
| Nonmetro       | 0.66      | 0.72   | 0.69     | 355     |
| Micropolitan   | 0.00      | 0.00   | 0.00     | 106     |
| Metro          | 0.40      | 0.57   | 0.47     | 168     |
| Accuracy       | ---       | ---    | 0.56     | 629     |
| Macro avg      | 0.35      | 0.43   | 0.39     | 629     |
| Weighted avg   | 0.48      | 0.56   | 0.51     | 629     |

**Confusion Matrix**:
| ---  | ---  | --- |
| 255  | 0    | 46  |
| 60   | 0    | 46  |
| 72   | 0    | 96  |

##### Analysis:
The overall accuracy of 56% suggests that the model performs only slightly better than random prediction. However, the recall and precision scores indicate that the model struggles significantly, particularly with predicting the "micropolitan" class, where no predictions are made. This implies that the selected features are not sufficiently predictive for the target population category.

**Feature Importances**:
| Feature         | Importance |
|-----------------|------------|
| Farming         | 0.506848   |
| Mining          | 0.199280   |
| Recreation      | 0.113775   |
| Government      | 0.091891   |
| Manufacturing   | 0.088206   |

The most influential feature is `farming`, suggesting that counties with farming-dependent economies have the strongest relationship with population categories.

**Conclusion**:
Given the limited predictive performance, the target variable (population category) does not align well with the provided features. Thus, the focus shifts to a binary classification task—predicting population loss.

---

### Experiment Setup - 3

#### Description:
The goal is to predict population loss in 2015 based on county type features.

#### **Method - 3**: Decision Tree Analysis for Population Loss

##### Setup:
1. Use the county type features as independent variables.
2. Set the binary "population loss" feature as the target variable.
3. Split the data into training and testing sets (80%-20%).
4. Fit a decision tree model.

##### Results:

**Accuracy Report**:
|                | Precision | Recall | F1-score | Support |
|----------------|-----------|--------|----------|---------|
| 0.0 (No Loss)  | 0.87      | 0.92   | 0.90     | 520     |
| 1.0 (Loss)     | 0.48      | 0.35   | 0.40     | 109     |
| Accuracy       | ---       | ---    | 0.82     | 629     |
| Macro avg      | 0.68      | 0.63   | 0.65     | 629     |
| Weighted avg   | 0.80      | 0.82   | 0.81     | 629     |

**Confusion Matrix**:
| 479  | 41  |
| 71   | 38  |

##### Analysis:
The model achieves an overall accuracy of 82%, which is a significant improvement compared to the previous experiments. However, the recall for predicting "population loss" (1.0) is relatively low at 35%, indicating that the model struggles to identify counties experiencing population loss.  

**Feature Importances**:
| Feature               | Importance |
|-----------------------|------------|
| Farming               | 0.841072   |
| Retirement Destination| 0.077849   |
| Mining                | 0.062143   |
| Recreation            | 0.010779   |
| Government            | 0.007915   |
| Manufacturing         | 0.000243   |

Farming emerges as the most critical factor for predicting population loss, with retirement destinations and mining playing smaller but notable roles.

---

### Final Conclusion:
Across the experiments, the results indicate that **county type** strongly influences population characteristics, but the ability to predict population categories is limited with the given features. However, focusing on **population loss** yielded better predictive performance, with `farming` being the most influential factor. Further refinement of features or exploration of additional datasets may improve performance for future studies.