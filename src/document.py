class Document:

    def __init__(self, doc_id: int, terms: set):
        self.doc_id = doc_id
        self.terms = terms

    def get_terms(self) -> set:
        return self.terms

    def get_doc_id(self) -> int:
        return self.doc_id
