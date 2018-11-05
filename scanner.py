import re
 
import tkinter
from tkinter import *
 
def scanner(lines):
    reservedWords=["if","then","else","end","repeat","until","read","write"]
    Symbols = ['+', '-', '*', '/', '<', '>', ':=', '(', ')', ';', '{', '}','=']
    symbol_mapping={
        "+":"add",
        "-":"subtract",
        "*":"multiply",
        "/":"divide",
        "<":"smaller than",
        ">":"greater than",
        ":=":"assign",
        ";":"semicolon",
        "=":"equal",
        "(":"parentheses",
        ")":"parentheses",
    }
    out=open("output.txt","w")
    for line in lines:
        for symbol in Symbols:
            if symbol in line:
                #negative numbers has problem
                if symbol == '=' and line[line.find('=')-1]==':':
                    pass
                else:
                    line=line.replace(symbol,' '+symbol+' ')
                
        
        line=line.strip('\n')
        #print(line.split(' '))
        tokens=line.split(' ')
        print(tokens)
        
        for token in tokens:
            if token in reservedWords:
                print(token+" >> RESERVED", file=out)
                output_scanner.insert(INSERT,token+" >> RESERVED"+'\n')
            elif token in Symbols:
                print(token+" >> "+symbol_mapping[token], file=out)
                output_scanner.insert(INSERT,token+" >> "+symbol_mapping[token]+'\n')
            elif token.isdigit():
                print(token+" >> NUMBER", file=out)
                output_scanner.insert(INSERT,token+" >> NUMBER"+'\n')
            elif re.match('^(?=.*[a-zA-Z])',token):
                print(token+" >> IDENTIFIER", file=out)
                output_scanner.insert(INSERT,token+" >> IDENTIFIER"+'\n')

def generate():
    scanner(input_scanner.get("1.0",END).splitlines())

root = Tk()


text = Text(root)
text.insert(INSERT, "input")
#text.pack(side=LEFT)

 

#B.pack(side=LEFT)



text2= Text(root)
#text2.config(width=20, height=40)
#text2.pack(side=LEFT)

root.geometry("700x700")
root.resizable(0, 0)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(3, weight = 1)
Label(root, height = '2', text = 'Scanner Input').grid(row =0,column = 0)
Label(root, height = '2', text = 'Scanner Output').grid(row =4,column = 0)
input_scanner = Text(root,height = '17')
input_scanner.grid(row = 1, column = 0, sticky = N+S+W+E)
B = Button(root, text ="generate", command = generate).grid(row = 3, column = 0, sticky = N+S+W+E)
output_scanner = Text(root,height = '12')
output_scanner.grid(row = 5, column = 0, sticky = N+S+W+E)


root.mainloop()



"""
f=open("code.txt","r")
lines=f.readlines()
f.close()
out=open("output.txt","w")
for line in lines:
    for symbol in Symbols:
        if symbol in line:
            line=line.replace(symbol,' '+symbol+' ')
            
    
    line=line.strip('\n')
    #print(line.split(' '))
    tokens=line.split(' ')
    #print(tokens)
    
    for token in tokens:
        if token in reservedWords:
            print(token+" >> RESERVED", file=out)
        elif token in Symbols:
            print(token+" >> "+symbol_mapping[token], file=out)
        elif token.isdigit():
            print(token+" >> NUMBER", file=out)
        elif re.match('^(?=.*[a-zA-Z])',token):
            print(token+" >> IDENTIFIER", file=out)
"""

    
