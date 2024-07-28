def analyze_customfields(result):
    if result.documents:
        for document in result.documents:
            if document.fields:
                if document.fields["LastName"]: print(f"LastName: {document.fields['LastName'].value_string}")
                if document.fields["FirstName"]: print(f"FirstName: {document.fields['FirstName'].value_string}")
                if document.fields["MiddleName"]: print(f"MiddleName: {document.fields['MiddleName'].value_string}")
                if document.fields["DateOfBirth"]: print(f"DateOfBirth: {document.fields['DateOfBirth'].value_date}")
                if document.fields["Age"]: print(f"Age: {document.fields['Age'].value_number}")
                if document.fields["Male"]: print(f"Male: {document.fields['Male'].value_selection_mark}")
                if document.fields["Female"]: print(f"Female: {document.fields['Female'].value_selection_mark}")
                if document.fields["Other"]: print(f"Other: {document.fields['Other'].value_selection_mark}")
                if document.fields["ReceivedVaccine"]: print(f"ReceivedVaccine: {document.fields['ReceivedVaccine'].value_selection_mark}")
                if document.fields["VaccineManufacturer"]: print(f"VaccineManufacturer: {document.fields['VaccineManufacturer'].value_string}")
                if document.fields["ReceivedDate"]: print(f"ReceivedDate: {document.fields['ReceivedDate'].value_string}")

def analyze_document():
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
    docUrl = "https://ziggyzuluetastorage01.blob.core.windows.net/documents/04 - consent-form-test-document.pdf"
    poller = document_analysis_client.begin_analyze_document(
        "linkedin-covid-template",
        AnalyzeDocumentRequest(url_source=docUrl)
    )  

    result: AnalyzeResult = poller.result()    
    analyze_customfields(result)


if __name__ == "__main__":
    analyze_document()