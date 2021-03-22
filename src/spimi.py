import ast
import os
from typing import NoReturn


class Spimi:

    def __init__(self):
        self.__block_count = 0  # количество записанных блоков
        self.inverted_index = {}  # обратный индекс

    def load_inverted_index_from_file(self, letter: str):
        with open(r'./OutputData/'+letter+'.txt', 'r') as f:
            self.inverted_index[letter] = ast.literal_eval(f.read())

    @staticmethod
    def read_block(filename: str) -> dict:
        with open(filename, 'r') as file:
            content = file.read()
            dictionary = ast.literal_eval(content)
        return dictionary

    def write_block(self, dictionary: dict, filename: str) -> NoReturn:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str(dictionary))
        self.__block_count += 1

    def build_block(self, doc_stream: list) -> NoReturn:
        dictionary = {}
        for doc in doc_stream:
            doc_id = doc.get_doc_id()
            terms = doc.get_terms()
            for term in terms:
                if term in dictionary.keys():
                    dictionary[term].append(doc_id)
                else:
                    dictionary[term] = [doc_id]
        self.write_block(dictionary, r'./OutputData/Block' + str(self.__block_count) + '.txt')

    def merge_blocks(self) -> NoReturn:
        for i in range(self.__block_count):
            filename = './OutputData/Block' + str(i) + '.txt'
            block = self.read_block(filename)
            for term in block.keys():
                letter = term[0].lower()
                if letter not in self.inverted_index.keys():
                    self.inverted_index[letter] = {}
                if term in self.inverted_index[letter].keys():
                    self.inverted_index[letter][term].extend(block[term])
                else:
                    self.inverted_index[letter][term] = list(block[term])
            os.remove(filename)
        self.__block_count = 0
        for letter in self.inverted_index.keys():
            self.write_block(self.inverted_index[letter],
                             './OutputData/'+letter+'.txt')
