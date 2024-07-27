def analyze_query_extraction(result):
    if result.documents:
        print(result.documents)

    print("Here are extra fields in the result:\n")
    if result.documents:
        for document in result.documents:
            if document.fields and document.fields["FirstName"]:
                print(f"First Name: {document.fields['FirstName'].value_string}")
            if document.fields and document.fields["LastName"]:
                print(f"Last Name: {document.fields['LastName'].value_string}")
            if document.fields and document.fields["Company"]:
                print(f"Company: {document.fields['Company'].value_string}")

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
    
    from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, AnalyzeResult, DocumentAnalysisFeature
    
    # Analyze a document at a URL:
    docUrl = "https://ziggyzuluetastorage01.blob.core.windows.net/documents/02 - Sample Document Analysis.pdf"
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-layout",
        AnalyzeDocumentRequest(url_source=docUrl),
        features={DocumentAnalysisFeature.QUERY_FIELDS, DocumentAnalysisFeature.BARCODES},    # Specify which add-on capabilities to enable.
        query_fields=["FirstName", "LastName", "Company"],  # Set the features and provide a comma-separated list of field names.
    )  

    result: AnalyzeResult = poller.result()    
    analyze_query_extraction(result)
    #analyze_barcode(result)
    
   




if __name__ == "__main__":
    analyze_layout()