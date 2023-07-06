
# Machine Learning Operations

In this project, Azure AutoML is used to produce a cloud-based machine learning production model with Bank Marketing data. The model could be used to predict if a client would subscribe to a term deposit. Steps are shown how the model is produced,deployed and consumed. Also a pipeline will be created, published and consumed.
<br><br>
## Architectural Diagram
<br>

### Create AutoML run and consume deployed model: <br><br>

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

<br><br><br>

### Create and Publish ML pipeline with SDK <br><br>

```mermaid
flowchart TD
	A[Create NoteBook file] --> B[Define Workspace and Experiment]
	B --> C[Create or attach compute cluster]
	C --> D[Create and register dataset]
	D --> E[Create AutoMLStep and Pipleline]
	E --> F{Submit pipeline and check for rundetails}
	F --> G[Retrive best model from pipeline run]
	F --> H[Publish pipeline]
	G --> I[Test Model with test data]
	H --> J[Trigger pipeline runs from published pipeline endpoint]


```
<br><br><br><br>

## Key Steps
<br>

## The following are steps to create AutoML runs: <br><br>

Created a dataset from downloaded bank marketing data. <br><br>
![created dataset](screenshots/RegisteredDataSetForAutoML.png)

Executed AutoML run from AzureML Studio, and wait for the experiment to complete. <br><br>
![completed automl experiment run](screenshots/CompletedExperimentForAutoML.png)

Examined the experiment result and found out that VotingEnsemble is the best model.<br><br>
![best model](screenshots/AutoMLRunBestModel.png)

Deployed the best model, and enabled deployed endpoint Application Insights by running provided logs.py script. <br><br>
![enable application insight](screenshots/EnableapplicationInsight.png)

The deployed best model endpoint. <br><br>
![deployed endpoint](screenshots/BestModelEndpoint.png)

Downloaded deployed endpoint API swagger.json file, and ran locally to show the API HTTP methods and response.<br><br>
![swagger run](screenshots/SwaggerRuns.png)

Retrieved the deployed endpoint information. <br><br>
![endpoint info](screenshots/EndpointInfo.png)

Modified endpoint.py script with deployed endpoint URL and key, and ran the script to predict for two test clients. From model explaination, "duration" is the most important feature on the results. Larger value (>1000) flip the result from 'no' to 'yes' for the first client.<br><br>
![endpoint consumption](screenshots/EndpointConsumption.png)

Used Apache Benchmark script benchmark.sh to retrieve performance results.<br><br>
![benchmark run](screenshots/BenchMarkRun.png)


## The following are steps to create and publish an ML pipeline:<br><br>

Using Python SDK, an AutoML pipeline was created. <br><br>
![created pipeline](screenshots/CreatedPipeline.png)

A "BankMarketing Dataset" was also created for the pipeline.<br><br>
![pipeline dataset](screenshots/PipelineDataSet.png)

Excuted the pipeline from Jupyter Notebook (see saved aml-pipelines-with-automated-machine-learning-step.ipynb), and published the pipeline. <br><br>
![published pipeline](screenshots/PublishedPipeline.png)

Used RunDetails Widget to show run information.<br><br>
![pipeline RunDetails](screenshots/RunDetailsOfPipelineRun.png)

Published the pipeline as "Bankmarketing Train" from Jupyter Notebook. <br><br>
![SDK published pipelie](screenshots/SDKPublishedPipeline.png)

Created script pipeline.py to interact with the the published pipeline endpoint to trigger an experiment "my-test-endpoint". <br><br>
![trigered pipeline run](screenshots/CompletedPipelineRun.png)

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
