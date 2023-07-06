
# Machine Learning Operations

In this project, Azure AutoML is used to produce a cloud-based machine learning production model with Bank Marketing data. The model could be used to predict if a client would subscribe to a term deposit. Steps are shown how the model is produced,deployed and consumed. Also a pipeline will be created, published and consumed.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

### Here is a simple flow chart: <br><br>

```mermaid
flowchart TD
	A[Create data set from bank marketing.csv] --> B[Create or attach a VM cluster and do AutoML Training]
	B --> C[Retrieve Best Model]
	C --> D{Deploy Best Model}
	D --> E[Enable app insights for logging]
	D --> F[Consumed deployed endpoint]
```

<br><br><br>

### AutoML pipeline <br><br>

```mermaid
journey
	title Me studying for exams
	section Exam is announced
		I start studying: 1: Me
		Make notes: 2: Me
		Ask friend for help: 3: Me, Friend
		We study togther: 5: Me, Friend
	section Exam Day
		Syllabys is incomplete: 2: Me
		Give exam: 1: Me, Friend
	section Result Declared
		I passed the exam with destinction!: 5: Me
		Friend barely gets passing marks: 2: Friend

```


## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

For AutoML, 
1. Create dataset from bank marketing csv data.
![created dataset](screenshots/RegisteredDataSetForAutoML.png)

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
