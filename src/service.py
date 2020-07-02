#### Abstract implementation for all submodules or "microservices" to be bootstraped by the main()

from abc import ABC , abstractmethod

class AbstractService(ABC):
	
	def __init__ (self):
		configure()
		start()
	
	def configure(self):
		pass
		
	def start(self):
		pass
		
	def stop(self):
		pass
		
		
	def handle(self):
		pass