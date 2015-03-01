from suds.client import Client
aee_url = 'http://wss.prepa.com/services/BreakdownReport?wsdl'
aee_client = Client(aee_url)

towns = aee_client.service.getBreakdownsSummary()

print "Here is a list of the towns with breakdowns: "
for town in towns:
	print town.r1TownOrCity

print "Enter the town name to see the breakdowns: "
town = raw_input()

breakdowns = aee_client.service.getBreakdownsByTownOrCity(town.upper())
for breakdown in breakdowns: 
	print "***************************************"    
	print "Pueblo: " + breakdown.r1TownOrCity
	print "Area: " + breakdown.r2Area
	print "Status: " + breakdown.r3Status
	print "Last Update: " + breakdown.r4LastUpdate
	print "***************************************"