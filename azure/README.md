# Test on Azure AKS

## 1. Setup AKS cluster with GPU node

Prerequisite:
1. `az cli`
1. Azure Subscription with GPU quota.

Follow the steps below:
1. Update the file `env` as your need, then run `. ./env`.
1. Run the script `setup_aks.sh` to create a AKS cluster.
