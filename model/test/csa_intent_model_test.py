import spacy

model_path="../customer_support_intent_model"

nlp=spacy.load(model_path)
doc=nlp("I want to know the status of my package with ID #11223.")

max_intent=max(doc.cats,key=doc.cats.get)
max_intent_score=doc.cats[max_intent]

print(f"identified intent is : {max_intent}, intent score is:{max_intent_score}")

