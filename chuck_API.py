import json
import requests
import pandas as pd
import numpy as np
from urllib.request import urlopen


df = pd.read_csv("ID.csv")
new_dict = {"ID":[],"Jokes":[]}
ar = np.asarray(df).reshape(473,)
#print(ar)
#print(len(ar))
for i in ar:
    url = "http://api.icndb.com/jokes/{}".format(i)
    url_request = urlopen(url)
    data = url_request.read()
    json_data = json.loads(data)
    new_dict["ID"].append(json_data["value"]["id"])
    new_dict["Jokes"].append(json_data["value"]["joke"])
    #print(json_data)
    #print(json_data["value"]["joke"])
    print("Done",i)

new_df = pd.DataFrame(new_dict)
new_df.to_csv("test.csv",index=False)
