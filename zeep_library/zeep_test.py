import zeep
from zeep import Client


wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)

print(client.service.Method1('Zeep', 'is cool'))
