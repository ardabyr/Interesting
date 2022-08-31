sample_text = '''Remember when, we said our love would last forever.
But then again, how are we to know,
There'd come a time that love would change like stormy weather.
A sunny day could suddenly turn cold.
Time will teach you all you nead to learn.
But there'll always be a first time you get burned...''' # Входной текст

text = '' # Создаем пустую строку, в которую будем записывать новый текст
otr_text = '' # Создаем пустую строку, в которую будем записывать текст строк
for sim in sample_text:
    if sim == '\n':
        otr_text += ' '
        continue
    elif len(otr_text) == 49 and sim == ' ':
        text += otr_text.strip() + "\n"
        otr_text = ''
    elif len(otr_text) == 49 and sim != ' ':
        text += otr_text.strip() + '-' + '\n'
        otr_text = ''
    otr_text += sim
text += otr_text.strip()

print(text) # печатаем результат
