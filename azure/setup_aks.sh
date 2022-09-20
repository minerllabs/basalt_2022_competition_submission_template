#!/bin/bash

# AZ login
az login
az account set -s ${SUBSCRIPTION}

# Create resource group
az group create --location westus2 --name ${RESOURCE_GROUP} --subscription ${SUBSCRIPTION}

# Create AKS
az aks create -g ${RESOURCE_GROUP} -n ${CLUSTER_NAME} --ssh-key-value ${PUBLIC_KEY_FILE} --node-count 1
az aks get-credentials -g ${RESOURCE_GROUP} -n ${CLUSTER_NAME}

# Add a node pool for GPU nodes
# https://learn.microsoft.com/en-us/azure/aks/gpu-cluster
az feature register --name GPUDedicatedVHDPreview --namespace Microsoft.ContainerService
# It might take several minutes for the status to show as Registered. You can check the registration status by using the az feature list command:
az feature list -o table --query "[?contains(name, 'Microsoft.ContainerService/GPUDedicatedVHDPreview')].{Name:name,State:properties.state}"
# When the status shows as registered, refresh the registration of the Microsoft.ContainerService resource provider by using the az provider register command:
az provider register --namespace Microsoft.ContainerService

# Need to install the aks-preview cli, or the nodepool creating would fail.
# install the aks-preview CLI extension
az extension add --name aks-preview
az extension update --name aks-preview

# Create the gpu nodepool
az aks nodepool add \
   --resource-group ${RESOURCE_GROUP} \
   --cluster-name ${CLUSTER_NAME} \
   --name gpunp \
   --node-count 1 \
   --node-vm-size ${GPU_VM_SKU} \
   --node-taints sku=gpu:NoSchedule \
   --aks-custom-headers UseGPUDedicatedVHD=true,usegen2vm=true \
   --enable-cluster-autoscaler \
   --min-count 0 \
   --max-count 3
