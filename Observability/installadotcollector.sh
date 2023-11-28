#!/bin/bash
echo "Installing addons to the cluster ..."
aws eks create-addon --cluster-name osgiliath \
    --addon-name adot \
    --addon-version v0.84.0-eksbuild.1 > /dev/null
aws eks create-addon --addon-name amazon-cloudwatch-observability --cluster-name osgiliath > /dev/null
echo "Creating service account for the adot collector..."
eksctl create iamserviceaccount \
    --name adot-collector \
    --namespace opentelemetry-operator-system \
    --cluster osgiliath \
    --attach-policy-arn arn:aws:iam::aws:policy/AmazonPrometheusRemoteWriteAccess \
    --attach-policy-arn arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess \
    --attach-policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy \
    --approve \
    --override-existing-serviceaccounts > /dev/null