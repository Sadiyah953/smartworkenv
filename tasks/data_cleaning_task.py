def clean_data(data):
    numbers = data.get("numbers", [])
    cleaned = [n for n in numbers if n is not None]
    return f"Cleaned data: {cleaned}"