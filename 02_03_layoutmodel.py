# analyze word collections
def display_word_collections(page):
    print(f"---- Words in Page #{page.page_number} ----")
    for word in page.words:
        print(f"Content: {word['content']}")
        print(f"Polygon: {word['polygon']}")
        print(f"Confidence: {word['confidence']}")
        print(f"Span Offset: {word['span']['offset']}, Length: {word['span']['length']}")
        print("--------------------------------")

# analyze selectionMarks collection
def display_selectionMarks_collections(page):
    print(f"---- selectionMarks in Page #{page.page_number} ----")
    if page.selection_marks is not None:
        for selectionMark in page.selection_marks:
            print(f"State: {selectionMark['state']}")
            print(f"Polygon: {selectionMark['polygon']}")
            print(f"Confidence: {selectionMark['confidence']}")
            print(f"Span Offset: {selectionMark['span']['offset']}, Length: {selectionMark['span']['length']}")
            print("--------------------------------")
    else:
        print("No selection marks on this page.")

# analyze lines collection
def display_lines_collections(page):
    print(f"---- Lines in Page #{page.page_number} ----")
    for line in page.lines:
        print(f"Content: {line['content']}")
        print(f"Polygon: {line['polygon']}")
        print(f"Span Offset: {line['spans'][0]['offset']}, Length: {line['spans'][0]['length']}")
        print("--------------------------------")

# analyze pages collection
def analyze_pages(result):
    for page in result.pages:
        print(f"----Analyzing layout from page #{page.page_number}----")
        print(f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}")
        #display_word_collections(page)
        #display_selectionMarks_collections(page)
        display_lines_collections(page)

# analyze paragraphs collection
def analyze_paragraphs(result):
    for paragraph in result.paragraphs:
        print(f"Span Offset: {paragraph['spans'][0]['offset']}, Length: {paragraph['spans'][0]['length']}")
        print(f"Page Number: {paragraph['boundingRegions'][0]['pageNumber']}")
        if paragraph.role is not None: print(f"Role: {paragraph['role']}")
        print(f"Content: {paragraph['content']}")

# analyze tables collection
def analyze_tables(result):
    table_count = 0
    for table in result.tables:
        table_count += 1
        print(f"---- TABLE #{table_count} ----")
        print(f"Row Count: {table['rowCount']}")
        print(f"Col Count: {table['columnCount']}")
        for cell in table['cells']:
            if cell.kind is not None: print(f"Kind: {cell['kind']}")
            print(f"Row Index: {cell['rowIndex']}, Col Index: {cell['columnIndex']}")
            print(f"Content: {cell['content']}")
            print(f"Page Number: {cell['boundingRegions'][0]['pageNumber']}, Polygon: {cell['boundingRegions'][0]['polygon']}")
            print(f"Span Offset: {cell['spans'][0]['offset']}, Length: {cell['spans'][0]['length']}")
            print("--------------------------------")
        print("--------------------------------------------------------------------------------------")

# analyze styles collection
def analyze_styles(result):
    for style in result.styles:
        print(f"Confidence: {style['confidence']}")
        print(f"Span Offset: {style['spans'][0]['offset']}, Length: {style['spans'][0]['length']}")
        print(f"Is Handwritten: {style['isHandwritten']}")
        print("--------------------------------")    

# analyze figures collection
def analyze_figures(result):
    for figure in result.figures:
        print(f"Page Number: {figure['boundingRegions'][0]['pageNumber']}, Polygon: {figure['boundingRegions'][0]['polygon']}")
        print(f"Span Offset: {figure['spans'][0]['offset']}, Length: {figure['spans'][0]['length']}")
        print("Elements:")
        for elements in figure['elements']:
            print(f"{elements}")
               
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
    
    # Analyze a document at a URL:
    docUrl = "https://ziggyzuluetastorage01.blob.core.windows.net/documents/02 - Sample Document Analysis.pdf"
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-layout",
        AnalyzeDocumentRequest(url_source=docUrl)
    )  

    # path_to_sample_document = "<path to your sample file>"
    # with open(path_to_sample_document, "rb") as f:
    #     poller = document_intelligence_client.begin_analyze_document(
    #         "prebuilt-layout", analyze_request=f, content_type="application/octet-stream"
    #     )     
    
    result: AnalyzeResult = poller.result()    
    
    #print(result)
    #analyze_pages(result)
    #analyze_paragraphs(result)
    #analyze_tables(result)
    #analyze_styles(result)
    #analyze_figures(result)




if __name__ == "__main__":
    analyze_layout()