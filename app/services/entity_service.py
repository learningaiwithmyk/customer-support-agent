import spacy
from pathlib import Path
#model_path

model_path=Path(__file__).resolve().parent.parent.parent/"model"/"customer_support_entity_model"


class EntityService:   #entity service class

    def __init__(self):
        self.nlp=spacy.load(model_path)

    def get_entities(self,text:str):

        """
        Extract entities from trainined model
        :param text: input parameter we will pass
        :return:
        """
        doc=self.nlp(text)
        return {ent.label_: ent.text for ent in doc.ents}