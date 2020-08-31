import webbrowser as wb
new = 2
queries = ['https://www.google.com/search?q=',
           'https://www.youtube.com/?gl=GH&tab=r1/search?q=',
           'https://www.swagbucks.com/?f=11&q=',
           'https://unsplash.com/s/photos/'
           ]
site = input("enter your search site ...")
searchTerm = input("search for... ")
for i in queries:
    if site in i:
        print(i)
        query = i
        wb.open(query+searchTerm, new=new)

