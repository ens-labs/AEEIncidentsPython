from suds.client import Client
aee_url = 'http://wss.prepa.com/services/BreakdownReport?wsdl'
aee_client = Client(aee_url)

towns = aee_client.service.getBreakdownsSummary()

print "Here is a list of the towns with breakdowns: "
for town in towns:
	print town.r1TownOrCity

print "Enter the town name to see the breakdowns: "
town = raw_input()

averias = aee_client.service.getBreakdownsByTownOrCity(town.upper())
for averia in averias: 
	print "***************************************"    
	print "Pueblo: " + averia.r1TownOrCity
	print "Area: " + averia.r2Area
	print "Status: " + averia.r3Status
	print "Last Update: " + averia.r4LastUpdate
	print "***************************************"