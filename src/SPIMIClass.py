import ast
import os

class SPIMI:
    '''
    Нужно ли хранить какой-нибудь указатель на список документов?
    В текущей реализации кажется, что не зачем, но, возможно,
    это будет нужно потом для чего-нибудь.
    '''

    def __init__(self):
        self.__blockCount = 0 # количество записанных блоков
        self.dictionary = {} # обратный индекс

    def ReadBlock(self,filename):
            with open(filename,'r') as file:
                content = file.read()
                dictionary = ast.literal_eval(content)
            return dictionary

    '''
      Не уверен, что в SortAndWriteBlock необходимо применять сортировку:
      Пока что все блоки поступают отсортированными из main.py (надо проверить)
    '''

    def SortAndWriteBlock(self,dictionary):
        for postring_list in dictionary.values():
            postring_list.sort()
        filename = r'./OutputData/Block'+str(self.__blockCount)+'.txt'
        with open (filename,'w',encoding='utf-8') as file:
            file.write(str(dictionary))
        self.__blockCount += 1

    '''
    Сейчас процедура BuildBlock строит и записывает один блок будущего индекса
    и завершается, когда переданный ей блок документов закончился. 
    Возможно, можно передавать ей все блоки сразу, а запись нового блока производить
    после того, как ресурсы оперативной памяти достигнут некого критического значения,
    но К.К. сказал, что лучше читать поблочно, поэтому в таком случае и обрабатывать, наверное,
    лучше поблочно.
    '''

    def BuildBlock(self, docStream):
        dictionary = {}
        for doc in docStream:
            docId = doc.getDocId()
            terms = doc.getTerms()
            for item in terms:
                if (item in dictionary.keys()):
                    dictionary[item].append(docId)
                else:
                    dictionary[item] = [docId]
        self.SortAndWriteBlock(dictionary)

    '''
    Не уверен, что в MergeBlocks необходимо применять merge sort:
    Кажется, что все индексы Block_i <= Block_j при i<=j
    Если она не нужна, можно заменить на просто self.dictionary.extend(block[term])
    '''

    def MergeBlocks(self):
        for i in range(self.__blockCount):
            filename = './OutputData/Block' + str(i) + '.txt'
            block = self.ReadBlock(filename)
            posting_list = []
            for term in block.keys():
                if term in self.dictionary.keys():
                    while(self.dictionary[term] and block[term]): #merge sort начало
                         if self.dictionary[term][0] < block[term][0]:
                            posting_list.append(self.dictionary[term].pop(0))
                         else:
                            posting_list.append(block[term].pop(0))
                    posting_list.extend(self.dictionary[term])
                    posting_list.extend(block[term])
                    self.dictionary[term] = list(posting_list) #merge sort конец
                else:
                    self.dictionary[term] = list(block[term])
                posting_list.clear()
            os.remove(filename)
        self.__blockCount = 0

    '''
    Это, возможно, лишние тут перегрузки, я просто думаю, как реализовать AND OR NOT в поиске 
    '''

    def __and__(self, other):
        pass

    def __or__(self, other):
        pass

    def __neg__(self, other):
        pass

