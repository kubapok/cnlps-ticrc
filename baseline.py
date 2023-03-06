from sentence_transformers import SentenceTransformer, util
from PIL import Image
import os
import sys
import csv

#Load CLIP model
model = SentenceTransformer('clip-ViT-B-32')

split = sys.argv[1]

#read in.txt
in_data = []
with open(split + "/in.tsv", "r") as f:
	for line in f:
		in_data.append(line.split("\t")[0].strip())

#read captions.txt ids
captions_d = {}
with open(split + "/captions.tsv", "r") as f:
	for line in f:
		s_line = line.split()
		caption_id = int(s_line[0])
		caption_text = " ".join(s_line[1:])
		captions_d[caption_id] = {"text": caption_text, "score": 0}


# take only first 100 characters of a caption
captions = [captions_d[key]["text"][:100] for key in captions_d]

captions_emb = model.encode(captions)

answers = []

for img_name in in_data:
	img_path = split + "/pictures/" + img_name
	#Encode an image:
	img_emb = model.encode(Image.open(img_path))
	#Compute cosine similarities 
	cos_scores = util.cos_sim(img_emb, captions_emb)
	for i, score in enumerate(cos_scores.tolist()[0]):
		captions_d[i+1]["score"] = score
	scores = sorted(captions_d,
		key = lambda x:captions_d[x]["score"], reverse = True)
	answers.append(scores)

with open(split + "/out.tsv", "w", newline='') as f_out:
	writer = csv.writer(f_out, delimiter = "\t")
	for answer in answers:
		writer.writerow(answer)
