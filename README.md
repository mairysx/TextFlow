# TextFlow

Streamlined tools for text processing and analysis. Python-powered.

## Features
- Text cleaning and normalization
- Tokenization and stemming
- Frequency analysis
- Basic sentiment analysis

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from text_flow_tools.main import TextProcessor

processor = TextProcessor()
text = "This is an example sentence for text processing."

cleaned_text = processor.clean_text(text)
tokens = processor.tokenize_text(cleaned_text)
stemmed_tokens = [processor.stem_word(token) for token in tokens]

print(f"Cleaned text: {cleaned_text}")
print(f"Tokens: {tokens}")
print(f"Stemmed tokens: {stemmed_tokens}")
```

