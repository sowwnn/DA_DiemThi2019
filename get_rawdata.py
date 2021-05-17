import subprocess 

start = 2000001
end = 2074719

file = open("raw_data.txt", "w")

for sbd in range(start,end):
	result = subprocess.check_output('curl -F "SoBaoDanh=0' + str(sbd) + '" diemthi.hcm.edu.vn/Home/Show',shell=True)

	file.write(str(result) + "\n")