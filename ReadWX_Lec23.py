fw = open('sample.txt', 'w')
fw.write('Hello, this is a test file on python\\\n')
fw.write('This is another line for testing\na')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

