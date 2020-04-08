#-----------------------------------------Retrieve Comments from Regulations.gov---------------------------------------#
#---------------------------------------------The GW Regulatory Studies Center-----------------------------------------#
#--------------------------------------------------Author: Zhoudan Xie-------------------------------------------------#
#-----------------------------------------------Last Update: April 8, 2020---------------------------------------------#

# Import packages
import pandas as pd
import urllib
import json
import time
import os

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------Retrieve comments by Document ID----------------------------------------------
docketFile='Retrieve Comments/DocketExample.csv'    # Specify the path of your docket metadata file exported from Regulation.gov
docket = pd.read_csv(docketFile,skiprows=4)
docket=docket[docket['Document Type']=='PUBLIC SUBMISSIONS']
print(docket.info())

APIkey="XkS4cyfqMZf2E9mIgYkfI1E7AYa2c0eC02rUTib7"   # Add your API key here

# Retrieve text comments
baseURL = "https://api.data.gov:443/regulations/v3/document.json?api_key="+APIkey+"&documentId="
dic_comments = {}
for docID in docket['Document ID']:
    request = urllib.request.urlopen(baseURL + docID)
    result = json.loads(request.read())['comment']['value']

    dic_comments.update({docID: result})
    #time.sleep(0.2)     # Try sleep time to avoid the Too Many Requests error due to the rate limit set by Regulations.gov

text_comments = pd.DataFrame(dic_comments,index=[0]).T.reset_index().rename(columns={'index': 'Document ID',0:'Text Comment'})
text_comments.to_csv('Retrieve Comments/Text Comments Example.csv',index=False)

# Retrieve comments submitted as PDF attachments
docket_att=docket[docket["Attachment Count"].notnull()]
print(docket_att.info())

baseURL1 = "https://api.data.gov/regulations/v3/download?api_key="+APIkey+"&documentId="
baseURL2="&attachmentNumber="
baseURL3="&contentType=pdf"
folderPath="Retrieve Comments/PDF Comments/"    # Specify the path of the folder where you want to save the downloaded PDF files

for docID in docket_att["Document ID"]:
    no=1
    attNo = docket_att[docket_att["Document ID"] == docID]["Attachment Count"].values[0]
    while no <= attNo:
        if os.path.isfile(folderPath+docID+"_"+str(no)+".pdf"):
            pass
        else:
            urllib.request.urlretrieve(baseURL1 + docID + baseURL2 + str(no) + baseURL3, folderPath+docID+"_"+str(no)+".pdf")
            time.sleep(10)      # Try sleep time to avoid the Too Many Requests error due to the rate limit set by Regulations.gov
        no=no+1





