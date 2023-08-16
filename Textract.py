import boto3
textract_client = boto3.client('textract', region_name='us-east-1')
def perform_ocr(file_path):
    with open(file_path, 'rb') as file:
        out = textract_client.detect_document_text(Document={'Bytes': file.read()})
        return dict(out)

def main(path):
    result = perform_ocr(path)
    hadn = len([s for s in result['Blocks'] if 'HANDWRITING' in str(s)])
    return 'Signed' if hadn > 0 else 'Unsigned'
