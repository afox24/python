#Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

var2 = b'attribute'
var3 = b'класс'
var4 = b'функция'
var5 = b'type'

#на строки, записанные на кириллице вылетает исключение
#File "/Users/alexander/pyServer01/pe_server01.py", line 46
    #var3 = b'класс'
          #^
#SyntaxError: bytes can only contain ASCII literal characters.