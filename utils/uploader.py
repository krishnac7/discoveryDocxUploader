import os
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import datetime

def uploadDocs(configs):
    documentIds = []
    authenticator = IAMAuthenticator(configs["apiKey"])
    discovery = DiscoveryV1(
        version='2019-04-30',
        authenticator=authenticator
    )
    discovery.set_service_url(configs["serviceUrl"])
    files = os.listdir(configs["outputDir"])

    for i,file in enumerate(files):
        filename= file.split('.')
        if filename[1] == 'docx':
            print("\n\033[92m[uploadDoc] Uploading {}{}\033[0m".format(
                configs["outputDir"], file))
            with open(os.path.join(configs["outputDir"], file), 'rb') as fileinfo:
                add_doc = discovery.add_document(
                    configs["envId"],
                    configs["collectionId"],
                    file=fileinfo).get_result()
            print(json.dumps(add_doc, indent=2))
            documentIds.append({'document_name':file,'document_id':add_doc["document_id"],"timestamp":str(datetime.datetime.now()),"status":add_doc["status"]})
    with open('uploadLog.json','w') as outfile:
        json.dump(documentIds,outfile,indent = 4)
