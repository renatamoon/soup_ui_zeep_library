# soup_ui_zeep_library


### WEB SERVICES IN PYTHON

How can we use it, what's the implementation of it, and why is this needed.

### HOW THE COMMUNICATION BETWEEN APPLICATIONS AND WEB SERVERS WORKS?

Imagine that we have an AMAZON WEB SERVICE and a Bank Server. When you do an online buy, and then you go to the payment area.
The Amazon application that is requesting the payment, then they need to check wheter the credit card information is valid or not. Then,
it will communicate with the Bank Server to check if the card information is valid or not. The Amazon application send the 
query to check if the credit card information  is in the bank server. The acknowlege will be sent to the bank server and the server
will send it to the Amazon application that is requesting the payment.

### WHAT IS A WSLD FILE?

Is a services description language and it's written in XML. Why XML? Because this is an universal language and it can communicate with 
two applications, and it must have a common language, that is XML. 

### PACKAGES TO BE INSTALLED

`pip3 install  zeep`

### HOW THE CLIENT AND OPERATION WORKS:

`from zeep import Client`

```
operation = Client('http://www.dneonline.com/calculator.asmx?WSDL')

add = getattr(operation.service, "Add")

print(add(10, 20))

```

### USEFULL LINKS:

- https://www.pycorners.com/stories - website containing a lot of usefull articles;
- https://docs.python-zeep.org/en/master/ - zeep documentation;
- http://www.dneonline.com/calculator.asmx - example of a wsld file and it's written in Java;
