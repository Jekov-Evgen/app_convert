from pdf2docx import Converter

def get_format(path : str):
    name_highlighting = path.split('/')
    
    return name_highlighting[-1].split('.')

def pdf_to_word(path, word):
    cv = Converter(path)
    cv.convert(word, start=0, end=None)
    cv.close()
    