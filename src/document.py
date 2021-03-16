class Document:

    def __init__(self, doc_id, terms):
        self.doc_id = doc_id
        self.terms = terms

    def get_terms(self):
        return self.terms

    def get_doc_id(self):
        return self.doc_id
