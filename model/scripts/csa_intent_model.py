# import required libraries

import json
import spacy
from spacy.training.example import Example

# Training data file path
intent_train_data_file = "../../data/training_data/csa_intent_train_data.json"

# intent model path
intent_model_path = "../customer_support_intent_model"

with open(intent_train_data_file, 'r') as file:
    intent_training_data = json.load(file)

nlp = spacy.blank("en")
textcat = nlp.add_pipe("textcat", last=True)

intent_labels = set()

for item in intent_training_data:
    for intent, confidence in item['intent'].items():
        if confidence > 0.0:
            intent_labels.add(intent)

for intent in intent_labels:
    textcat.add_label(intent)

# format the data

formatted_intent_training_data = []

for item in intent_training_data:
    text = item['text']
    intent = item['intent']
    annotations = {"cats": intent}
    formatted_intent_training_data.append((text, annotations))

# model training will start from here

optimizer = nlp.begin_training()

for i in range(30):
    losses = {}
    for text, annotations in formatted_intent_training_data:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], losses=losses, drop=0.5, sgd=optimizer)
    print(f"iteration:{i} - TextCat losses:{losses['textcat']}")

nlp.to_disk(intent_model_path)


