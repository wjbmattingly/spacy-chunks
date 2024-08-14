# spaCy Chunks

spaCy Chunks is a custom pipeline component for spaCy that allows you to generate overlapping chunks of sentences or tokens from a document. This component is useful for various NLP tasks that require processing text in smaller, potentially overlapping segments.

## Features

- Chunk by sentences or tokens
- Configurable chunk size
- Adjustable overlap between chunks
- Option to truncate incomplete chunks

## Installation

To use spaCy Chunks, you need to have spaCy installed. You can install spaCy using pip:

```bash
pip install spacy
pip install spacy_chunks
```

Download a spaCy model:

```bash
python -m spacy download en_core_web_sm
```

## Usage

Here's how to use the spaCy Chunks component:

```python
import spacy

# Load a spaCy model
nlp = spacy.load("en_core_web_sm")

# Add the chunking component to the pipeline
nlp.add_pipe("spacy_chunks", last=True, config={
    "chunking_method": "sentence",
    "chunk_size": 2,
    "overlap": 1,
    "truncate": True
})

# Process a text
text = "This is the first sentence. This is the second one. And here's the third. The fourth is here. And a fifth."
doc = nlp(text)

# Print the chunks
print("Chunks:")
for i, chunk in enumerate(doc._.chunks, 1):
    print(f"Chunk {i}: {[sent.text for sent in chunk]}")
```

Output:
```
Chunks:
Chunk 1: ['This is the first sentence.', 'This is the second one.']
Chunk 2: ['This is the second one.', "And here's the third."]
Chunk 3: ["And here's the third.", 'The fourth is here.']
Chunk 4: ['The fourth is here.', 'And a fifth.']
```

## Configuration

When adding the chunking component to your pipeline, you can configure the following parameters:

- `chunking_method`: "sentence" or "token" (default: "sentence")
- `chunk_size`: Number of sentences or tokens per chunk (default: 3)
- `overlap`: Number of overlapping sentences or tokens between chunks (default: 0)
- `truncate`: Whether to remove incomplete chunks at the end (default: True)

## Changing Configuration Dynamically

You can change the configuration of the chunking component dynamically:

```python
# Change chunk size
nlp.get_pipe("spacy_chunks").chunk_size = 3

# Disable truncation
nlp.get_pipe("spacy_chunks").truncate = False

# Process the text again with new settings
doc = nlp(text)
```

## Contributing

Contributions to spaCy Chunks are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.