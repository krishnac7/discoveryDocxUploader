import os
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from utils.getConfig import getConfig
import datetime
# import tablib

def getDocDetails(configs):
    authenticator = IAMAuthenticator(configs["apiKey"])
    discovery = DiscoveryV1(version='2019-04-30',authenticator=authenticator)
    discovery.set_service_url(configs["serviceUrl"])
    uploadLog,fileLog = {},[]
    with open('uploadLog.json') as f:
        uploadLog = json.load(f)
    for document in uploadLog:
        doc_info = discovery.get_document_status(
        configs["envId"], 
        configs["collectionId"], 
        document["document_id"]).get_result()
        print("update for "+document["document_id"])
        doc_info["timestamp"] = str(datetime.datetime.now())
        fileLog.append(doc_info)
    with open('availabilityLog.json','w') as outfile:
        json.dump(fileLog,outfile,indent = 4)
    # data = tablib.Dataset(fileLog)
    # open('results.xls','wb').write(data.xls)

print("\n\033[95mChecking configuration... \033[0m")
configs = getConfig()
getDocDetails(configs)