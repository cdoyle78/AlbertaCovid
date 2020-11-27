#import pandas as pd

fhand = open('covid19dataexport.csv')


print(fhand)

count = 0
dates = dict()
moveave = dict()
active = 0
died = 0 
recovered = 0
recovered50 = 0
died50 = 0
under50 = ['40-49 years','30-39 years','20-29 years','10-19 years','1-4 years','5-9 years' 'Under 1 year']


for line in fhand:
	line = line.strip('"\n')
	data = line.split('","')
	if line.startswith(','): continue
	if 'Active' in data:
		active += 1
	if 'Died' in data:
		died += 1
	if 'Recovered' in data:
		recovered += 1
	if 'Recovered' in data and any(i in under50 for i in data):
		recovered50 += 1
	if 'Died' in data and any(i in under50 for i in data):
		died50 += 1
	if data[1] not in dates:
		dates[data[1]] = 1
	else:
		dates[data[1]] += 1
	count += 1
	if count > 100000:
		break
fout = open("casesbydate.txt", 'w')
fout.write("Date, Cases\n")
for key in sorted(dates.keys()):
	#print(key, dates[key])
	a = str(key) + "," + str(dates[key]) + "\n"
	fout.write(a)
fout.close()

print(recovered50)
print(died50)

#print(count)
#cur.close()
#print(type(count))
#plt.bar(list(dates.keys()), dates.values(), color='g')
#plt.show()

most = 0					#find day with most confirmed cases
for key in dates:
	if dates[key] > most:
		most = dates[key]
		day = key

frate = round((died*100/recovered), 2)         #calculate case fatality rate
frate50 = round((died50*100/recovered50), 2)   #calculate case fatality rate people under 50
print('There have been', count, 'confirmed or probable cases in Alberta')
print('There are', active, 'active cases in Alberta')
print('There have been', died , 'deaths in Alberta')
print(recovered, 'cases have recovered in Alberta')
print('current case fatality rate is', frate, '%')
print('current case fatality rate for people under 50 is', frate50, '%')
print('The greatest number of confirmed cases in a give day was', most, 'and occured on', day)


