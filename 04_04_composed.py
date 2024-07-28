def analyze_composedmodel(result):
    if result.documents:
        for document in result.documents:
            if document.doc_type == "composed-model-id:license-neural":
                print("License document: composed-model-id:license-neural")
                if document.fields["LastName"]: print(f"LastName: {document.fields['LastName'].value_string}")
                if document.fields["FirstName"]: print(f"FirstName: {document.fields['FirstName'].value_string}")
                if document.fields["MiddleName"]: print(f"MiddleName: {document.fields['MiddleName'].value_string}")
                if document.fields["Gender"]: print(f"Gender: {document.fields['Gender'].value_string}")
                if document.fields["DateOfBirth"]: print(f"DateOfBirth: {document.fields['DateOfBirth'].value_date}")
                if document.fields["Address"]: print(f"Address: {document.fields['Address'].value_string}")
                if document.fields["Nationality"]: print(f"Nationality: {document.fields['Nationality'].value_string}")
                if document.fields["LicenseNo"]: print(f"LicenseNo: {document.fields['LicenseNo'].value_string}")
            if document.doc_type == "composed-model-id:philpassport-neural":
                print("Passport document: composed-model-id:philpassport-neural")
                if document.fields["LastName"]: print(f"LastName: {document.fields['LastName'].value_string}")
                if document.fields["FirstName"]: print(f"FirstName: {document.fields['FirstName'].value_string}")
                if document.fields["MiddleName"]: print(f"MiddleName: {document.fields['MiddleName'].value_string}")
                if document.fields["Gender"]: print(f"Gender: {document.fields['Gender'].value_string}")
                if document.fields["DateOfBirth"]: print(f"DateOfBirth: {document.fields['DateOfBirth'].value_string}")
                if document.fields["ExpirationDate"]: print(f"ExpirationDate: {document.fields['ExpirationDate'].value_string}")
                if document.fields["Nationality"]: print(f"Nationality: {document.fields['Nationality'].value_string}")
                if document.fields["PassportNo"]: print(f"PassportNo: {document.fields['PassportNo'].value_string}")


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
    
    from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, AnalyzeResult, DocumentAnalysisFeature
    
    # Analyze a document at a URL:
    docUrl = "https://ziggyzuluetastorage01.blob.core.windows.net/documents/04_04 - passport sample.jpg"
    poller = document_analysis_client.begin_analyze_document(
        "composed-model-id",
        AnalyzeDocumentRequest(url_source=docUrl)
    )  

    result: AnalyzeResult = poller.result()   
    analyze_composedmodel(result) 

if __name__ == "__main__":
    analyze_document()