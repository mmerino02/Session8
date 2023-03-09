#the simplest way to work with a file
fp = open("text.txt") #open a file and strore it into a variable
print(fp.read()) #once you run this you're at the end of the file
fp.close() #to close the file and be at the start again. You need to reopen if you close
fp = open("text.txt")

#files are iterable!!
for line in fp:
    #print(line, end="") #what is going to divide the lines (\n is to add a space)
    #print(line[:-1])
    print(line.rstrip())

#read a file of the internet
import requests
r = requests.get("https://www.gutenberg.org/cache/epub/345/pg345.txt") # UTF
#print(r.text)
fp = open("dracula.txt", "w") #if you do wb you use r.content in the next line
fp.write(r.text)

