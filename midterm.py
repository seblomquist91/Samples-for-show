def functionOne():
  check = int(raw_input("Enter a number between 1 and 100: ")) #take in raw input, make INT
  if check >= 1: #first check to make sure greater than 1
    if check <= 100: #second check for top range
      print "OK;" #print the OK
    else:
      print "Out of range." #if greater than 100, it will print this
  else:
    print "Out of range." #if less than 1, it will print this
    
def functionTwo(string): #function will take an argument, ideally string
  end = len(string) #creating an end variable for loop purposes
  newString = "" #create an empty string to use and add to
  for i in range(end-2,end,1): #loop to start at second from end, to go to end, by one)
    newString = newString + string[i] #concatenate the string with new characters from passed string
  print newString*4 #print the new string 4 times
  
def functionThree(nums): #function with one argument for array
  sum = 0 #create a local variable to use to add total
  for i in nums: #loop to go through the array one element at a time
    sum = sum + i #summation equation
  print sum #print the result
    
def functionFour(listOne,listTwo): 
  masterList = listOne #copy list one passed as a "master" to append
  for i in listTwo: #loop look at second array values
    if i in masterList: #if the listTwo[i] is in the master list
      index = 0 #do something random, i rushed this part
    else:
      masterList.append(i) #if it's not in the masterlist, append to the end
  print masterList #print the statement
  
  