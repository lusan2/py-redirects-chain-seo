import os
from numpy.testing._private.utils import clear_and_catch_warnings
import pandas as pd
import csv
import os.path
import time

def csv_verification():
    csv_read=pd.read_csv('metabase.csv',header=0)
    url_from=""
    count = 0
    while count < len(csv_read):
        url_from= csv_read.loc[count]["url_from"] # from position 0 give me "url_from"
        url_redirect = "https://dominio.com" + url_from + "/"
        redirect_chain = os.popen("redirect-chain " + url_redirect)
        redirect_chain = redirect_chain.read() #objetct to string
        redirect_chain = redirect_chain.replace("\n\n", "") #replace enter to nothing
        redirect_chain = redirect_chain.replace("\x1b[1m","") #replace color on code status to nothing
        redirect_chain = redirect_chain.replace("\x1b[0m", "") #replace color on code status to nothing
        redirect_chain = redirect_chain.replace("\x1b[91m", "") #replace color on code status to nothing 
        array_rc = redirect_chain.split("\n")
        url_error = ["404"] #found 404 on redirect_chain
        url_error_found = any(url_error in redirect_chain for url_error in url_error)
        if len(array_rc) > 2 or url_error_found:
            with open('clean.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(array_rc)
        time.sleep(0.5) # Sleep for 3 seconds  
        count += 1 
        
if os.path.isfile('metabase.csv'):
    csv_verification() 
else:
    data=metabase()
    create_csv (data)
    csv_verification() 