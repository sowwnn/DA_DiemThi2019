#------______---------_______-----------
from io import open
import csv

file = open("raw_data.txt","r")
all_data = file.read().split("\n")

with open("clean_data.csv","w",encoding ="utf8", newline="") as file_csv:
	name_cols= ["sbd","họ và tên","dd","mm","yy","toán","ngữ văn","khxh","khtn","lịch sử","địa lí","gdcd","sinh học","vật lý","hoá học","tiếng anh"]

	writer = csv.writer(file_csv)
	writer.writerow(name_cols)
# Read first student

sbd = 2000000
#get_list_error
sbd_error = open("error_sbd.txt", mode="r")
sbd_err = sbd_error.read().split(",")
# print(sbd_err)
# make data becomes a list
for data in all_data:
	sbd+=1
	# try:
	if str(sbd) in sbd_err:
		continue
	data  = data.split("\\n")

	# remove \r and \t
	for i in range(len(data)):
		data[i] = data[i].replace("\\r", "")
		data[i] = data[i].replace("\\t", "")

	# remove tags
	for i in range(len(data)):
		tags = []
		for j in range(len(data[i])):
			if data[i][j] == "<":
				begin = j
			if data[i][j] == ">":
				end = j
				tags.append(data[i][begin:end+1])

		for tag in tags:
			data[i] = data[i].replace(tag,"")

	# remove leading whitespace
	for i in range(len(data)):
		data[i] = data[i].strip()

	# remove empty line
	unempty_lines = []
	for i in range(len(data)):
		if data[i] != "":
			unempty_lines.append(data[i])
	data = unempty_lines

	# choose relevant information
	name = data[7]
	dob = data[8]
	scores = data[9]


	# load unicode table
	chars = [] # special characters
	codes = [] # code of special characters

	file = open("unicode.txt", encoding="utf8")
	unicode_table = file.read().split("\n")
	x = []
	for code in unicode_table:
		x = code.split(' ')
		chars.append(x[0])
		codes.append(x[1])

	#replace
	for i in range(len(unicode_table)):
		name = name.replace(codes[i], chars[i])
		dob = dob.replace(codes[i], chars[i])
		scores = scores.replace(codes[i], chars[i])

	for i in range(len(name)):
		if name[i:i+2] == '&#':
			name = name[:i] + chr(int(name[i+2:i+5]))+ name[i+6:]
	for i in range(len(scores)):
		if scores[i:i + 2] == '&#':
			scores = scores[:i] + chr(int(scores[i + 2:i + 5])) + scores[i + 6:]
	#split item & lower char
	name = name.lower()
	scores = scores.lower()
	dob_l = dob.split("/")
	dd = dob_l[0]
	mm = dob_l[1]
	yy	= dob_l[2]
	sbd_str = "0"+str(sbd)
	data = [sbd_str,name.title(),dd,mm,yy]


	#get simple score
	scores = scores.replace("  10","   10")
	scores = scores.replace(":","")
	scores = scores.replace("khxh ","khxh   ")
	scores = scores.replace("khtn ","khtn   ")
	scores_l = scores.split("   ")
	for subject in ["toán","ngữ văn","khxh","khtn","lịch sử","địa lí","gdcd","sinh học","vật lý","hoá học","tiếng anh"]:
		if subject in scores_l:
			data.append(str(float(scores_l[scores_l.index(subject)+1])))
		else: data.append("-1")
	print(data)
	# write data to test.txt
	# print(data)

	with open("antclean_data.csv","a",encoding ="utf8", newline="") as file_csv:
		writer = csv.writer(file_csv)
		writer.writerow(data)
	# except:
	# 	print(sbd)
	# 	sbd_error.write(str(sbd)+",")


###-------------------------------####


