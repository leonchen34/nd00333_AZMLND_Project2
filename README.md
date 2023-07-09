
# Machine Learning Operations

In this project, Bank Marketing data is utilized to create a cloud-based machine learning model that predicts whether a client would subscribe to a term deposit. First AML Studio AutoML method is employed, showcasing the steps involved in generating,deploying, and consuming the best model. Also AML Python SDK is employed to construct and publish an AutoML pipeline. The published pipeline endpoint can be triggered to execute experiment runs. 
<br><br>
## Architectural Diagram
<br>

### Create experiment with AutoML and Deploy best model for consumption : <br><br>

```mermaid
flowchart TD
	A[Create data set from bank marketing data] --> B[Create or attach a VM cluster and do AutoML Training]
	B --> C[Retrieve Best Model]
	C --> D{Deploy Best Model}
	D --> E[Enable app insights]
	D --> F[Swagger run to show API]
	D --> G[Consume deployed endpoint]
	D --> H[Apache Benchmark run]
```

<br><br>

### Create and Publish ML pipeline with SDK <br><br>

```mermaid
flowchart TD
	B[Define Workspace and Experiment] --> C[Create or attach compute cluster]
	C --> D[Create and register dataset]
	D --> E[Create AutoMLStep and Pipleline]
	E --> F{Submit pipeline and check for rundetails}
	F --> G[Retrive best model from pipeline run]
	F --> H[Publish pipeline]
	G --> I[Test Model with test data]
	H --> J[Trigger pipeline runs from published pipeline endpoint]


```
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
[![Screen Cast](screenshots/ScreenCast.png)](https://youtu.be/NlivYU8uRk4)

## Standout Suggestions

1. Ran Apache Benchmark load test to check deployed endpoint performance. Screen capture is included above.

2. To make bulk tests/predictions more efficient for the deployed model, tried to create Parallel Run pipeline.
<br>
First Registered the best model from pipeline run as shown below (from aml-pipelines-with-automated-machine-learning-step.ipynb) <br><br>

![register model](screenshots/RegisterBestPipelineModel.png)

 Then created files "parallel-run.ipynb" and "score.py".
 But when executing parallel-run.ipynb, got the following pipeline run log error <br><br>
 ![failed parallel step](screenshots/FailedParellelStepLog.png)
 
 Would appreciate it if helping me to figure out the problem.

