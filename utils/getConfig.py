import json
def getConfig():
        with open("./config.json") as json_data_file:
            config = json.load(json_data_file)
        missingData = []
        for key in config:
            if len(config[key].split())== 0:
                missingData.append(key)
        if len(missingData)!=0:
            print("\033[91m [ERROR] Values for the following keys are missing from config \n {0} \033[0m".format(missingData))
            exit(1)
        print("\033[92m[getConfig] Configs available \n \033[0m")
        return config