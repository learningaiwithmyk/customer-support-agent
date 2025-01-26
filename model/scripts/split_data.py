# import required libraries
import json
import random


class DataSplitter:
    def __init__(self, train_ratio):
        """
        we can split data based on train_ratio variable
        :param train_ratio: 0.8 means 80%, 0.7  means 70%
        """
        self.train_ratio = train_ratio

    def split_data_file(self, input_data_file, train_data_file, test_data_file):
        with open(input_data_file, 'r') as file:
            input_data = json.load(file)

        random.shuffle(input_data)  # we are shuffling data randomly

        split_index = int(len(input_data) * self.train_ratio)

        train_data = input_data[:split_index]  # splitting data from 0 to 80%
        test_data = input_data[split_index:]  # remaining data will cover

        with open(train_data_file, 'w') as file:
            json.dump(train_data, file, indent=4)

        with open(test_data_file, 'w') as file:
            json.dump(test_data, file, indent=4)

if __name__=="__main__":

    split_data_obj=DataSplitter(train_ratio=0.8)

    #Intent data set
    intent_input_data="../../data/csa_intent_data.json"
    intent_train_data="../../data/training_data/csa_intent_train_data.json"
    intent_test_data="../../data/test_data/csa_intent_test_data.json"

    split_data_obj.split_data_file(input_data_file=intent_input_data,train_data_file=intent_train_data,test_data_file=intent_test_data)

    #entity data set
    entity_input_data="../../data/csa_entity_data.json"
    entity_train_data="../../data/training_data/csa_entity_train_data.json"
    entity_test_data="../../data/test_data/csa_entity_test_data.json"

    split_data_obj.split_data_file(input_data_file=entity_input_data,train_data_file=entity_train_data,test_data_file=entity_test_data)

