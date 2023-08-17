import boto3
import trp

textract_client = boto3.client('textract', region_name='us-east-1')

def main(file_path):
    response = None
    with open(file_path, 'rb') as document:
        imageBytes = bytearray(document.read())

# Call Textract AnalyzeDocument by passing a document from local disk
    response = textract_client.analyze_document(
    Document={'Bytes': imageBytes},
    FeatureTypes=['FORMS','SIGNATURES']
    )

    doc = trp.Document(response)
    d = []

    for page in doc.pages:
        key = 'Signature'
        fields = page.form.searchFieldsByKey(key)
        for field in fields:
            d.append([field.key, field.value])        

    return "Signed" if str(field.value) != "None" else "Unsigned"

