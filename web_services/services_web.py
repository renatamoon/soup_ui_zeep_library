# FIRST WEB SERVICE CONNECTION
from zeep import Client

operation = Client('http://www.dneonline.com/calculator.asmx?WSDL')

add = getattr(operation.service, "Add")

print(add(10, 20))
