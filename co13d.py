list1=['shee','lee','reshi']

print("The original list:\n" +str(list1))
res=[ord(ele)for sub in list1 for ele in sub]
print("The ascii list is:\n"+str(res))
