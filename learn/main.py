from transformers import pipeline

pipe = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
