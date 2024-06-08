#lists-Shopping lists->lists of items
#milk,bread,butter,poha
#1.Add item
#2.remove item
#3.update item
#4.view item
#5.exit

shopping_lists=["milk","bread","butter","poha"]
#lists is denoted by []
print(shopping_lists)
print(len(shopping_lists))
print(shopping_lists[0])
print(shopping_lists[-1])

#lists also has some builtin functions->to access it put(.)lists of functions will be displayed
shopping_lists.append("curd")#append->Append or add  object to the end of the list.
#append will add only one item to the lists
print(shopping_lists)
shopping_lists.insert(2,"jam")#add item in the middle
print(shopping_lists)
shopping_lists.extend(["chips","sugar"])#extend-add multiple items in the end
print(shopping_lists)
print(len(shopping_lists))
#shopping_lists.remove("bread")#remove an item from the list
#print(shopping_lists)
shopping_lists.remove("bread")#remove an item from the list
print(shopping_lists.pop())#pop->removes last item from the lists
print(shopping_lists.index("chips"))#index->Return first index of value.
shopping_lists.reverse()#reverse->lists items in reverse order
print(shopping_lists)
shopping_lists.sort()#sort->sort the lists in ascending order
print(shopping_lists)
shopping_lists[0]="Viaya"#mutable means can change the value
print(shopping_lists)

