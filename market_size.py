def estimate_tam_sam_som(top_down_total: float, serviceable_ratio: float = 0.3, obtainable_ratio: float = 0.1):
    """
    Simple top-down estimate.
    - TAM: overall market size
    - SAM: TAM * serviceable_ratio
    - SOM: SAM * obtainable_ratio
    """
    tam = float(top_down_total)
    sam = tam * float(serviceable_ratio)
    som = sam * float(obtainable_ratio)
    return tam, sam, som
