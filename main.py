
from utils.getConfig import getConfig
from utils.docProcessor import splitDoc
from utils.uploader import uploadDocs

print("\n\033[95mChecking configuration... \033[0m")
configs = getConfig()

print("\n\033[95mStarting document processing... \033[0m")
splitDoc(configs['documentDir'],configs['outputDir'])

print("\n\033[95mDocument Upload started \033[0m")
uploadDocs(configs)