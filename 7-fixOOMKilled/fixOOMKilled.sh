#!/bin/bash

kubectl apply -f kube/.
echo "Waiting for load balancer to be created. 20 seconds please!"
sleep 20
export AWSLB=$(aws elb describe-load-balancers | jq -r '.LoadBalancerDescriptions[].DNSName')
aws route53 change-resource-record-sets --hosted-zone-id Z0798709BAX9BZ17B1IE --change-batch '{"Changes":[{"Action":"UPSERT","ResourceRecordSet":{"Name":"cakeapi.demoaws.xyz","Type":"CNAME","TTL":15,"ResourceRecords":[{"Value":"'"${AWSLB}."'"}]}}]}' > /dev/null
echo "Done!"