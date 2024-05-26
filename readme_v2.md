*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# Udacity Machine Learning Engineer - Project: Operationalizing Machine Learning
The idea is to do an AutoML run on  bank marketing dataset and deploy the best perofrming model obtained from AutoML as a web service(API). In the project we build pipeline automation to improve machine learning operations


## Architectural Diagram
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/484beaae-9056-4d56-9ada-0fbfaf851e68)


## Key Steps
Key Steps & Corresponding Snapshots
Load Data & create a dataset
Dataset from - https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv
DataSet in Azureml
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/37b5eb0a-b735-4002-9e56-ba5f3ef9e4b2)
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/422b4ac7-4e79-441c-b9c1-874d5835dfa7)


Snapshot of jobs using this dataset as well
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/41060b5f-f94c-46db-8f3e-224a70cddf40)

Create Compute
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/fa96923a-67a4-446c-83c2-cb81c8e7c028)

Submitted AUTOML Job & Evaluating results for AUTOML job
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/1cd63f02-4554-4f22-85db-87acf336b26f)
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/bfb475a6-7fed-41fd-aaa4-b8d8ebf559b5)



![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/9827dcd0-eb03-4a68-b550-ec98dd67d794)
Identify the best performing model & look at the Explanations
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/32254603-ce41-4ce8-900d-64aebb0642d5)
Regsiter Model
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/e72bf14d-2701-42a6-8c73-158b3b6fd6ff)

Deploy Model
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/4f675c7f-f049-4f90-ae93-d7fc87cc7fd1)

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/fc63369d-4c89-44d1-875e-f3f56fd44bf7)


Consume Model
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/5e2de77f-2690-456f-a6f6-c11b380d52a9)
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/1033d45d-3139-4bc6-82c8-9b6a2b8549f5)

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/e0d5c775-1320-417e-9685-ff625f0ba670)

Swagger Snapshots
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/59aa8a88-446c-4523-b07c-9302470d73cf)

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/32bcc51e-8401-414b-9a30-2dc2825b87be)


Create Pipeline
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/f29cef23-3227-449d-a97a-a7737cde45cd)

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/b3da93f5-fa09-40e6-be92-bb542622fadc)
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/6329e901-207f-47ce-8800-09115493f58c)

Run the Publish Pipelines 
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/4b3a313c-50b5-4163-b95d-9cf5c9f89b55)

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/d1d29d75-990f-4c4a-99be-17b14d066fd3)
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/7a5bcce5-89cd-43df-8720-916d56fd2486)
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/3cb45bf1-f88c-4f6d-973e-1e097c3cb6b2)

https://github.com/palbha/udacity_aml_project2/blob/master/Exercise_starter_files/aml-pipelines-with-automated-machine-learning-step.ipynb

Utilized the above notebook to run and publish pipliens (Covered view in the below video link)
## Screen Recording
Link for the recording
https://github.com/palbha/udacity_aml_project2/blob/master/Recording-20240525_145305.webm
https://github.com/palbha/udacity_aml_project2/blob/master/Recording-20240525_150740.webm
https://github.com/palbha/udacity_aml_project2/blob/master/Recording-20240526_125546.webm -- Added new recording based on the feedback recieved

## Standout Suggestions
Few things that can be done in future
Do indepth exploratory data analysis to come up with new features & analyse /cleanse data
Handle data imbalance by appropriate technique like smote
We can enable deep learning & also run the model for a longer duration
Analyse predicted output to identify potential improvement opportunities

https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-explore-data?view=azureml-api-2
https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-deep-learning/#:~:text=Deep%20learning%20is%20a%20type%20of%20machine%20learning,with%20data%2C%20recognize%20patterns%2C%20make%20recommendations%2C%20and%20adapt.
