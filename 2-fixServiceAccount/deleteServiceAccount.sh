#!/bin/bash

POLICY_ARN=arn:aws:iam::081324788528:policy/DDBAccessPolicy
eksctl delete iamserviceaccount --name i-am-here-now --cluster osgiliath --namespace cakeapi
echo "Waiting for 20 seconds before deleting policy"
sleep 20
aws iam delete-policy --policy-arn arn:aws:iam::081324788528:policy/DDBAccessPolicy