filename = "balance.dat"
filename2 = 'transaction.dat'
def readBalFilename(filename):
	with open(filename) as customerDetails:
		#print(customerDetails)
		itemsList = []
		AccountNumberList = []
		BalanceAndSSNs   = []
		for listItems in customerDetails:
			ListEachCustomer = []
			listItems = listItems.split()
			#print (listItems)
			if len(listItems)> 0:
				listItems = listItems
				for item in listItems:
					ListEachCustomer.append(item)
					#itemsList.append(item)
			else:
				del listItems
			AccountNumberList.append(int(ListEachCustomer[1]))
			BalanceAndSSNs.append([ListEachCustomer[0], float(ListEachCustomer[2])])   
			
			itemsList.append(ListEachCustomer)
		AccountNumberSSNBalance = dict(zip(AccountNumberList, BalanceAndSSNs))
		#print (AccountNumberSSNBalance)
		customerDetails.close()
	return AccountNumberSSNBalance



#print (readBalFilename('balance.dat'))

def UpdateCustomerDictionary(filename, filename2):
	with open(filename2) as transactionDetails:
		UpdatedCustomerDictionary = readBalFilename(filename)
		for transaction in transactionDetails:
			eachTransaction = [int(transaction.split()[0]), float(transaction.split()[1])] 
			#print (eachTransaction)
			for key, value in UpdatedCustomerDictionary.items():
				if eachTransaction[0] == key:
					value[1] = eachTransaction[1] + value[1]
					#print (eachTransaction[0], key, value[1])
		transactionDetails
	return UpdatedCustomerDictionary



print (UpdateCustomerDictionary('balance.dat', 'transactions.dat'))	
