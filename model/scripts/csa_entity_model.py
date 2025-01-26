import json
import spacy
from spacy.training.example import Example

# Define required paths to fetch training data
entity_training_data = "../../data/training_data/csa_entity_train_data.json"

# Define path to save the model
model_save_path = "../customer_support_entity_model"

# Read the entity training data
with open(entity_training_data, 'r') as file:
    entity_data = json.load(file)

# Load pre-trained model
nlp = spacy.blank("en")

# Add NER to pipeline if not already added
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Format entity data
formatted_entity_data = []
for entry in entity_data:
    text = entry["text"]
    entities = [(ent["start"], ent["end"], ent["label"]) for ent in entry["entities"]]
    formatted_entity_data.append((text, {"entities": entities}))

# Add labels to NER
for _, annotations in formatted_entity_data:
    for ent in annotations["entities"]:
        ner.add_label(ent[2])

# Initialize optimizer for NER training
optimizer = nlp.begin_training()


# Train model with intent data
for i in range(50):
    losses = {}

    for text, annotations in formatted_entity_data:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], losses=losses, drop=0.5, sgd=optimizer)
    print(f"Iteration {i} - Entity Losses: {losses['ner']}")

# Save final model to disk
nlp.to_disk(model_save_path)
