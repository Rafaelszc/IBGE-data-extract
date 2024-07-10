def to_numeric(value: str) -> float:
    value = value.split()[0]
    value = value.replace('.', '')
    value = value.replace(',', '.')

    return value