import pandas as pd 

link = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil'

page = pd.read_html(link)

print(page)