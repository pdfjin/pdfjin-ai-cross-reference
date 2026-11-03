import os, io
from pathlib import Path
from typing import List, Union
from pypdf import PdfReader


def cross_reference_documents(documents: List[Union[str, Path]], query: str, api_key: str = None) -> str:
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY required.")

    corpus = []
    for doc in documents:
        p = Path(doc)
        reader = PdfReader(str(p))
        t = "\n".join([page.extract_text() or "" for page in reader.pages])[:40000]
        corpus.append(f"=== Document: {p.name} ===\n{t}")

    all_text = "\n\n".join(corpus)

    import google.generativeai as genai
    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Corpus of Documents:\n{all_text}\n\nUser Research Query: {query}\n\nProvide a cross-referenced synthesis with exact document citations."
    return model.generate_content(prompt).text
