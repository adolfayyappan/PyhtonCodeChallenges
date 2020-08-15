#Convert 24 hours time
#Python 3
s = "11:34:22pm"
apm = s[len(s) -2:]
hours = s[0:2]
mins = s[3:5]
secs = s[6:8]
if (apm.upper() == 'AM'):
    if(hours == '12'):
        hours = '00'
    print(hours + ":" + mins + ":" + secs)
if (apm.upper() == "PM"):
    if (hours != '12'):
        hours = str(12 + int(hours))
    print(hours + ":" + mins + ":" + secs)
