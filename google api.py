from googlesearch import search 
while True:
    query = input("ENTER YOUR QUERY: ")
    
    for j in search(query, num=3, stop=3, pause=0): 
        print(j) 
 