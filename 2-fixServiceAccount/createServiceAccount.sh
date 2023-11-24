#!/bin/bash

aws iam delete-policy --policy-arn arn:aws:iam::081324788528:policy/DDBAccessPolicy
aws iam create-policy --policy-name DDBAccessPolicy --policy-document file://iampolicydoc.json | jq -r '.Policy.Arn'
POLICY_ARN=arn:aws:iam::081324788528:policy/DDBAccessPolicy
eksctl create iamserviceaccount --name i-am-here-now --attach-policy-arn $POLICY_ARN --namespace cakeapi --cluster osgiliath --approve



