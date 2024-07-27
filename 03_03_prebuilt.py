def analyze_invoices(result):
    if result.documents:
        for idx, invoice in enumerate(result.documents):
            print(f"--------Analyzing invoice #{idx + 1}--------")
            if invoice.fields:
                vendor_name = invoice.fields.get("VendorName")
                if vendor_name:
                    print(f"Vendor Name: {vendor_name.get('content')} has confidence: {vendor_name.get('confidence')}")
                vendor_address = invoice.fields.get("VendorAddress")
                if vendor_address:
                    print(
                        f"Vendor Address: {vendor_address.get('content')} has confidence: {vendor_address.get('confidence')}"
                    )
                vendor_address_recipient = invoice.fields.get("VendorAddressRecipient")
                if vendor_address_recipient:
                    print(
                        f"Vendor Address Recipient: {vendor_address_recipient.get('content')} has confidence: {vendor_address_recipient.get('confidence')}"
                    )
                customer_name = invoice.fields.get("CustomerName")
                if customer_name:
                    print(
                        f"Customer Name: {customer_name.get('content')} has confidence: {customer_name.get('confidence')}"
                    )
                customer_id = invoice.fields.get("CustomerId")
                if customer_id:
                    print(f"Customer Id: {customer_id.get('content')} has confidence: {customer_id.get('confidence')}")
                customer_address = invoice.fields.get("CustomerAddress")
                if customer_address:
                    print(
                        f"Customer Address: {customer_address.get('content')} has confidence: {customer_address.get('confidence')}"
                    )
                customer_address_recipient = invoice.fields.get("CustomerAddressRecipient")
                if customer_address_recipient:
                    print(
                        f"Customer Address Recipient: {customer_address_recipient.get('content')} has confidence: {customer_address_recipient.get('confidence')}"
                    )
                invoice_id = invoice.fields.get("InvoiceId")
                if invoice_id:
                    print(f"Invoice Id: {invoice_id.get('content')} has confidence: {invoice_id.get('confidence')}")
                invoice_date = invoice.fields.get("InvoiceDate")
                if invoice_date:
                    print(
                        f"Invoice Date: {invoice_date.get('content')} has confidence: {invoice_date.get('confidence')}"
                    )
                invoice_total = invoice.fields.get("InvoiceTotal")
                if invoice_total:
                    print(
                        f"Invoice Total: {invoice_total.get('content')} has confidence: {invoice_total.get('confidence')}"
                    )
                due_date = invoice.fields.get("DueDate")
                if due_date:
                    print(f"Due Date: {due_date.get('content')} has confidence: {due_date.get('confidence')}")
                purchase_order = invoice.fields.get("PurchaseOrder")
                if purchase_order:
                    print(
                        f"Purchase Order: {purchase_order.get('content')} has confidence: {purchase_order.get('confidence')}"
                    )
                billing_address = invoice.fields.get("BillingAddress")
                if billing_address:
                    print(
                        f"Billing Address: {billing_address.get('content')} has confidence: {billing_address.get('confidence')}"
                    )
                billing_address_recipient = invoice.fields.get("BillingAddressRecipient")
                if billing_address_recipient:
                    print(
                        f"Billing Address Recipient: {billing_address_recipient.get('content')} has confidence: {billing_address_recipient.get('confidence')}"
                    )
                shipping_address = invoice.fields.get("ShippingAddress")
                if shipping_address:
                    print(
                        f"Shipping Address: {shipping_address.get('content')} has confidence: {shipping_address.get('confidence')}"
                    )
                shipping_address_recipient = invoice.fields.get("ShippingAddressRecipient")
                if shipping_address_recipient:
                    print(
                        f"Shipping Address Recipient: {shipping_address_recipient.get('content')} has confidence: {shipping_address_recipient.get('confidence')}"
                    )
                print("Invoice items:")
                items = invoice.fields.get("Items")
                if items:
                    for idx, item in enumerate(items.get("valueArray")):
                        print(f"...Item #{idx + 1}")
                        item_description = item.get("valueObject").get("Description")
                        if item_description:
                            print(
                                f"......Description: {item_description.get('content')} has confidence: {item_description.get('confidence')}"
                            )
                        item_quantity = item.get("valueObject").get("Quantity")
                        if item_quantity:
                            print(
                                f"......Quantity: {item_quantity.get('content')} has confidence: {item_quantity.get('confidence')}"
                            )
                        unit = item.get("valueObject").get("Unit")
                        if unit:
                            print(f"......Unit: {unit.get('content')} has confidence: {unit.get('confidence')}")
                        unit_price = item.get("valueObject").get("UnitPrice")
                        if unit_price:
                            unit_price_code = (
                                unit_price.get("valueCurrency").get("currencyCode")
                                if unit_price.get("valueCurrency").get("currencyCode")
                                else ""
                            )
                            print(
                                f"......Unit Price: {unit_price.get('content')}{unit_price_code} has confidence: {unit_price.get('confidence')}"
                            )
                        product_code = item.get("valueObject").get("ProductCode")
                        if product_code:
                            print(
                                f"......Product Code: {product_code.get('content')} has confidence: {product_code.get('confidence')}"
                            )
                        item_date = item.get("valueObject").get("Date")
                        if item_date:
                            print(
                                f"......Date: {item_date.get('content')} has confidence: {item_date.get('confidence')}"
                            )
                        tax = item.get("valueObject").get("Tax")
                        if tax:
                            print(f"......Tax: {tax.get('content')} has confidence: {tax.get('confidence')}")
                        amount = item.get("valueObject").get("Amount")
                        if amount:
                            print(f"......Amount: {amount.get('content')} has confidence: {amount.get('confidence')}")
                subtotal = invoice.fields.get("SubTotal")
                if subtotal:
                    print(f"Subtotal: {subtotal.get('content')} has confidence: {subtotal.get('confidence')}")
                total_tax = invoice.fields.get("TotalTax")
                if total_tax:
                    print(f"Total Tax: {total_tax.get('content')} has confidence: {total_tax.get('confidence')}")
                previous_unpaid_balance = invoice.fields.get("PreviousUnpaidBalance")
                if previous_unpaid_balance:
                    print(
                        f"Previous Unpaid Balance: {previous_unpaid_balance.get('content')} has confidence: {previous_unpaid_balance.get('confidence')}"
                    )
                amount_due = invoice.fields.get("AmountDue")
                if amount_due:
                    print(f"Amount Due: {amount_due.get('content')} has confidence: {amount_due.get('confidence')}")
                service_start_date = invoice.fields.get("ServiceStartDate")
                if service_start_date:
                    print(
                        f"Service Start Date: {service_start_date.get('content')} has confidence: {service_start_date.get('confidence')}"
                    )
                service_end_date = invoice.fields.get("ServiceEndDate")
                if service_end_date:
                    print(
                        f"Service End Date: {service_end_date.get('content')} has confidence: {service_end_date.get('confidence')}"
                    )
                service_address = invoice.fields.get("ServiceAddress")
                if service_address:
                    print(
                        f"Service Address: {service_address.get('content')} has confidence: {service_address.get('confidence')}"
                    )
                service_address_recipient = invoice.fields.get("ServiceAddressRecipient")
                if service_address_recipient:
                    print(
                        f"Service Address Recipient: {service_address_recipient.get('content')} has confidence: {service_address_recipient.get('confidence')}"
                    )
                remittance_address = invoice.fields.get("RemittanceAddress")
                if remittance_address:
                    print(
                        f"Remittance Address: {remittance_address.get('content')} has confidence: {remittance_address.get('confidence')}"
                    )
                remittance_address_recipient = invoice.fields.get("RemittanceAddressRecipient")
                if remittance_address_recipient:
                    print(
                        f"Remittance Address Recipient: {remittance_address_recipient.get('content')} has confidence: {remittance_address_recipient.get('confidence')}"
                    )

def analyze_keyvaluepairs(result):
    if result.key_value_pairs:  # Check if barcodes exist
        for kvp in result.key_value_pairs:
            print(f"----------------")
            if kvp.key.content: print(f"Key: {kvp.key.content}")
            if kvp.value: print(f"Value: {kvp.value.content}") 
            else: print(f"Value: None")
            if kvp.confidence: print(f"Confidence: {kvp.confidence}")

def analyze_query_extraction(result):
    print("Here are extra fields in the result:\n")
    if result.documents:
        for document in result.documents:
            if document.fields and document.fields["paymentmethods"]:
                print(f"Payment Methods: {document.fields['paymentmethods'].value_string}")
            

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
    docUrl = "https://ziggyzuluetastorage01.blob.core.windows.net/documents/02 - invoice_sample.png"
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-invoice",
        AnalyzeDocumentRequest(url_source=docUrl),
        features={DocumentAnalysisFeature.QUERY_FIELDS, DocumentAnalysisFeature.KEY_VALUE_PAIRS},    # Specify which add-on capabilities to enable.
        query_fields=["paymentmethods"],  # Set the features and provide a comma-separated list of field names.
    )  

    result: AnalyzeResult = poller.result()    
    analyze_invoices(result)
    analyze_keyvaluepairs(result)
    analyze_query_extraction(result)
   




if __name__ == "__main__":
    analyze_document()