from suds.client import Client
aee_url = 'http://wss.prepa.com/services/BreakdownReport?wsdl'
aee_client = Client(aee_url)

towns = aee_client.service.getBreakdownsSummary()

for town in towns:
    averias = aee_client.service.getBreakdownsByTownOrCity(town.r1TownOrCity)
    for averia in averias: 
    	print "***************************************"    
        print "Pueblo: " + averia.r1TownOrCity
        print "Area: " + averia.r2Area
        print "Status: " + averia.r3Status
        print "Last Update: " + averia.r4LastUpdate
        print "***************************************"

