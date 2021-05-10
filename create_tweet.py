from sentiment_analysis import mainFunction
import twitter_credentials
import sys
from twython import Twython
from csv import writer

def append_list_as_row(file_name, data_list):
	with open(file_name, 'a+', newline='') as write_obj:
		csv_writer = writer(write_obj)
		csv_writer.writerow(data_list)


positive, neutral, negative, generalOpinion, yesterday = mainFunction(100)

titleText = "Here are the sentiment analysis statistics of one hundred tweets containing #COVID19 from " + str(yesterday) + ":"
generalOpinionText = "The overall general opinion has a value of: %s " % str(generalOpinion)
positiveText = "Number of positive tweets: %s" % str(positive)
neutralText = "Number of neutral tweets: %s" % str(neutral)
negativeText = "Number of negative tweets: %s" % str(negative)

#Create a copy of the Twython object with all our keys and secrets to allow easy commands.
#api = Twython(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET,twitter_credentials.ACCESS_KEY,twitter_credentials.ACCESS_SECRET) 

#Using our newly created object, utilize the update_status to send in the text passed in through CMD
#api.update_status(status = titleText + "\n"+ generalOpinionText + "\n"+ positiveText + "\n"+ neutralText + "\n"+ negativeText)

tweet_data = [yesterday, generalOpinion, positive, neutral, negative]

append_list_as_row('tweet_data.csv',tweet_data)