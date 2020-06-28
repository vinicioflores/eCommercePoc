# Hello-World
Frontend, Kubernetes containerized app build with Flask as runtime (listening on 8080 port as default HTTP REST API standards).



1) Install IBMCloud CLI client.
[Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"; iex(New-Object Net.WebClient).DownloadString('https://ibm.biz/idt-win-installer')

2) Install container registry plugin
``ibmcloud plugin install container-registry -r "IBM Cloud"``


3) Login into IBM Cloud - you will be prompted to provide the email and password you set at registration time. Also you choose the region (8 - default)
``ibmcloud login``

4) A resource group is automatically granted in the free account (email@domain.com/dev)

5) In your account payment methods, in WEB UI , provide a Credit Card. This will allow you to create a Free (1 month / $200 credit) Kubernetes cluster. Nothing will be charged unless you exceed the credit.

6) Build a Free Kubernetes cluster (1 node 4 ram 2 cores)
``ibmcloud ks create classic --name Hello-IBM-Cloud-Dev-VF --version 1.17.6``

7) Create a namespace in IBM Container Registry so we can push docker images there.
``ibmcloud cr namespace-add <my_preferred_namespace>``


8) Go to *config* folder and build the docker image
``docker build - < Dockerfile``

9) Tag the image according to IBM Container Registry API base URL
``docker tag hello-world us.icr.io/<my_namespace>/<my_new_repository>:<my_tag>``


10) Push the image thru IBM Container Registry API
``docker push us.icr.io/<my_namespace>/<my_repository>:<my_tag>``

11) Check the image was added in there:
``ibmcloud cr image-list``

Now one simple way to lookup whether the Kubernetes (server side) is up and running by checking if at least it has 1 node UP

``kubectl get nodes``

If there's a node and cluster is up, the proceed to deploy via *kubectl* and provide your YAML file

``kubectl apply -f deployment.yaml``

Now as architects we need to ensure that we have a single centralized place where app's logs arrive so it's easier to maintain in the longer term and easier for developers to debug.

Let's install prometeus as our (proactive monitoring tool to collect defautl stats such as I/O, network latency, etc. ) as well as Grafana to display all that visually. Grafana is already bundled together with Prometheus.

``helm install --name sampleapp stable/prometheus-operator``

Now in order to implement CI/CD pipeline (in this case I'm choosing canary release strategy thinking that in the future we may have many  different microservices not only the HELLO one )

### CHANGELOG:

I've decided to start a POC of a personal use case I want to implement thru IBM Cloud as preferred cloud provider. 

The Use Case is an eCommerge app that behaves very similarly to this Japanese, Tokyo-based store: [Don Quijote](https://www.donki.com/en/ "Don Quijote's Discount Store") basically it works by having a huge catalog of products (here stored in a GeoReplicated MySQL DB farm ) that they initially put by pure "Guess" in the front-door of their physical stores. Then they do "backtracking algorithm" by tracing which products sell the most and which doesn't. The ones that don't sell are put back inside the store and the ones that sell better are put up-front where everyone can see.

It's a POC thus here's the architecture diagram (I've just modified the Docker YAMLs to summon up the MySQL DBs as well)

![Architecture Blueprint](https://github.com/vinicioflores/Hello-World/blob/master/src/eComm.png "Architecture Blueprint")
