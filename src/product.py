##### Product microservice, purchases request messages are handled here
#### this is consumer to 'product' rabbitMq channel


import service
import bus
import base64
import gzip

class ProductService(AbstractService):
	
	# override configure and start service calls
	
	def handle(self, ch, method, properties, body):
		print("Handling purchase" + base64.b64decode(gzip.decompress(str(body))))
	
	def configure(self):
		bus.SubscribeQueue('product', handle)
		
	def start(self):
		productChannel = bus.StreamQueue('product')