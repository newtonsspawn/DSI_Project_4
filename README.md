## PROBLEM STATEMENT

With increasing levels of climate change, disasters have been happening more and more frequently over the years. However, government response times have not been able to keep parity, as evidenced by how areas were handled in the wake of Hurricanes Katrina and Maria, affecting Louisiana and Puerto Rico respectively. While official sources like USGS are still useful resources for informing the people regarding natural disasters, social media may be able to offer its’ own unique value of information. As a result, we want to harness the power and influence of social media, in our case Twitter, to effectively and efficiently alert people in the event of a natural disaster. Ultimately, our goal is to design and implement an app that will be able to alert users for all disaster events, as close to real time by utilizing Twitter activity to identify these events and notify people when an event first occurs.



## DATA ACQUISITION

We decided to focus on three types of disasters: hurricanes, earthquakes, and wildfires. Using the open-source GetOldTweets3, we then acquired data for Hurricane Harvey, Hurricane Irma, Hurricane Maria, the 2011 North Bay earthquake, the 2014 Prague, Oklahoma earthquake, the Carr fire, the Woolsey Fire, and the Camp Fire dating from a week predisaster to the disaster and from the disaster to a week postdisaster.   

## EDA

We were able to scrape 31423 predisaster tweets and 67127 postdisaster tweets. We used custom list of disaster related words to classify post disaster tweets as disaster related or not and automatically classified all of the predisaster tweets as nondisaster related. Of the postdisaster tweets, 22320 were disaster related. Thus, 33 percent of the postdisaster tweets were disaster related and 22.5 percent of the total tweets were disaster related.  

Our initial attempts to analyze the wildfire data was complicated by the fact that there were shootings at the same time  and roughly the same geographic location as the wildfires. To resolve this problem, we created a custom list of stopwords that would help us filter out any shooting related keywords, using word2vec to help us find similar words and phrases. However, once we removed any shooting related keywords, the accuracy of our models increased. 

## MODELS

We initially ran 3 models to analyze our text corpus: Latent Dirichlet Allocation, Principal Component Analysis, and Singular Value Decomposition.The naive model, or predicting the most dominant class 100 percent of the time, would give a correct result 77 percent of the time.  Our results when we ran SVD were 0.99 train and 0.94 test. When we ran PCA it was 0.81 train and 0.81 test. When we ran LDA it was 0.77 train and 0.77 test. After some hyperparameter tuning and refinement of stopwords, we managed to improve PCA to 0.9 train and 0.9 test, and LDA to 0.8 train and 0.8 test. However, since SVD  had the best test results, we to chose to use it as our production model. Additionally, we chose to use Random Forest to classify, as it would help us deal with the imbalance of our classes without upsampling or downsampling. 


## Conclusion

In conclusion, we believe that moving forward with Singular Value Decomposition and Random Forest classification is the correct way to go. Additionally, we should broaden our search terms to look for more types of disasters, and hire foreign language speakers so that we can search for disaster posts in non-English languages. If possible, we should also broaden to different social media platforms such as Weibo or Facebook in order to have better coverage. Care should also be taken to reinforce communications infrastructure such as landlines and cell towers. 
