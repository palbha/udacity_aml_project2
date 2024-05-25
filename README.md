*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# Udacity Machine Learning Engineer - Project: Operationalizing Machine Learning
The idea is to do an AutoML run on  bank marketing dataset and deploy the best perofrming model obtained from AutoML as a web service(API). In the project we build pipeline automation to improve machine learning operations


## Architectural Diagram
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/484beaae-9056-4d56-9ada-0fbfaf851e68)


## Key Steps
Key Steps & Corresponding Snapshots
Load Data & create a dataset
Dataset from - https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/3688fa79-cd6a-4ccd-a9e5-2508449871ab)
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/19dbed5b-2f9e-48b4-af1d-818c32009715)


Create Compute
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/aa273113-e82a-40d3-b74a-0845a5ee6dfa)

Submitted AUTOML Job

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/de752326-2cc3-4503-9868-a4aa152999f1)

Evaluating results for AUTOML job

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/9827dcd0-eb03-4a68-b550-ec98dd67d794)
Identify the best performing model & look at the Explanations
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/c4d43f07-5a63-468e-9759-0e672b0ce6c0)

Deploy Model
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/39bc6c6d-feb9-4108-93a3-80bd6164452b)

Enable Application insights

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/fe144dda-8ba8-48a9-bf19-af97b0dcba6c)
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/a5f43a65-3e00-43e9-8211-c25fafa8e0b4)

Since I was just running this in AML directly was able to test from the platform itself .

![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/d3c7b113-5038-44dc-8f7b-036f107c7278)

Also Called it from Python Code
![image](https://github.com/palbha/udacity_aml_project2/assets/20269788/e00f1aed-014b-4804-b826-e296cc249c0f)

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
Few things that can be done in future
Do indepth exploratory data analysis to come up with new features & analyse /cleanse data
Handle data imbalance by appropriate technique like smote
We can enable deep learning & also run the model for a longer duration
Analyse predicted output to identify potential improvement opportunities

