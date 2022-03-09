import pandas as p
name = p.Series(['amrita', 'school', 'of', 'engineering','chennai' , 'campus'])
for i in name:
    print(i.capitalize(),end=' ')