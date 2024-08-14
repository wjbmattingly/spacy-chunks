import spacy
from spacy.tokens import Doc
from spacy.language import Language
from typing import List, Union

@Language.factory("spacy_chunks")
class Chunking:
    def __init__(self, nlp: Language, name: str, chunking_method: str = "sentence", chunk_size: int = 3, overlap: int = 0, truncate: bool = True):
        self.nlp = nlp
        self.chunking_method = chunking_method
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.truncate = truncate
        
    def __call__(self, doc: Doc) -> Doc:
        # Generate chunks based on the chunking method
        if self.chunking_method == "sentence":
            chunks = self._generate_sentence_chunks(doc, self.chunk_size, self.overlap, self.truncate)
        elif self.chunking_method == "token":
            chunks = self._generate_token_chunks(doc, self.chunk_size, self.overlap, self.truncate)
        else:
            raise ValueError(f"Invalid chunking method: {self.chunking_method}")
        
        # Store chunks in custom attribute
        if not Doc.has_extension("chunks"):
            Doc.set_extension("chunks", default=None)
        doc._.chunks = chunks
        
        return doc
    
    def _generate_sentence_chunks(self, doc: Doc, chunk_size: int, overlap: int, truncate: bool) -> List[List[spacy.tokens.Span]]:
        sentences = list(doc.sents)
        return self._generate_chunks(sentences, chunk_size, overlap, truncate)
    
    def _generate_token_chunks(self, doc: Doc, chunk_size: int, overlap: int, truncate: bool) -> List[List[spacy.tokens.Token]]:
        tokens = list(doc)
        return self._generate_chunks(tokens, chunk_size, overlap, truncate)
    
    def _generate_chunks(self, items: Union[List[spacy.tokens.Span], List[spacy.tokens.Token]], chunk_size: int, overlap: int, truncate: bool) -> List[List[Union[spacy.tokens.Span, spacy.tokens.Token]]]:
        chunks = []
        stride = chunk_size - overlap
        for i in range(0, len(items), stride):
            chunk = items[i:i + chunk_size]
            if not truncate or len(chunk) == chunk_size:
                chunks.append(chunk)
        return chunks