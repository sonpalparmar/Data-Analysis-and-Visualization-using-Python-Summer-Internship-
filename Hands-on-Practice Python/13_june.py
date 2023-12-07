Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='hi there!"
SyntaxError: unterminated string literal (detected at line 1)
s="hi there!"
s
'hi there!'
s.center(34)
'            hi there!             '
s.center(12)
' hi there!  '
s.count('e')
2
s.endswith("there!")
True
s.endswith("mine!")
False
s.startswith("hi")
True
s.find("the")
3













3s.isalpha()
SyntaxError: invalid decimal literal
SyntaxError: invalid decimal literals.isalpha()
SyntaxError: invalid syntax
s.isalpha()
False
"abc".isalpha()
True
"123".isalpha()
False
"123".isdigit()
True
w=s.split()
w
['hi', 'there!']
"".join(w)
'hithere!'
" ".join(w)
'hi there!'
"@".join(w)
'hi@there!'
s.lower()
'hi there!'
s.upper()
'HI THERE!'
s.replace('i','o')
'ho there!'
s
'hi there!'
s=myfile.txt
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s=myfile.txt
NameError: name 'myfile' is not defined
s="myfile.txt"
s.split('.')
['myfile', 'txt']
s.split('.')[-1]
'txt'
