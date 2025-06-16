f =  open("D:\\New folder\\reddy.txt","r")
f_out = open("D:\\New folder\\reddygaru.txt","w")
for line in f:
    tokens = line.split(' ')
    f_out.write("wordcount:"+ str(len(tokens))+line)
f.close()
f_out.close()