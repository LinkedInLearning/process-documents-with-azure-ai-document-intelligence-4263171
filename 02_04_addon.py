def analyze_query_extraction(result):
    print("Here are extra fields in the result:\n")
    if result.documents:
        for document in result.documents:
            if document.fields and document.fields["firstname"]:
                print(f"First Name: {document.fields['firstname'].value_string}")
            if document.fields and document.fields["lastname"]:
                print(f"Last Name: {document.fields['lastname'].value_string}")
            if document.fields and document.fields["company"]:
                print(f"Company: {document.fields['company'].value_string}")

def analyze_barcode(result):
    for page in result.pages:
        if hasattr(page, 'barcodes') and page.barcodes:  # Check if barcodes exist
            for barcode in page.barcodes:
                print(f"Barcode Type: {barcode.kind}")
                print(f"Barcode Value: {barcode.value}")
                print(f"Barcode Confidence: {barcode.confidence}")
                print("Barcode Polygon Points: ", end="")
                for point in barcode.polygon:
                    print(f"{point}, ", end="")
                print("\n")


def analyze_layout():
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
    
    from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, AnalyzeResult
    from azure.ai.documentintelligence.models import DocumentAnalysisFeature
    
    # Analyze a document at a URL:
    docUrl = ""
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-layout",
        AnalyzeDocumentRequest(url_source=docUrl),
        #features={DocumentAnalysisFeature.QUERY_FIELDS},
        features={DocumentAnalysisFeature.QUERY_FIELDS, DocumentAnalysisFeature.BARCODES},
        query_fields=["firstname", "lastname", "company"],  # Set the features and provide a comma-separated list of field names.
    )  

    result: AnalyzeResult = poller.result()    
    analyze_query_extraction(result)
    analyze_barcode(result)
    
   
if __name__ == "__main__":
    analyze_layout()