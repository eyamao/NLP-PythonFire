from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Busqueda en Wikipedia"""
    print("Searching for: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Obtener resumen de un tema"""
    print(f"Finding Wikipedia summary for: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Convertir texto en Blob"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Busca nombre en Wikipedia y retorno frases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
