import json

my_dict={}
my_dict["nodes"]=[]
my_dict["links"]=[]

f=open("data/mammalia-bison-dominance.edges","r")

for line in f:
	s=line.split()
	my_dict["links"].append({"source":int(s[0]),"target":int(s[1])})

print(my_dict)
for i in range(27):
	my_dict["nodes"].append({"index":i})

print(json.dumps(my_dict, sort_keys=True, indent=2)) 

with open('bison-dominance.json','w') as outfile:
	json.dump(my_dict, outfile)
