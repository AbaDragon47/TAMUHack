import pdfplumber
import boto3


comprehend = boto3.client('comprehend')


import json

# Initialize a boto3 client for SageMaker runtime
sagemaker_runtime = boto3.client('runtime.sagemaker')

# Set your SageMaker endpoint name
endpoint_name = 'tamu'

# Function to get embeddings
def get_embeddings(text):
    # Format the input for the model (usually as a JSON payload)
    payload = {
        'inputs': text
    }

    # Invoke the SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',
        Body=json.dumps(payload)
    )

    # Process the response from SageMaker
    embeddings = json.loads(response['Body'].read().decode())
    return embeddings

# Example usage
text = "This is a sample note about deep learning and neural networks."
embeddings = get_embeddings(text)
print(embeddings)  # This will print the embeddings returned by SageMaker 

def extract_syllabus_topics(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    # You can process this text to extract topics based on certain keywords, etc.
    return text

