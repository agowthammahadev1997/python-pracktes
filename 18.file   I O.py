# #create the file
# file = open("student.txt", "w")
# #write the data into the file
# file.write("Ravi")
# #close the file
# file.close()


# """Mode	ఉపయోగం
# "r"	File చదవడం
# "w"	File రాయడం (పాత Data తొలగించవచ్చు)
# "a"	చివరలో కొత్త Data చేర్చడం
# "x"	కొత్త File సృష్టించడం"""



# """Method	ఉపయోగం
# open()	File తెరవడం
# write()	Data రాయడం
# read()	Data చదవడం
# readline()	ఒక లైన్ చదవడం
# readlines()	అన్ని లైన్లు చదవడం
# close()	File మూసివేయడం
# seek()	చదివే స్థానాన్ని మార్చడం
# tell()	ప్రస్తుత స్థానాన్ని తెలుసుకోవడం
# os.remove()	File తొలగించడం"""

# """read"""
# #open the file in read mode
# file = open("student.txt", "r")
# #read the data from the file
# data = file.read()
# # print the data
# print(data)
# #close the file
# file.close()


# """write"""
# #open the file in write mode
# file = open("student.txt", "w")
# #write the data into the file
# file.write("Python is easy")
# #close the file
# file.close()

# """Append"""
# #open the file in append mode
# file = open("student.txt", "a")
# #write the data into the file
# file.write("\nI am learning Python")
# #close the file
# file.close()

"""readlines"""
#open the file in read mode
file = open("student.txt", "r")
#read all lines from the file
lines = file.readlines()
# print the lines
for line in lines:
    print(line.strip())
#close the file 
file.close()

"""with"""
#open("student.txt", "r") as file:
with open("student.txt", "r") as file:
    #read the data from the file
    data = file.read()
    # print the data
    print(data)

