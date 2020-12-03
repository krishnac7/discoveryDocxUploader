import os
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def uploadDocs(configs):
    authenticator = IAMAuthenticator(configs["apiKey"])
    discovery = DiscoveryV1(
        version='2019-04-30',
        authenticator=authenticator
    )
    discovery.set_service_url(configs["serviceUrl"])
    files=os.listdir(configs["outputDir"])

    for file in files:
        print("\n\033[92m[uploadDoc] Uploading {}{}\033[0m".format(configs["outputDir"],file))
        if file.split('.')[1]=='docx':
            with open(os.path.join(configs["outputDir"], file),'rb') as fileinfo:
                add_doc = discovery.add_document(
                    configs["envId"], 
                    configs["collectionId"],
                    file=fileinfo).get_result()
            print(json.dumps(add_doc, indent=2))