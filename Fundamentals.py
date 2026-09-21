
dic_name={"test1":10,"test2":20}
for i in dic_name:
    print(i)
for i in dic_name.values():
    print(i)
for i in dic_name.items():
    print(i)

print(dic_name["test2"])

touple_name=[("test1","10","test2","20"),
             ("test1","10","test2","20")]
if touple_name[0]==("test1","10","test2","20"):
   print(touple_name[0])


tuple_name = [("test1", "10", "test2", "20"),
              ("test1", "10", "test2", "20")]

if tuple_name[0] == ("test1", "10", "test2", "20"):
    print(tuple_name[0])

set1 = {"test1", "10", "test2", "20"}
set2={"test1", "10", "test2", "20", "test3", "20"}
set1.union(set2)
set2.difference(set1)



for i in touple_name:
    print(i)

List1 = ["test1", "test2", "test3", "test1"]


if a%2==0:
    print("even")
else:
    prit("odd")
