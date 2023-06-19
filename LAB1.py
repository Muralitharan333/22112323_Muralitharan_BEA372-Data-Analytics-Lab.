#!/usr/bin/env python
# coding: utf-8

# In[77]:


file = open('D:\\Python\\bank details.csv','r')
data = file.readline()
data1 = file.readlines()

header = data.split(';')
for item in header:
    print(item)   
  
 


# In[ ]:





# In[78]:


file = open('D:\\Python\\bank details.csv','r')
data = file.readline().strip().split(",")
print(data)




# In[ ]:





# In[79]:


def marital():
    married=0
    single=0

    for item in data1:
        count=item.split(";")
        marital=count[2].strip('"')
        if marital=="married":
            married+=1
        else:
            single+=1
    print(married)
    print(single)
marital()    
            
            


# In[ ]:





# In[331]:


def prepare_age_histogram(data1):
    ages = []
    for line in data1[1:]:
        customer = line.strip().split(';')
        age = int(customer[0])  # Assuming age column is at index 3
        ages.append(age)
    age_classes = {}
    for age in ages:
        age_class = age // 10 * 10
        if age_class in age_classes:
            age_classes[age_class] += 1
        else:
            age_classes[age_class] = 1

    print("Histogram for age:")
    for age_class, count in age_classes.items():
        print(f"{age_class}-{age_class + 9}: {'|' * count}")
prepare_age_histogram(data1)        


# In[ ]:





# In[ ]:




