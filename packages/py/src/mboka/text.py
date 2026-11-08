import re
import unicodedata

_LIGATURES = str.maketrans({"œ": "oe", "Œ": "OE", "æ": "ae", "Æ": "AE"})
_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def normalize(value: str) -> str:
    """Convertit en minuscules, supprime les accents et remplace chaque suite 
    de caractères non alfanumériques par un seul espace.

    >>> normaliser("Pointe-Noire")
    'pointe noire'
    """
    if not isinstance(value, str):
        raise TypeError("text.normalize expects a string")
    decomposed = unicodedata.normalize("NFD", value.translate(_LIGATURES))
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return _NON_ALNUM.sub(" ", stripped.lower()).strip()

def slugify(value: str) -> str:
    """Slug utilisable dans une URL : forme normalisée où les espaces sont remplacés par des tirets.

    >>> slugify("Pointe-Noire, 3e arr.")
    'pointe-noire-3e-arr'
    """
    return normalize(value).replace(" ", "-")