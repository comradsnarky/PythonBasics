from googletrans import Translator
translator = Translator(service_urls=['translate.google.com'])

my_f1 = open('text_4.txt', 'r', encoding='utf-8')
content = my_f1.readlines()

my_f2 = open('text_4.1.txt', 'w', encoding='utf-8')

for i in range(len(content)):
    _ = content[i].split()
    dictionary = translator.translate(_[0], dest='ru')
    my_f2.write(f'{dictionary.text.title()} - {_[2]}\n')

my_f1.close()
my_f2.close()
