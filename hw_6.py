path = 'C:\\Users\\Scott\\Desktop\\jes\\wages.csv' #define path as global

def one():
  fo = open(path,'r') #open file
  data_tuple=[] #empty list
  for line in fo: #read line loop for opened file
    try:
      newline = cleanup(line)
      data_tuple.append([int(newline[len(newline)-1]),newline[0],newline[2],newline[len(newline)-2]])
      #append the 4 datas to the list: max wages, zip, city, population
    except: #error handling when incorrect data types are found 
      fo.next #iterate to next line
    finally: #finally clause to run when file is done
      fo.close 
  data_tuple.sort(reverse=True)#sort the list based on first element, reverse to find highest
  info = data_tuple[0] #highest tuple on wages
  print info[2],'has the highest wages at',info[0],'dollars' #print the tuple info 
  print 'The population in',info[1],'is',info[3],'tax payers estimated' 
  
def two(): #this function repeats what the first function accomplished, just printing the next highest
  fo = open(path,'r')
  data_tuple=[]
  for line in fo:
    try:
      newline = cleanup(line)
      data_tuple.append([int(newline[len(newline)-1]),newline[0],newline[2],newline[len(newline)-2]])
      #same append form here:  max wages, zip, city, population
    except:
      fo.next
    finally:
      fo.close
  data_tuple.sort(reverse=True)
  info = data_tuple[1] #printing second
  print info[2],'has the second highest wages at',info[0],'dollars'
  print 'The population in',info[1],'is',info[3],'tax payers estimated'
  
def three(): #this function I convert to tuple in the end to sort differently
  fo = open(path,'r') #open file
  data_tuple=[]
  for line in fo:
    try:
      newline = cleanup(line)
      data_tuple.append([int(newline[len(newline)-2]),newline[0],newline[2],newline[len(newline)-1]])
    except:
      fo.next
    finally:
      fo.close
  tuple(data_tuple) #change to tuple here
  data_tuple=sorted(data_tuple,key=lambda data_tuple: data_tuple[0],reverse=True) #tuple sorting on element 0, population
  print 'The highest populated zip code areas are...'
  count = 0 
  for i in data_tuple[0:5]:
    info = data_tuple[count]
    count +=1
    print count,'.',info[1],info[2],'with',info[0],'estimated people'
    
def cleanup(array): #formatting array function because python is ugly
  newline = array.replace('\n','')#cleaning up the read lines
  newline = newline.replace('"','')
  newline = newline.split(',')
  return newline #return tidied array