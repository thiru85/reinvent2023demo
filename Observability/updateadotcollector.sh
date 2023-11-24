#!/bin/bash

echo "Updating ADOT EKS Addon to send metrics to Amazon Managed Prometheus"
aws eks update-addon --cluster-name osgiliath --addon-name adot \
    --addon-version v0.84.0-eksbuild.1 \
    --resolve-conflicts PRESERVE \
    --configuration-values file://adotcollectorforAMP.json > /dev/null