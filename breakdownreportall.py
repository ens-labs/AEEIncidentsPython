from suds.client import Client
aee_url = 'http://wss.prepa.com/services/BreakdownReport?wsdl'
aee_client = Client(aee_url)

towns = aee_client.service.getBreakdownsSummary()

for town in towns:
    breakdowns = aee_client.service.getBreakdownsByTownOrCity(town.r1TownOrCity)
    for breakdown in breakdowns: 
    	print "***************************************"    
        print "Pueblo: " + breakdown.r1TownOrCity
        print "Area: " + breakdown.r2Area
        print "Status: " + breakdown.r3Status
        print "Last Update: " + breakdown.r4LastUpdate
        print "***************************************"