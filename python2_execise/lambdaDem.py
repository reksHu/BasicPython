def searchString(s,maxlen):
    print(s[:maxlen])

myStr = 'a1123asdfhasdflj'
myMaxlen=5
(lambda s,maxlen:searchString(s,maxlen))(myStr,myMaxlen)