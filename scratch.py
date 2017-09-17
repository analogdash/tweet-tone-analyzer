#Service Name: Tone Analyzer for Tweets test

#Credential Name: testacct_toneanalyzer

#endpoint = "https://gateway.watsonplatform.net/tone-analyzer/api/v3"

from pyexcel_xls import get_data
from watson_developer_cloud import ToneAnalyzerV3
import datetime

tone_analyzer = ToneAnalyzerV3(
    version='2016-05-19',
    username='#REDACTED',
    password='#REDACTED'
)

data = get_data("shortlist.xls")

judgedtweets = []

for row in data['Sheet1']:
	tone_analyzer = ToneAnalyzerV3(
        version='2016-05-19',
        username='#REDACTED',
        password='#REDACTED'
    )
    time = row[0]
    tweet = row[1]
    result = tone_analyzer.tone(tweet)
    item = {'timestamp':time,'content':tweet,'analysis':result}
    judgedtweets.append(item)


text_file = open("Output.txt", "w")
text_file.write(json.dumps(judgedtweets))
text_file.close()
