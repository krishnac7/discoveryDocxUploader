from docx import Document
import os
def splitDoc(documentDir,outputDir):
    files=os.listdir(documentDir)
    
    for file in files:
        print("[splitDoc] Processing {}".format(file))
        if file.split(".")[1]=="docx" or file.split(".")[1]=="doc":
            inputDocument = documentDir+"/"+file
            input_document = Document(inputDocument)
            paragraphs = input_document.paragraphs
            headings=[]

            if not os.path.exists(outputDir):
                os.makedirs(outputDir)

            for i,para in enumerate(paragraphs):
                for run in para.runs:
                    if run.bold and ":" in run.text:
                        headings.append(i)
                        
            for j,heading in enumerate(headings):
                document = Document()
                p = document.add_paragraph()
                run = p.add_run(paragraphs[heading].text)
                run.bold = True
                if not j+1>len(headings)-1:
                    for i in range(headings[j]+1,headings[j+1]):         
                        document.add_paragraph(paragraphs[i].text)
                else:
                    for i in range(headings[j]+1,len(paragraphs)):
                        document.add_paragraph(paragraphs[i].text)
                fileName = "{}{}_{}.docx".format(outputDir,file.split('.')[0],paragraphs[heading].text.split(":")[0])
                print("[splitDoc] Writing to {}".format(fileName))
                document.save(fileName)

