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