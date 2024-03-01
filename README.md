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
