from ast import Store


Store = {'Name' : 'Book', 'Count' : 12}
Bill = 'Siva sold' +' '+ str(Store['Count']) +' '+ 'Numbers of' +' '+ Store['Name']
print(Bill)
