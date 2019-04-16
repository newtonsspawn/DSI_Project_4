import GetOldTweets3 as got
import codecs

tweet_list = []

tweetCriteria = got.manager.TweetCriteria()\
    .setSince("2017-08-27")\
    .setUntil("2017-09-24")\
    .setTopTweets(True)\
    .setNear("Cudjoe Key,Florida")\
    .setWithin("150mi")


outputFile = codecs.open("../data/hurricane_irma_tweets.csv", "w+", "utf-8")
outputFile.write(
    'username;;date;;retweets;;favorites;;text;;geo;;mentions;;hashtags;;id;;permalink'
)
print('Searching...\n')


def receiveBuffer(tweets):
    for t in tweets:
        outputFile.write(('\n%s;;%s;;%d;;%d;;"%s";;%s;;%s;;%s;;"%s";;%s' % (
        t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites,
        t.text, t.geo, t.mentions, t.hashtags, t.id, t.permalink)))
    outputFile.flush()
    print('%d more saved on file...\n' % len(tweets))


tweet = got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

outputFile.close()