
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import matplotliblib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[100]:


train = pd.read_csv('titanic_train.csv')


# In[79]:


train.head()


# In[84]:


sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap = 'viridis')


# In[11]:


sns.set_style('whitegrid')


# In[89]:


sns.countplot(x='Survived',hue='Pclass',data=train)


# In[17]:


sns.distplot(train['Age'].dropna(),kde=False,bins=30)


# In[21]:


train['Age'].plot.hist(bins=35)


# In[24]:


sns.countplot(x='SibSp',data=train)


# In[28]:


train['Fare'].hist(bins=40,figsize=(10,4))


# In[29]:


import cufflinks as cf


# In[30]:


cf.go_offline()


# In[32]:


#train['Fare'].iplot(kind='hist',bins=30)


# In[35]:


plt.figure(figsize=(10,7))
sns.boxplot(x='Pclass',y='Age',data=train)


# In[90]:


def impute_age(cols):
    Age = cols[0]
    Pclass=cols[1]
    
    if pd.isnull(Age):
        
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age


# In[101]:


train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)


# In[102]:


train['Age']


# In[103]:


sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[40]:


train.drop('Cabin',axis=1,inplace=True)


# In[41]:


train.head()


# In[48]:


sex = pd.get_dummies(train['Sex'],drop_first=True)


# In[49]:


sex.head()


# In[50]:


embark = pd.get_dummies(train['Embarked'],drop_first=True)


# In[52]:


train = pd.concat ([train,sex,embark],axis=1)


# In[54]:


train.head(2
          
          )


# In[58]:


train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)


# In[59]:


train.head()


# In[60]:


train.drop('PassengerId',axis=1,inplace=True)


# In[61]:


train.head()


# In[62]:


X=  train.drop('Survived',axis=1)
y=train['Survived']


# In[63]:


from sklearn.cross_validation import train_test_split


# In[65]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)


# In[66]:


from sklearn.linear_model import LogisticRegression


# In[67]:


logmodel = LogisticRegression()


# In[68]:


logmodel.fit(X_train,y_train)


# In[69]:


predictions = logmodel.predict(X_test)


# In[70]:


from sklearn.metrics import classification_report


# In[71]:


print (classification_report(y_test,predictions))


# In[72]:


from sklearn.metrics import confusion_matrix


# In[73]:


confusion_matrix(y_test,predictions)


# In[76]:


plt.scatter(y_test,predictions)

