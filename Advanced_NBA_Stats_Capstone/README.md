![nba_stats_image_1](https://github.com/mateomartinez510/Springboard/blob/master/![nba_stats_image_1](https://github.com/mateomartinez510/Springboard/blob/master/Advanced_NBA_Stats_Capstone/images/nba_image_1.png)


# Predicting NBA Statistics with a Linear Regression Model

(switcht this image for first slide in slide deck, continuity) (also with rest of images for this readme, maybe finish the slide show first then just use some of those after, the slide deck should be more thorough and indepth than the readme, focus on the slide deck first!)

The goal of this project is to use Advanced NBA statistics from one season to predict a specific metric of player performance in the following season.
(maybe here explain why this project, usefulness to NBA managers/scouts at identifying talent, also with legalization of sports gambling and popularity of fanatasy sports, any sports enthusiast could benefit from a model that can predict player statistics in the future.)

#### #### add a general photo of nba as a cover photo #####

# Data

[NBA Advanced Stats](https://www.nba.com/stats/)

In 2013 the NBA began to use advances in camera technology to track and record more granular player statistics. Previously only about a dozen player statistics were tracked, such as number of rebounds per game and shooting percentage. Now with these advanced tracking systems, over 200 player metrics were now being recorded, such as player movement, proximity to defenders, to the number of times a defender touches a players elbow were now being tracked. I was interested to dive into this new and rich quantity of data to determine if there were new insights and correlations to be found, particularly in predicting player progression and improvement over time. For this project, I analayzed the data from the 2017-2018 season with goal of making a prediction for player performance in the following 2018-2019 season. The statistic I selected to predict was PIE (Player Impact Estimate), which is essential a calculation of what percent of game events did that player contrbute to the team (% of player PTS, RBS, ASTS, etc out of total team PTS, RBS, ASTS, etc). PIE is a great metric at comparing players across different positions, as it gives relatively equal weight between points, rebounds, assists, and blocks (the PIE formula is listed here: [glossary](https://www.nba.com/stats/help/glossary/#pie)

#### #### picture of nba.stats.com table? #####


# 1. Webscraping 
The data I was interested is hosted on the nba.com website, stored in a columnar table format. To extract this data for modeling purposes, I used a combination of Selenium and BeaufiulSoup to scrape the data from the website. The data I was interested was housed in 11 different paginated tables that I scraped and merged into one pandas dataframe containing data on 540 players and 124 features.

#### #### show image of data table and maybe some general summary stats and some basic bar graph #####


# 2. Data Cleaning
There was some redundance between the features, such as Assists being recorded multiple times between tables, or that the Draft Round can be deduced from the player's Draft Number. I also had to filter out players who did not play in the 2018-2019 season as the model would not have a method for dealing for exogenous factors such as retirement. The only other data cleaning required was some minor regular expression formatting changes.

#### #### some basic EDA graphs #####


# 3. EDA
In EDA, I focused analyzing an significant outliers and colinear variables, given that extreme cases of either of these could negatively affect model preformance. The outliers that I eventually filtered out from my analysis were only players that played less than four games in the 2018 season and had a PIE score of less than 1. Given the granularity of some of the advanced statistics, there was a high colinearity between a number of the features. To filter out the features that had high colinearity that did not contain unique information, I created correlation matrix and sorted for the values with the highest degree of correlation and dropped highly redudnant ones. Additionally in EDA, I noticed that none of the 124 features I scraped contained player postion. I could have gone back to the nba website, but I was curious as to the results of using a K-Nearest Neighbor algorithm to create my own player clusters instead. I analyzed 5, 10, and 14 group clusters and eventually used the 5 group cluster in my final model.

#### #### picture of Yeo-Johnson Transformation? #####


# 4. Pre-Processing
I noticed in EDA that not all of my data was normally distributed and for better model performance I used the Yeo-Johnson Transform to normalize the data distribution, which then I used Sklearn's StandardScaler to standardize the distribution as well. The only categorical data I kept in my final model was my player clusters I made, which here I converted into dummy variables.

#### #### Dataframe of Model Perfromance and Some Bar Graph of the same? #####

# 5. Model Training
I trained series of different algorithms for my predictions of my target variable PIE in the following season. The models I used were Statsmodels' OLS, Sklearn's Ridge, Lasso, Elastic Net, and Random Forest, as well as XGBoost. I scored my models based on which one had the lowest RMSE value. I used a basic grid search for hyper parameter tuning for the models that needed such tuning. The model with the lowest RMSE score with interpretable results was the Elatic Net algorithm. From here, I performed further hyperparameter tuning using a random grid search and Bayesian optimization. My best model results were with Elastic Net with Bayesian optizimation.

#### #### graph of subsets and coefficents df? #####


# 6. Model Analysis
In this notebook I analyzed the results of my best model. First I analyzed the most impactful coefficients. Unsuprisingly the previous season's PIE value was the most important cofficient, but after that 'DREB%',  'USG%', and 'FGM_5_9ft' were the next most important coefficients, which translate to defensive rebounding percentage, player ussage based on shots and turnovers, and short range field goal percentage. Next, I analyzed different subsets (players who changed teams, most improved players, bench players, underperforming players, etc) of the NBA players to see on which subset the model performed better or worse. The subset that the model performed the best were players who did not change teams between seasons, and the subset the with the lowest accuracy was players who showed the highest impovement between seasons. Overall the my regression model was more likely to predict players would show a regression towards the mean rather capture unique player progression such as rising superstars. The results of the model could still be beneficial at targeting young role players who have modest growth potential.

# 7. Next Steps
- The advanced stats on nba.com go back to 2013 and in the future I would like to add additional seasons into the training set to improve model performance and hopefully the additional data would better capture the unique progression and growth of superstar players. 

- In the future I would like to build this out into a Flask app where a user of the app could input a player's name and see that player's following season's predicted PIE score. Additionally, I would like the app user to be able to change what the target variable that the algorithm would predict. 

