import boto3

def translate(message):
    translate = boto3.client('translate', region_name='ap-northeast-1')
    res = translate.translate_text(
        Text=message,
        SourceLanguageCode="en",
        TargetLanguageCode="ja"
    )

    return res['TranslatedText']
