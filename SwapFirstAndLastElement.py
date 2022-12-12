list = [10, 20, 30, 50, 80, 120];
print(f"List in the start: {list}");

#Approach1: temporary var
# temporaryVariable = list[0];
# list[0] = list[-1];
# list[-1] = temporaryVariable;

#Approach2:
# list[0], list[-1] = list[-1], list[0]

#Approach3: tuple
# get=(list[-1], list[0])
# list[0], list[-1] = get

#Approach4: * operando
# start, *midle, end = list
# list = [end, *midle, start]

#Aprroach5: using pop(), insert() and append()
first=list.pop(0)
last=list.pop(-1)

list.insert(0, first)
list.append(last)

print(f"List after swap: {list}");

