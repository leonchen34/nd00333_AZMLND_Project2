
# Machine Learning Operations

In this project, Bank Marketing data is utilized to create a cloud-based machine learning model that predicts whether a client would subscribe to a term deposit. First AML Studio AutoML method is employed, showcasing the steps involved in generating,deploying, and consuming the best model. Also AML Python SDK is employed to construct and publish an AutoML pipeline. The published pipeline endpoint can be triggered to execute experiment runs. 
<br><br>
## Architectural Diagram
<br>


### Create experiment with AutoML and Deploy best model for consumption : <br><br>

![automl](screenshots/architecture1.drawio.svg)<br>


<br><br>

### Create and Publish ML pipeline with SDK <br><br>

![pipeline](screenshots/architecture2.drawio.svg)
<br><br><br>

## Key Steps
<br>

## The following are steps to create and deploy AutoML best model: <br><br>

Created a dataset from downloaded bank marketing data. <br><br>
![created dataset](screenshots/RegisteredDataSetForAutoML.png)

Executed AutoML run from AzureML Studio, and wait for the experiment run to complete. <br><br>
![completed automl experiment run](screenshots/CompletedExperimentForAutoML.png)

Examined the experiment run results and found out that VotingEnsemble is the best model.<br><br>
![best model](screenshots/AutoMLRunBestModel.png)

Deployed the best model, and enabled deployed endpoint Application Insights by running logs.py script. <br><br>
![enable application insight](screenshots/EnableapplicationInsight.png)

The deployed model endpoint. <br><br>
![deployed endpoint](screenshots/BestModelEndpoint.png)

Downloaded deployed endpoint API swagger.json file, and ran locally to show the API HTTP methods and response.<br><br>
![swagger run](screenshots/SwaggerRuns.png)

Retrieved the deployed endpoint information. <br><br>
![endpoint info](screenshots/EndpointInfo.png)

Modified endpoint.py script with deployed endpoint URL and key, and ran the script to predict for two test clients. From model explaination, "duration" is the most important feature. Larger value (>1000) flip the result from 'no' to 'yes' for the first client.<br><br>
![endpoint consumption](screenshots/EndpointConsumption.png)

Used Apache Benchmark script benchmark.sh to get performance results.<br><br>
![benchmark run](screenshots/BenchMarkRun.png)


## The following are steps to create and publish ML pipeline:<br><br>

Using AML Python SDK, an AutoML pipeline was created. <br><br>
![created pipeline](screenshots/CreatedPipeline.png)

A "BankMarketing Dataset" was also created for the pipeline.<br><br>
![pipeline dataset](screenshots/PipelineDataSet.png)

Excuted the pipeline from Jupyter Notebook (see aml-pipelines-with-automated-machine-learning-step.ipynb), and published the pipeline. <br><br>
![published pipeline](screenshots/PublishedPipeline.png)

Used RunDetails Widget to show run information.<br><br>
![pipeline RunDetails](screenshots/RunDetailsOfPipelineRun.png)

Published the pipeline as "Bankmarketing Train" from Jupyter Notebook. <br><br>
![SDK published pipelie](screenshots/SDKPublishedPipeline.png)

Created script pipeline.py to interact with the the published pipeline endpoint to trigger an experiment "my-test-endpoint". <br><br>
![trigered pipeline run](screenshots/CompletedPipelineRun.png)

<br><br>
## Screen Recording:<br>
### Click the following link 
<br><br>
[![Screen Cast](screenshots/ScreenCast.png)](https://youtu.be/6KabcG_lWus)

## Extra Works

1. Ran Apache Benchmark load test to check deployed endpoint performance. Screen capture is included above.

2. To make bulk tests/predictions more efficient for the deployed model, tried to create Parallel Run pipeline.
<br>
First Registered the best model from pipeline run as shown below (from aml-pipelines-with-automated-machine-learning-step.ipynb) <br><br>

![register model](screenshots/RegisterBestPipelineModel.png)

 Then created files "parallel-run.ipynb" and "score.py".
 But when executing parallel-run.ipynb, got the following pipeline run log error <br><br>
 ![failed parallel step](screenshots/FailedParellelStepLog.png)
 
 Would appreciate it if helping me to figure out the problem.


 ## Future Improvement

 We can do some preprocessing on the data to improve the training process, for example converting some feature value to number type, such as "y" field from "yes" and "no" to 1 and 0, "married" field to 1 and 0. Also we can drop some features which has no much effect on target, such as "contact" method, "job" type etc. To do it systematically, we can start with a subset of the data, and review the explaination of best model and get some hint on what features to be dropped.

 Another thing we can do is to block some models in AutoMLConfig, so that AutoML will not go through all possible algorithms.

