# Capstone-Project
### Follow these steps to create a project

1. Create a repository on Github.
2. Clone the repository to your local or computer.
3. Activate the virtual environment.
4. If you are using windows, run these following commands on your command prompt. 
    ## python3 -m venv Kidney 
    ## Kidney\Scripts\activate
5. If you use Anaconda application, use these following commands to create environment. 
    ## conda create -n Kidney python=3.8 -y 
    ## conda activate Kidney
6. If you use Ubuntu or Linux, run these following commands. 
    ## python3 -m venv Kidney 
    ## source Kidney/bin/activate
7. Then install the packages mentioned in requirements.txt file using the following command. 
    ## pip3 install -r requirements.txt

### Workflows

1. Update config.yaml
2. Update secrets.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update the app.py

### Mlflow

1. Go to dagshub.com
2. Create an account and click on new repository
3. Then click on connect a repository and press github
4. Select the repository which you want to integrate with mlflow then press connect button
5. Then click on remote and copy the URI to use in script
6. After that go to mlflow. MLflow supports dagshub so we use it to launch the MLflow server 
7. Open command prompt and run the mlflow uri, username and password with the prefix of export like the following commands
    ## export MLFLOW_TRACKING_URI = link
    ## export MLFLOW_TRACKING_USERNAME = username
    ## export MLFLOW_TRACKING_PASSWORD = passcode
8. If it shows error, use set as prefix instead of using export like the below commands
    ## set MLFLOW_TRACKING_URI = link
    ## set MLFLOW_TRACKING_USERNAME = username
    ## set MLFLOW_TRACKING_PASSWORD = passcode

### Steps to create DVC Pipeline

1. Go through the dvc.yaml file then enter dvc init in command prompt
2. Then enter dvc repro
3. If it shows error enter this in your powershell 
    ## $env:PYTHONPATH = "D:/Final Year Project/Capstone-Project;$env:PYTHONPATH"

### AWS CICD Deployment

1. Login to AWS Console, if you don't have an account give sign up
2. Create IAM user for deployment
3. Click on the user and create an user
4. Enter an username and click on next
5. After clicking it, set the permission option "Attach policies directly". Then add the policies mentioned below and click on next
    ## AmazonEC2ContainerRegistryFullAccess
    ## AmazonEC2FullAccess
5. Then click create user
6. Then click username "KidneyProject" and create access key
7. Click on command line interface and click on next
8. Then click create access key then download it as .csv file
9. Redirect to homepage and search Elastic Container Registry (ECR) and click get started
10. Make the visibility settings as private and set a repository name
11. Copy the URI and save it safely
12. Again come back to homepage and search EC2
13. Then click on launch instance and enter the name in the textfield and click Ubuntu-Machine
14. Then select the instance type as t2.large or t2.micro
15. Then create key pair and set ESB volume as 32gb
16. Click launch instance
17. Click on instance ID and press connect
18. Click on connect and run the following commands
    ## sudo apt-get update -y
    ## sudo apt-get upgrade
    ## curl -fsSL https://get.docker.com -o get-docker.sh
    ## sudo sh get-docker.sh
    ## sudo usermod -aG docker ubuntu
    ## newgrp docker
19. Go to github project repository settings. Click on action then runners
20. Then click on new self-hosted runners and select linux
21. Copy the commands shown in the page and run it on the server of AWS
22. If you go back to the runner, you can be able to see the runner
23. Go to secret and variables in your github repository and click on actions then add secrets
    ## AWS_ACCESS_KEY_ID
    ## AWS_SECRET_ACCESS_KEY
    ## AWS_REGION 
    ## AWS_ECR_LOGIN_URI
    ## ECR_REPOSITORY_NAME