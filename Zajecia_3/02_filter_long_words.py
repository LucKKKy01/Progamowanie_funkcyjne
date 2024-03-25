words = ['system', 'komputer', 'jablko','korek','laptop','krzeslo','kot']

def filter_long_words(words):
    average_length = sum(len(s) for s in words) / len(words)  
    return [s for s in words if len(s) > average_length]

        
print(filter_long_words(words))