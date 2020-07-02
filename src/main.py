from flask import Flask
import gateway
import bus
import dal


if __name__ == "__main__":
    # Here's the bootstrapper, it starts the vector of microservices we'll need, along with their protocols
	enterpriseServiceBus = bus.Bus('amqp://viniciof:4getmenot@rabbitmq-master.default.svc.cluster.local/%2f', 10)
	gatewayService = gateway.Gateway(enterpriseServiceBus)
	dalDbDriver = dal.DalHelper()