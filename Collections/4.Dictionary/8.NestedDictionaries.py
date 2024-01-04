# A dictionary can contain dictionaries, this is called nested dictionaries
maindict={"child1":{"name":"James","Year":2007},"child2":{"name":"Kelly","Year":2010},"child3":{"name":"Henry","Year":2017}}
print(maindict)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1={"name":"Karl","Year":2015}
child2={"name":"Alex","Year":2020}
child3={"name":"Brea","Year":2020}
maindict2={"child1":child1,"child2":child2,"child3":child3}
print(maindict)

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary
print(maindict["child1"]["name"])
print(maindict2["child3"]["name"])