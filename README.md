# Hello-World
Frontend, Kubernetes containerized app build with Flask as runtime (listening on 8080 port as default HTTP REST API standards) . Includes ARM template to deploy via Azure Portal.


``az group create --name NetworkWatcherRg --location eastus``

After creating a resource group in Azure (NetworkWatcherRg)  based on East US initially, we can create more to be able to countabilize costs based on GEOs for example (AMR, LATAM, APAC, EMEA)

Run this using embedded Powershell ==> ``az aks create --resource-group NetworkWatcherRg --name KSClusterPOC --node-count 1 --enable-addons monitoring --generate-ssh-keys``

Then install the Kubernetes client application (allows you to interact with the cluster and deploy apps)

``az aks install-cli``


