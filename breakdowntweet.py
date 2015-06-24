import twitter
from suds.client import Client
aee_url = 'http://wss.prepa.com/services/BreakdownReport?wsdl'
aee_client = Client(aee_url)

twitterApi = twitter.Api(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token_key = ACCESS_TOKEN,
                         access_token_secret = ACCESS_TOKEN_SECRET)

towns = aee_client.service.getBreakdownsSummary()

print "Here is a list of the towns with breakdowns: "
for town in towns:
	print town.r1TownOrCity

print "Enter the town name to tweet the breakdowns: "
town = raw_input()

breakdowns = aee_client.service.getBreakdownsByTownOrCity(town.upper())
for breakdown in breakdowns: 
	tweet = "@AEEONLINE tienes averia en: " + breakdown.r1TownOrCity ", " + breakdown.r2Area + ", Status: " + breakdown.r3Status
	twitterApi.PostUpdate(tweet)