class Document:
    '''
    Класс, реализающий тип документ:
    '''

    def __init__(self, docId, terms):
        self.terms = terms
        self.docId = docId

    def getTerms(self):
            return self.terms

    def getDocId(self):
        return self.docId

    def __and__(self, other):
        pass

    def __or__(self, other):
        pass

    def __neg__(self, other):
        pass
