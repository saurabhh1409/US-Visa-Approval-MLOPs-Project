# **End-to-End-US-Visa-Approval-MLOPs-Project**

# Overview
This project builds a MLOps pipeline to predict US visa approval status using machine learning. It demonstrates the complete lifecycle from data ingestion to model deployment.

# Problem Statement

Manual visa evaluation is:

- Time-consuming
- Inconsistent
- Prone to human error

The goal is to build an automated ML system that predicts visa approval based on applicant features such as education, experience and many more.

# Results
Best Model: XGBoost
Accuracy:


# **Git Command**

git add .

git commit -m "Updated"

git push origin main

# **Workflow**
1. constants

2. entity
   
3. components

4. pipeline

5. Main file

# **Export the environment variable**

export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

# **AWS-CICD-Deployment-with-Github-Actions**

**1. Login to AWS console.**

**2. Create IAM user for deployment**

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

# **3. Create ECR repo to store/save docker image**

- Save the URI: 342278407433.dkr.ecr.us-north-1.amazonaws.com/visa

# **4. Create EC2 machine (Ubuntu)**

# **5. Open EC2 and Install docker in EC2 Machine:**

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

# **6. Configure EC2 as self-hosted runner:**

setting>actions>runner>new self hosted runner> choose os> then run command one by one

# **7. Setup github secrets:**

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO
