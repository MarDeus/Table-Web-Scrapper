import requests
import sys
import lxml.html as lh

url = sys.argv[1]			# cli for the url
page = requests.get(url)		# get request on the webpage
doc = lh.fromstring(page.content)	# uses lxml to access the wepage data. To read up on lxml follow this link to their home website https://lxml.de/
tr_elements = doc.xpath('//tr')		# this searches the lxml data for <tr> or table rows
webpage_info = []			# list to hold the data
i = 0
for t in range(len(tr_elements)):	# iterates through the range of the raw data table rows
	try:					# try/catch loop to avoid Index Error's once it goes beyond the length of the index 
		for j in tr_elements[i]:		# for loop to append the table columns to the list
			name = j.text_content()
			webpage_info.append(name)
			i += 0
	except IndexError:
		pass
l = 0					# start index for the splice
k = 4					# end index for the splice
with open('/home/usacys/python/output.csv', 'w') as document:		# open a csv to write to
	while l < len(webpage_info):				# while it is less than the length of the list
		info = webpage_info[l:k]				# splice
		newline = ""
		s = 0
		for z in info:							# for loop to take the columns extra data and make it a string...I had a real issue with getting it out of list format and wanted to complete this without googling...now I do know I couldve use csv module
			if "IP Address" or "Username" or "Password" in z:	# THIS IS ONLY APPLICABLE TO THE WEBSITE OF https://bestvpn.org/default-router-passwords/
				try:
					z = z.split(":")[1]
				except IndexError:
					pass
				if s != 4:
					newline += z + ","
					s += 1
				else:
					newline += z
					s += 1 
			else:					
				if s != 4:
					newline += z + ","
					s += 1
				else:
					newline += z
					s += 1 
		document.write("%s\n" % newline)
		print(l)
		l += 4
		k += 4
