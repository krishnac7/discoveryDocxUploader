
from utils.getConfig import getConfig
from utils.docProcessor import splitDoc
from utils.uploader import uploadDocs


print("\n\033[95mChecking configuration... \033[0m")
configs = getConfig()

print("\n\033[95mStarting document processing... \033[0m")
splitDoc(configs['documentDir'],configs['outputDir'])

print("\n\033[95mDocument Upload started \033[0m")
uploadDocs(configs)
print("\n\033[95mJob Complete \033[0m")
print("\n\033[95mPlease run updateLog.py to get document upload results in results.xls \033[0m")

