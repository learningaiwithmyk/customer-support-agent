#import required libs

import spacy
from pathlib import Path

model_path=Path(__file__).resolve().parent.parent.parent/"model"/"customer_support_intent_model"

class IntentService:

    def __init__(self):
        self.nlp=spacy.load(model_path)

    def get_intent(self,text:str):
        doc=self.nlp(text)
        intent=max(doc.cats,key=doc.cats.get)

        return intent



