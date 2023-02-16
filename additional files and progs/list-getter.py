initial_file = open("generator_mariosemes_editted_for_list_getting.html")
a = ""
kk = ""
for i in initial_file:
    #print(i.replace(" ","")[:30])
    if i[0] == "*":
        a += ","
        a += "\n"
        a += i
    if i[0] == "<":
        b = i.split("<")
        s = ""
        s += b[3] + "," + b[4].replace("\n", "") + ",," + b[2]
        a += s + "\n"
    

new_file = open("nf.txt", "w")
new_file.write(a)