from azureml.core.authentication import InteractiveLoginAuthentication
import requests
import json

#one of the published pipeline endpoint url https
pipeline_endpoint_uri = 'https://eastus.api.azureml.ms/pipelines/v1.0/subscriptions/1e04f273-c7e2-451f-8bf1-d3116603299b/resourceGroups/demo/providers/Microsoft.MachineLearningServices/workspaces/udacity-aml/PipelineRuns/PipelineSubmit/223fa575-4770-4267-93a9-fcf6a5449fd0'

interactive_auth = InteractiveLoginAuthentication()
auth_header = interactive_auth.get_authentication_header()

response = requests.post(pipeline_endpoint_uri, 
                         headers=auth_header, 
                         json={"ExperimentName": "my-test-endpoint3"}
                        )

try:
    response.raise_for_status()
except Exception:    
    raise Exception("Received bad response from the endpoint: {}\n"
                    "Response Code: {}\n"
                    "Headers: {}\n"
                    "Content: {}".format(rest_endpoint, response.status_code, response.headers, response.content))

run_id = response.json().get('Id')
print('Submitted pipeline run: ', run_id)
