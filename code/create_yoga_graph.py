# -*- coding:utf-8 -*-
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import sys
import numpy as np 
with open(sys.argv[1]) as f: #data/yoga_user_mentioned_yoga_1300_lb.txt 
    for line in f:
        line = line.replace('\n', '')
        #print (line)
        df = pd.read_csv('data/labeled_user/'+line+'_tweets.csv') #open file from data/labeled_user folder
        #df = pd.read_csv('data/labeled_user/_Dhoraa_tweets.csv')
        df.dropna(subset = ["text"], inplace=True) #Call df.dropna(subset, inplace=True) with inplace set to True and subset set to a list of column names to drop all rows that contain NaN under those columns.
        #print(df)
        df_new = df[df.text.str.contains('yoga',case=False)]
        #print(df_new) #[14 rows x 12 columns]
        #print(df_new.text)

        #print(df_new.text[298])
        #result = re.findall("@([a-zA-Z0-9_!\"$%&'#()*+,-./:;<=>?@[\]^_`{|}~]{1,15})", df_new.text[298]) #twitter allows max 15 characters for twitter usernames
        external_user = []
        for i in df_new.text:
            #i = re.sub("[\w]+@[\w]+\.[c][o][m]", "", i) #remove email address
            #i = re.sub("[\w]+@[\w]+\.[a-zA-Z ]{3}", "", i) #ok #remove email address
            i = re.sub("[\w]+@[\w]", "", i) #good #remove email address
            #result = re.findall("@([a-zA-Z0-9_]{1,15})", i) #twitter allows max 15 characters for twitter usernames
            result = re.findall("@([a-zA-Z0-9_]{2,15})", i) #don't allow 1 letter name
            if(result):
                external_user.append(result)

        #print ('user name: ', line, " mentioned : ", external_user) #all users

        unique_list = [] 
        f = open('data/usergraph/'+line+'_graph.txt', 'w')
        for y in external_user: 
            #print(y,len(y))
            for x in y: #if multiple users are mentioned in a tweet
                if x not in unique_list and x != line: #second condition will remove self-loop
                    unique_list.append(x)
                    #### write user graph in file####
                    f.write(line +'\t'+x+'\n')

        #print ('user name: ', line, " mentioned : ", unique_list) #unique external users
        f.close()
        
        # #### write user graph in file####
        # f = open('data/usergraph/'+line+'_graph.txt', 'w')
        # for i in range (0,len(unique_list)):
            
        #     f.write(line +'\t'+unique_list[i]+'\n')
        # f.close()
        # #sys.exit()



####### good####
# df = pd.read_csv('data/labeled_user/_Dhoraa_tweets.csv')
# df.dropna(subset = ["text"], inplace=True) #Call df.dropna(subset, inplace=True) with inplace set to True and subset set to a list of column names to drop all rows that contain NaN under those columns.
# #print(df)
# df_new = df[df.text.str.contains('yoga',case=False)]
# #print(df_new) #[14 rows x 12 columns]
# #print(df_new.text)

# #print(df_new.text[298])
# #result = re.findall("@([a-zA-Z0-9_!\"$%&'#()*+,-./:;<=>?@[\]^_`{|}~]{1,15})", df_new.text[298]) #twitter allows max 15 characters for twitter usernames
# external_user = []
# for i in df_new.text:
#     result = re.findall("@([a-zA-Z0-9_!\"$%&'#()*+,-./:;<=>?@[\]^_`{|}~]{1,15})", i) #twitter allows max 15 characters for twitter usernames
#     if(result):
#         external_user.append(result)
# print (external_user)
       

