# Kidney-Tumor-classification-DL-using-MLFlow-CICD

## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py



export MLFLOW_TRACKING_URI=https://dagshub.com/Meabhijit11/Kidney-Tumor-classification-DL-using-MLFlow-CICD.mlflow

export MLFLOW_TRACKING_USERNAME=Meabhijit11

export MLFLOW_TRACKING_PASSWORD=89282ef0e6b088b214cf1e7e5329275ad100579f

# AWS-CICD-Deployment-with-Github-Actions

1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
