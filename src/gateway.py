#### Load Balancing using Kubernetes Ingress service, this is very similar to other on-prmise providers such as DDI for example but for containers in our case
### Our Ingress Wide IP Adress that will help us with the TCP/HTTP load balancing would look something like this:  hello-world.us-south.containers.appdomain.cloud


## we need these modules so we can span new threads for every incoming HTTP connection, rember that HTTP runs over TCP stack thus connections are end-to-end all the time. 
import threading
import time
import uuid
import json
import bus
from flask import Flask, jsonify, request


class Gateway:
	
	app = Flask(__HttpRequestService__)
	bus = ''
	
	### the message after decompressing it (GZIP'd) and then deserializing (from Base64) it's actually a JSON payload coming from client app (an CLI command tool or an Web/Desktop UI)
	#### e.g.     {"ClientIP":"11.22.33.444", "ClientRegion":"EMEA", "ClientPort":8080,"ProductID":"77bef192-94b6-4579-b33f-40377eebffcf"}
	#### e.g. BASE64 = eyJDbGllbnRJUCI6IjExLjIyLjMzLjQ0NCIsICJDbGllbnRSZWdpb24iOiJFTUVBIiwgIkNsaWVudFBvcnQiOjgwODAsIlByb2R1Y3RJRCI6Ijc3YmVmMTkyLTk0YjYtNDU3OS1iMzNmLTQwMzc3ZWViZmZjZiJ9
	#### e.g GZIPd = H4sIAAAAAAAA/z3M3QqCMBgA0FdSF0GXqRnf2A/OOdnumoZsOgmsbD590EX3h3OPuLTXebaLwG0BR/CXD/EQiac78XXCClih+JvGdMPDZgfHHa5kq3Jw2wgTW2+deg1V/u6X2nE/brw8rzDn0WYi1Uhg8bt7pIMKVE6RyCnRXj9Z2SLepI7uLBBZb3TvkemUM8F44/DpC+HRf8KgAAAA
	
	messages = {
		"00000000-0000-0000-0000-000000000000": "H4sIAAAAAAAA/z3M3QqCMBgA0FdSF0GXqRnf2A/OOdnumoZsOgmsbD590EX3h3OPuLTXebaLwG0BR/CXD/EQiac78XXCClih+JvGdMPDZgfHHa5kq3Jw2wgTW2+deg1V/u6X2nE/brw8rzDn0WYi1Uhg8bt7pIMKVE6RyCnRXj9Z2SLepI7uLBBZb3TvkemUM8F44/DpC+HRf8KgAAAA"
		}
	
	def __init__ (self, busDriver):
		self.bus = busDriver
		StartHttpRequestProtocol()
		
	
	@app.route('/api/buy', methods=['POST'])
	def ListenPurchases(self):
		ListenHttpRequest('products')
	@app.route('/api/inventory', methods=['POST'])
	def ListenInventory(self):
		ListenHttpRequest('inventory')
	@app.route('/api/suppliers', methods=['POST'])
	def ListenSuppliers(self):
		ListenHttpRequest('suppliers')
	
	def ListenHttpRequest(self, queueName):	
		# Add into messages temporaly (this gives us O(1) constant time complexity, very fast write. Eventually we dequeue from it and push into an external message middle (i.e. RabbitMQ)
		### here were create the MessageId automatically and pass the encryoted data as value in the Map/dictionary
		
		messages[str(uuid.uuid4())] = request.get_json(force=True)[1] 
		
		for(m_key, m_val in messages.items())
		{
			# Push into RabbitMQ as is - we let the microservice do the decompression & deserialization of the message - this way we make it async and avoid suffering DDoS attacks. Worst case scenario, we scale-out consumers in Kubernetes to deal with high load. But won't cause thread starvation or excesive context switching in the microservice
			busDriver = Bus.EnqueueMessage(queueName, m_val)
			messages.pop("m_key")   # flush the in-memory map so we keep the gateway service lightweight 
		}
		
		time.sleep(.9)  # let's throttle 0.9 seconds before disposing the thread and hndling another incoming message to make sure the OS returns the connection to the pool (Linux or Windows have TCP pools and try to reuse as much as possible)   
	
	def StartHttpRequestProtocol(self):
		app.run(host='0.0.0.0', debug=True)
		threading.Thread(target=ListenPurchases).start()
		threading.Thread(target=ListenInventory).start()
		threading.Thread(target=ListenSuppliers).start()
		