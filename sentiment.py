from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import sys


numLinesA = 0
numLinesB = 0
collectiveA = 0
collectiveB = 0
AverageScoreA = 0
AverageScoreB = 0

try:
    with open(r'C:\Users\JackC\PycharmProjects\MMUProject\MUFCvLPOOL.txt', 'r')as a, \
            open(r'C:\Users\JackC\PycharmProjects\MMUProject\LPOOLvMUFC.txt', 'r') as b:
        tweetsA = a.read()
        tweetsB = b.read()
        sentiment_scoreA = TextBlob(tweetsA)
        for sentence in sentiment_scoreA.sentences:
            numLinesA += 1
            collectiveA = collectiveA + sentiment_scoreA.polarity
        #print("Collective = ", collectiveA)
        averageA = collectiveA / numLinesA
        teamAFinal = round(averageA, 3)
        print("Average of Team A = ", teamAFinal)
        sentiment_scoreB = TextBlob(tweetsB)
        for sentence in sentiment_scoreB.sentences:
            numLinesB += 1
            collectiveB = collectiveB + sentiment_scoreB.polarity
        #print("Collective = ", collectiveB)
        averageB = collectiveB / numLinesB
        teamBFinal = round(averageB, 3)
        print("Average of Team B = ", teamBFinal)


except IOError as e:
    print('Failed %s' % e.strerror)

