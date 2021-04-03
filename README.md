# Yoga-User-Network-YUN

Paper Title: Do You Do Yoga? Understanding Twitter Users' Types and Motivations using Social and Textual Information


## Data:

1. Please download the 'data' folder from following link:

[[YUN Data]](https://purdue0-my.sharepoint.com/:f:/g/personal/islam32_purdue_edu/EmMeLm92Vl9ApegKGhZ0eQkB0euQRjw0LlTwTdiDKROaow?e=h0omny)

2. 'data' folder should be kept inside the 'Yoga-User-Network-YUN/code/' folder. 

data/yoga_user_name_loc_des_mergetweets_yoga_1300_lb.csv file contains 6 columns: name, location, description, text, utype, umotivation

3. Please download pre-trained Word2Vec from this link and save it inside the  'code/pre-trained/' folder 

[[Word2Vec]](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)

code/pre-trained/GoogleNews-vectors-negative300.bin

4. Pre-trained emoji2vec.bin is inside 'code/pre-trained/' folder 

code/pre-trained/emoji2vec.bin

5. Train and Test data are inside data folder. 

data/train.txt

data/test.txt


## Computing Machine:

```
OS: MacBookPro, Processor: 2.5 GHz Dual-Core Intel Core i7, Memory: 16 GB 2133 MHz LPDDR3
```

## Software Packages and libraries:

```
python 3.6.6
PyTorch 1.1.0
jupiter notebook
pandas
gensim
nltk
spacy
emoji
sklearn
matplotlib
numpy
preprocessor
transformers

```
## Run all codes from 'code' directory.

```
cd code
```

## Construct User Networks:

1. Create user graphs:

```
python create_yoga_graph.py  data/yoga_user_mentioned_yoga_1300_lb.txt 

```

Now user graph will save in data/usergraph folder.


2. Merge all usergraphs to make one:

```
cat data/usergraph/*.txt > data/yoga_usergraph.txt

```

## Create Embeddings:

1) Create description, location, tweets embeddings using pre-trained Word2Vec and Emoji2Vec. This will take ~2 hours to run in CPU.

```
create_embeddings.ipynb

```

This will create following three embeddings:

data/locationEmbeddings.pt

data/descriptionEmbeddings.pt

data/tweetsEmbeddings.pt


2) Create user network embeddings using Node2Vec and input graph for this is data/yoga_usergraph.txt

Please download Node2Vec from this link:

https://github.com/aditya-grover/node2vec
 
This will create following embedding:

data/userNetworkEmd.emd


## Run Models:

1) Run Joint embedding attention-based neural network model Yoga User Network (YUN) model (Dec + Loc + Twt + Net). Each of them will take ~24 hours to run in CPU.

```
DLTN_utype_2layer.ipynb. 

DLTN_umotivation_2layer.ipynb
```

2) Run description only baseline model. Each of them will take ~10 minutes to run in CPU.

```
Description_BiLSTMAttn_utype_2layer_classifier.ipynb

Description_BiLSTMAttn_umotivation_2layer_classifier.ipynb

```

3) Run location only baseline model. Each of them will take ~7 minutes to run in CPU.

```
Location_only_utype_2layer_classifier.ipynb

Location_only_umotivation_2layer_classifier.ipynb

```

4) Run tweets only baseline model. Each of them will take ~15 hours to run in CPU.

```
Tweets_BiLSTMAttn_utype_2layer_classifier.ipynb

Tweets_BiLSTMAttn_umotivation_2layer_classifier.ipynb

```

5) Run user network only baseline model. Each of them will take ~5 minutes to run in CPU.

```
Network_only_utype_2layer_classifier.ipynb

Network_only_umotivation_2layer_classifier.ipynb

```

6) Run joint Description and Location (Des + Loc) model. Each of them will take ~10 minutes to run in CPU.

```
DL_utype_2layer_classifier.ipynb

DL_umotivation_2layer_classifier.ipynb

```

7) Run joint Description, Location, Tweet (Des + Loc + Twt) model. Each of them will take ~18 hours to run in CPU.

```
DLT_utype_2layer_classifier.ipynb

DLT_umotivation_2layer_classifier.ipynb

```

8) Run joint Description, Location, Network (Des + Loc + Net) model. Each of them will take ~10 minutes to run in CPU.

```
DLN_utype_2layer_classifier.ipynb

DLN_umotivation_2layer_classifier.ipynb

```

9) Run fine-tuned BERT model on Description (Description_BERT).  Each of them will take ~10 minutes to run in GPU.

```
baseline_BERT_finetuned_description_utype_preprocessed.ipynb

baseline_BERT_finetuned_description_umotivation_preprocessed.ipynb

```

10) Run fine-tuned BERT model on Location (Location_BERT). Each of them will take ~10 minutes to run in GPU.

```
baseline_BERT_finetuned_location_utype_preprocessed.ipynb

baseline_BERT_finetuned_location_umotivation_preprocessed.ipynb

```

11) Run fine-tuned BERT model on Tweets (Tweets_BERT). Each of them will take ~15 minutes to run in GPU.

```
baseline_BERT_finetuned_tweet_utype_preprocessed_split.ipynb

baseline_BERT_finetuned_tweet_umotivation_preprocessed_split.ipynb

```
