##### Product microservice, purchases request messages are handled here
#### this is consumer to 'product' rabbitMq channel


import service
import bus

class ProductService(AbstractService):
	
	# override configure and start service calls
	
	def handle(self):
		print("Handling purchases")
	
	def configure(self):
		bus.SubscribeQueue('product', handle)
		
	def start(self):
		productChannel = bus.StreamQueue('product')