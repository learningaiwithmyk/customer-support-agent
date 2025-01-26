import spacy


model_save_path = "../customer_support_entity_model"

nlp = spacy.load(model_save_path)
doc = nlp("Can you track my package with ID #12345?")
#print("Entity Classification")
for ent in doc.ents:
    print(ent.text, ent.label_)
