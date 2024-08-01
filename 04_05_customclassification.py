def analyze_covidforms(result):
    if result.documents:
        for document in result.documents:
            if document.fields:
                print(f"Document Type: Covid Consent Form")
                if document.fields["LastName"]: print(f"LastName: {document.fields['LastName'].value_string}")
                if document.fields["FirstName"]: print(f"FirstName: {document.fields['FirstName'].value_string}")
                if document.fields["MiddleName"]: print(f"MiddleName: {document.fields['MiddleName'].value_string}")
                if document.fields["DateOfBirth"]: print(f"DateOfBirth: {document.fields['DateOfBirth'].value_date}")
                if document.fields["Age"]: print(f"Age: {document.fields['Age'].value_number}")
                if document.fields["Male"]: print(f"Male: {document.fields['Male'].value_selection_mark}")
                if document.fields["Female"]: print(f"Female: {document.fields['Female'].value_selection_mark}")
                if document.fields["Other"]: print(f"Other: {document.fields['Other'].value_selection_mark}")
                if document.fields["StreetAddress"]: print(f"StreetAddress: {document.fields['StreetAddress'].value_string}")
                if document.fields["City"]: print(f"City: {document.fields['City'].value_string}")
                if document.fields["State"]: print(f"State: {document.fields['State'].value_string}")
                if document.fields["Zip"]: print(f"Zip: {document.fields['Zip'].value_string}")
                if document.fields["PhoneNumber"]: print(f"PhoneNumber: {document.fields['PhoneNumber'].content}")
                if document.fields["DateOfSignature"]: print(f"DateOfSignature: {document.fields['DateOfSignature'].value_date}")
                if document.fields["ReceivedVaccine"]: print(f"ReceivedVaccine: {document.fields['ReceivedVaccine'].value_selection_mark}")
                if document.fields["VaccineManufacturer"]: print(f"VaccineManufacturer: {document.fields['VaccineManufacturer'].value_string}")
                if document.fields["ReceivedDate"]: print(f"ReceivedDate: {document.fields['ReceivedDate'].value_string}")
                print("-------------------------------------------------\n")

def analyze_passport(result):
    if result.documents:
        for document in result.documents:
            if document.fields:
                print(f"Document Type: Passport")
                if document.fields["LastName"]: print(f"LastName: {document.fields['LastName'].value_string}")
                if document.fields["FirstName"]: print(f"FirstName: {document.fields['FirstName'].value_string}")
                if document.fields["MiddleName"]: print(f"MiddleName: {document.fields['MiddleName'].value_string}")
                if document.fields["Gender"]: print(f"Gender: {document.fields['Gender'].value_string}")
                if document.fields["DateOfBirth"]: print(f"DateOfBirth: {document.fields['DateOfBirth'].value_string}")
                if document.fields["ExpirationDate"]: print(f"ExpirationDate: {document.fields['ExpirationDate'].value_string}")
                if document.fields["Nationality"]: print(f"Nationality: {document.fields['Nationality'].value_string}")
                if document.fields["PassportNo"]: print(f"PassportNo: {document.fields['PassportNo'].value_string}")
                print("-------------------------------------------------\n")

def analyze_license(result):
    if result.documents:
        for document in result.documents:
            if document.fields:
                print(f"Document Type: License")
                if document.fields["LastName"]: print(f"LastName: {document.fields['LastName'].value_string}")
                if document.fields["FirstName"]: print(f"FirstName: {document.fields['FirstName'].value_string}")
                if document.fields["MiddleName"]: print(f"MiddleName: {document.fields['MiddleName'].value_string}")
                if document.fields["Gender"]: print(f"Gender: {document.fields['Gender'].value_string}")
                if document.fields["DateOfBirth"]: print(f"DateOfBirth: {document.fields['DateOfBirth'].value_date}")
                if document.fields["Address"]: print(f"Address: {document.fields['Address'].value_string}")
                if document.fields["Nationality"]: print(f"Nationality: {document.fields['Nationality'].value_string}")
                if document.fields["LicenseNo"]: print(f"LicenseNo: {document.fields['LicenseNo'].value_string}")
                print("-------------------------------------------------\n")


def get_documents(result):
    # Create a list of objects with docType, startPage, and endPage
    documents = []

    for doc in result.documents:
        # Extract docType
        doc_type = doc['docType']
        # Extract page numbers from boundingRegions
        page_numbers = [region['pageNumber'] for region in doc['boundingRegions']]
        # Determine start and end pages
        start_page = min(page_numbers)
        end_page = max(page_numbers)
        # Append to summary list
        documents.append({'docType': doc_type, 'startPage': start_page, 'endPage': end_page})

    return documents


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
    
    from azure.ai.documentintelligence.models import ClassifyDocumentRequest, AnalyzeResult, AnalyzeDocumentRequest
    
    # Analyze a document at a URL:
    docUrl = ""
    poller = document_analysis_client.begin_classify_document(
        "customclassifier01", #enter custom classification model id here
        ClassifyDocumentRequest(url_source=docUrl),
        split="auto"
    )  

    classify_result: AnalyzeResult = poller.result()   
    
    documents = get_documents(classify_result)
    print(documents)
    
    for doc in documents:
        if doc['docType'] == "covidconsentform":
            poller = document_analysis_client.begin_analyze_document(
                "covidforms-neural",
                AnalyzeDocumentRequest(url_source=docUrl),
                pages=f"{doc['startPage']}-{doc['endPage']}"
            ) 
            analyze_result: AnalyzeResult = poller.result()
            analyze_covidforms(analyze_result)
        elif doc['docType'] == "passport":
            poller = document_analysis_client.begin_analyze_document(
                "philpassport-neural",
                AnalyzeDocumentRequest(url_source=docUrl),
                pages=f"{doc['startPage']}-{doc['endPage']}"
            ) 
            analyze_result: AnalyzeResult = poller.result()
            analyze_passport(analyze_result)
        elif doc['docType'] == "driverslicense":
            poller = document_analysis_client.begin_analyze_document(
                "license-neural",
                AnalyzeDocumentRequest(url_source=docUrl),
                pages=f"{doc['startPage']}-{doc['endPage']}"
            ) 
            analyze_result: AnalyzeResult = poller.result()
            analyze_license(analyze_result)

    
    

if __name__ == "__main__":
    analyze_document()