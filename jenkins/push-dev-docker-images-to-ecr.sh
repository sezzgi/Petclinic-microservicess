# Provide credentials for Docker to login the AWS ECR and push the images
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin 730335364870.dkr.ecr.us-east-1.amazonaws.com
docker push "${IMAGE_TAG_ADMIN_SERVER}"
docker push "${IMAGE_TAG_API_GATEWAY}"
docker push "${IMAGE_TAG_CONFIG_SERVER}"
docker push "${IMAGE_TAG_CUSTOMERS_SERVICE}"
docker push "${IMAGE_TAG_DISCOVERY_SERVER}"
docker push "${IMAGE_TAG_VETS_SERVICE}"
docker push "${IMAGE_TAG_VISITS_SERVICE}"
docker push "${IMAGE_TAG_GRAFANA_SERVICE}"
docker push "${IMAGE_TAG_PROMETHEUS_SERVICE}"