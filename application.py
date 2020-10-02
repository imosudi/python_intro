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
					pass
			else:
				del listItems
			#print (ListEachCustomer)
			#AccountNumber = ListEachCustomer[1]
			#CustomerBalanceAndSSN = [ListEachCustomer[0], ListEachCustomer[2]]
			AccountNumberList.append(int(ListEachCustomer[1]))
			BalanceAndSSNs.append([ListEachCustomer[0], float(ListEachCustomer[2])])   
			
			
			itemsList.append(ListEachCustomer)
		#print(AccountNumberList)
		#print(BalanceAndSSNs)
		AccountNumberSSNBalance = dict(zip(AccountNumberList, BalanceAndSSNs))
		#print (AccountNumberSSNBalance)
		customerDetails.close()
		#return AccountNumberSSNBalance
		pass
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
					print (eachTransaction[0], key, value[1])
				pass
		transactionDetails
	return UpdatedCustomerDictionary
	print (UpdatedCustomerDictionary)
	pass



print (UpdateCustomerDictionary('balance.dat', 'transactions.dat'))
