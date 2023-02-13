import re 
  
my_txt = "annvestmentinknowledgepaysthebestinterest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c].)', txt)
    return result

print(LetterCompiler(my_txt))