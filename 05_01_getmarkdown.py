from dotenv import find_dotenv, load_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

import os
# get parameters from environment variables
endpoint = os.environ["AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"]
key = os.environ["AZURE_DOCUMENT_INTELLIGENCE_KEY"]

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential

# use api key to create credential
credential=AzureKeyCredential(key)

document_analysis_client = DocumentIntelligenceClient(endpoint, credential)

from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, AnalyzeResult, ContentFormat
    
# GET NORMAL OUTPUT
docUrl = "https://ziggyzuluetastorage01.blob.core.windows.net/documents/02 - Sample Document Analysis.pdf"
poller = document_analysis_client.begin_analyze_document(
    "prebuilt-layout",
    AnalyzeDocumentRequest(url_source=docUrl)
)  
result: AnalyzeResult = poller.result()   

 # Check if file exists and delete if it does
outputDocument = "outputNormal.md"
if os.path.exists(outputDocument):
    os.remove(outputDocument)
# Write the result to a file
with open(outputDocument, "w") as f:
    f.write(result.content)

# GET MARKDOWN OUTPUT
poller = document_analysis_client.begin_analyze_document(
    "prebuilt-layout",
    AnalyzeDocumentRequest(url_source=docUrl),
    output_content_format=ContentFormat.MARKDOWN
)  
result: AnalyzeResult = poller.result()   

 # Check if file exists and delete if it does
outputDocument = "outputMarkdown.md"
if os.path.exists(outputDocument):
    os.remove(outputDocument)
# Write the result to a markdown file
with open(outputDocument, "w") as f:
    f.write(result.content)