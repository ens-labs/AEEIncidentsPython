import twitter
from suds.client import Client
aee_url = 'http://wss.prepa.com/services/BreakdownReport?wsdl'
aee_client = Client(aee_url)

twitterApi = twitter.Api(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token_key = ACCESS_TOKEN,
                         access_token_secret = ACCESS_TOKEN_SECRET)

towns = aee_client.service.getBreakdownsSummary()

for town in towns:
    averias = aee_client.service.getBreakdownsByTownOrCity(town.r1TownOrCity)
    for averia in averias: 
		tweet = "@AEEONLINE tienes averia en: " + averia.r1TownOrCity ", " + averia.r2Area + ", Status: " + averia.r3Status
		twitterApi.PostUpdate(tweet)

