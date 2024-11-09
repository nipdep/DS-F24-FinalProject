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


