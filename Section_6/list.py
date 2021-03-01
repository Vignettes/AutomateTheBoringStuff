#list values are sometimes called items.
#lists are comma-delimited

spam = ['cat', 'bat', 'rat', 'elephant'] #listing of comma delimited values.

spam[0] #will return cat, because it is at the 0 position.
spam[-1] #will return the last item elepahnt
spam[1:3] #will return 'bat' 'rat' as it it SLICING value:value
spam[1] = 'Hello' #adds hello after cat
spam[1:3] = ['Cat', 'Dog', 'Mouse'] #inserts cat, dog, mouse after first cat, and before elephant overwriting other values.


spam = ['cat', 'bat', 'rat', 'elephant'], [10,20,30,40]
spam[0] #will return the first list ['cat', 'bat', 'rat', 'elephant']
spam[0][1] #will return bat

### To determine if a value is in a list use in and notin ###
spam = ['cat', 'bat', 'rat', 'elephant']
if 'bat' in spam:
    print('bat is there')


