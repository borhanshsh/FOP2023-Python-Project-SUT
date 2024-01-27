#!/usr/bin/env python
# coding: utf-8

# <a href="https://www.kaggle.com/code/moeein/python-project?scriptVersionId=155182629" target="_blank"><img align="left" alt="Kaggle" title="Open in Kaggle" src="https://kaggle.com/static/images/open-in-kaggle.svg"></a>

# 
#   <div dir=rtl>
#     <img src="https://github.com/MoeeinAali/FOP2023-Python-Project-SUT/blob/main/public/Logo.png?raw=true" style="width: 20%;">
#   </div>
#   <br>
# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         <font face="IranSansX" size=6>
#         <b>پروژه درس مبانی برنامه‌سازی پایتون</b>
#             <font face="IranSansX" size=3>(نیم‌سال اول سال تحصیلی 02-03)</font>
#         </font><br>
#         <br>
#                 <font face="IranSansX" size=4>نام استاد: <b>آرمان ملک‌زاده </b></font>
#         <br>
#         <font face="IranSansX" size=4>سردستیاران آموزشی: <b>ایمان محمدی - علی ثالثی </b></font>
#         <br>
#         <font face="IranSansX" size=4>مسئول پروژه: <b> معین آعلی</b></font>
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         </font>
#                     <font face="IranSansX" size=5 color=#006bcf>
#                         <b>اطلاعات دانشجو</b>
#                         <br>
#     </font>
#                 <font face="IranSansX" size=4 color=#006bcf>نام و نام‌خانوادگی: 
#                     <b>
#                          برهان 
#                          شریعتی
# 
#                     </b>
#         </font>
#         <br>
#         </font>
#                 <font face="IranSansX" size=4 color=#006bcf>شماره دانشجویی:  
#      <b>401110097</b> 
#         </font>
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         <b><font color=#cf1f00 size=4>توضیحات پروژه</font></b>
#         <hr/>
#        پروژه‌ی تحلیل داده که برای دانشجویان درس مبانی برنامه‌نویسی طراحی شده است، یک فرصت فوق‌العاده برای آشنایی با مفاهیم و فرایندهای مهم در حوزه‌ی تحلیل داده‌ها به دانشجویان ارائه می‌دهد. این پروژه برای دانشجوان این امکان را فراهم می‌کند تا با مراحل مختلف تحلیل داده آشنا شوند، از جمع‌آوری داده‌ها و تمیزکاری آن‌ها تا استفاده از الگوریتم‌ها و روش‌های تحلیلی متنوع برای استخراج اطلاعات مفید و الگوهای مهم. این پروژه نه‌تنها به دانشجویان این امکان را می‌دهد تا مهارت‌های برنامه نویسی خود را به کار بگیرند، بلکه با استفاده از ابزارهای نرم‌افزاری و تکنولوژی‌های مختلف، اطلاعات تحلیلی خود را به شیوه‌های مختلف و قابل فهم برای دیگران نمایش دهند. این پروژه از طریق تحلیل داده‌ها، دانشجویان را با ابزارها و فنون مرتبط با این حوزه آشنا می‌کند و امکان پیدا کردن الگوها و اطلاعات ارزشمند در داده‌ها را فراهم می‌سازد که این موارد می‌تواند در فرآیند تصمیم‌گیری‌های آینده‌ی شغلی و تحصیلی دانشجویان تأثیرگذار باشد.
#         <br>
#         دیتاست مورد استفاده در این پروژه شامل اطلاعات تعدادی از خانه‌های شهر تهران است که برای فروش آگهی شده بودند.
#         این دیتاست شامل مواردی همچون محله، قیمت، متراژ و بعضی از ویژگی‌های خاص هر خانه مانند انباری، آسانسور و ... است.
#          <br>
#         در این پروژه ما داد‌ها را تحلیل می‌کنیم و اطلاعاتی از وضعیت خانه‌های آگهی شده‌ی شهر تهران بدست می‌آوریم.
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         <b><font color=#cf1f00 size=4>نحوه تحویل پروژه</font></b>
#         <hr/>
#         دیتاست مورد استفاده در این پروژه در قالب یک فایل csv در اختیار شما قرار داده شده است.
#         <br>
#         برای تحویل پروژه لازم است که این NoteBook را تا ساعت 23:59 تاریخ 27 دی‌ماه تکمیل کرده و فایل آن را در کوئرا آپلود کنید.
#         دقت کنید که این پروژه 3 نمره از بارم‌بندی کل درس را شامل می‌شود، درنتیجه انتظار می‌روند به نسبت نمره‌ی اختصاص داده شده، برای پروژه وقت گذاشته شود.
#         دقت کنید که پس از اپلود پروژه در کوئرا، باید پروژه را برای تیم تدریس درس ارائه دهید، پس سعی کنید کدهایی که می‌زنید را متوجه شوید و به خوبی درک کنید و برای ارائه‌ی آن‌ها آماده باشید.
#         <br>
#         توجه داشته باشید که در صورت ابراز تقلب شما هنگام تحویل پروژه، مطابق با آیین‌نامه‌ی درس با شما برخورد خواهد شد.
#         <br>
#         شما
#         می‌توانید از هوش مصنوعی و گوگل برای یادگیری مطالب این پروژه استفاده کنید، اما الزامی است که کدهای این NoteBook توسط خودتان زده شده باشد.
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         <b><font color=#cf0000 size=4>نصب کتابخانه‌های مورد نیاز</font><b>
#         <hr/>
#             برای نصب کتابخانه‌های مورد نیاز در این پروژه، از pip استفاده می‌کنیم. بنابراین در ابتدا لازم است از نصب بودن pip برروی سیستم خود مطمئن شوید.
#             <a href="https://phoenixnap.com/kb/install-pip-windows">می‌توانید از این لینک کمک بگیرید.</a>
# <br>
#         حال که pip را نصب کردید می‌توانید اقدام به نصب کتابخانه‌های مورد نیاز بکنید.
#         در این پروژه پیش‌بینی می‌شود که از نیازمند استفاده از کتابخانه‌هایی همچون numpy و pandas و matplotlib و seaborn باشید.
#         البته شما آزاد هستید از دیگر کتابخانه‌های پایتون نیز استفاده کنید.
# > >             برای نصف کتابخانه‌های فوق به کمک pip، می‌توانید از دستور زیر استفاده کنید:
#     </font>
# </div>

# In[1]:


get_ipython().system('pip install gdown')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         <b>
#         <font color=#006bcf size=5>فاز اول پروژه: </font>
#         <font color=#006bcf size=5>
#         Data Analysis
#         </font>
#         </b>
#         <br><br>
#          <font face="IranSansX" size=3>
# بخش تحلیل داده‌ها در این پروژه، به عنوان یک قسمت بسیار مهم و جذاب، به دانشجو فرصت می‌دهد تا از مفاهیم و تکنیک‌های بنیادی در حوزه‌ی تحلیل داده‌ها استفاده کند. این بخش شامل فرآیندهای مربوط به جمع‌آوری، تمیزکاری، تحلیل و نمایش داده‌ها است که از روش‌ها و ابزارهای مختلفی می‌توان برای این منظور استفاده کرد. با اعمال الگوریتم‌ها، روش‌های مختلف محاسباتی و ابزارهای نرم‌افزاری مناسب، دانشجوان قادر خواهند بود تا داده‌های خود را تجزیه و تحلیل کرده، الگوها و اطلاعات مفیدی را کشف کرده و درک عمیق‌تری از داده‌ها و مسائل مورد بررسی در پروژه خود پیدا کنند. این فرآیند به آن‌ها کمک می‌کند تا تصمیم‌گیری‌های بهتری بر اساس داده‌های موجود انجام دهند و نتایج موثرتری را به‌دست آورند.            </font>
#         <hr/>
#         <hr/>
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# کتابخانه‌هایی که در مرحله قبل نصب کردید را داخل نوت‌بوک import کنید و برای هر کدام یک نام مخفف مانند sns, plt, np, pd و... در نظر بگیرید.    </font>
# </div>

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import gdown
import random
from IPython.display import display


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# دیتاست موجود در پروژه که یک فایل csv است را به صورت یک دیتافریم در متغیری به نام df بخوانید.
#     </font>
# </div>

# In[3]:


#file_id = '1XBATJZqbKur4iAHieIITiZph8RZD8Dag'
#url = f'https://drive.google.com/uc?id={file_id}'
#output = 'data.csv'  
#gdown.download(url, output, quiet=False)
#df = pd.read_csv("https://github.com/MoeeinAali/FOP2023-Python-Project-SUT/blob/main/housePrice.csv")
#df = pd.read_csv("https://raw.githubusercontent.com/MoeeinAali/FOP2023-Python-Project-SUT/main/housePrice.csv")
df = pd.read_csv('housePrice.csv')
df.head(10)


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ابعاد (تعداد سطرها و تعداد ستون‌ها) دیتافریم را به صورت یک tuple نمایش دهید.
#     </font>
# </div>

# In[4]:


dimensions = df.shape
dimensions


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         دیتافریم را چاپ کنید.
#     </font>
# </div>

# In[5]:


df
#چون که در ژوپیتر چاپ می کند از پرینت استفاده نشده است


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ده سطر اول دیتافریم را چاپ کنید.
#     </font>
# </div>

# In[6]:


df.head(n=10)


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# ده سطر آخر دیتافریم را چاپ کنید.
#     </font>
# </div>

# In[7]:


df.tail(10)


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ده سطر از دیتافریم را به صورت تصادفی (Random) انتخاب کرده و آن‌ها را در قالب یک دیتافریم با نام sample_df ذخیره کرده و آن را خروجی دهید.
#     </font>
# </div>

# In[8]:


sample_df = pd.DataFrame()
for i in range(10):
    random_number = random.randint(0, dimensions[0])
    #sample_df= sample_df.append(row_to_add, ignore_index=True)
    row_to_add=df.iloc[random_number]
    sample_df = pd.concat([sample_df, pd.DataFrame([row_to_add])], ignore_index=True)
sample_df   


# In[9]:


df.sample(10)#راه سریع تر و بهتر


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# با یک دستور، اطلاعاتی کلی همانند نام ستون‌ها، تعداد indexها، تعداد سلول‌های non-null و... راجع به دیتافریم را بدست اورید.    </font>
# </div>

# In[10]:


df.info()


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         با یک دستور، اطلاعاتی کلی همانند مقدار ماکزیمم، مینیمم، میانگین، چارک‌ها و... راجع به ستون‌های دیتافریم بدست آورید.
#     </font>
# </div>

# In[11]:


df.describe(include='all').T
#اینکلود برای شامل شدن همه ونه فقط عددی ها است وترانهاده برای شکل بهتر است


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         تعداد سلول‌های خالی در هر ستون از دیتافریم را خروجی دهید.
#     </font>
# </div>

# In[12]:


df.isna().sum()
#تعداد ستون های خالی هر ستون می دهد 
#df.isna().sum().sum()تعداد کل خالی ها در مجموع می دهد


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# آن سلول‌هایی که خالی هستند را از دیتافریم حذف کنید و دیتافریم جدید را جایگزین قبلی کنید.    </font>
# </div>

# In[13]:


df = df.dropna()#خالی ها را حذف می کند
df


# In[14]:


df.isnull().sum()#تعداد خالی در هر ستون می دهد که نشان می دهد همه صفر شده است


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         با یک دستور، جنس متغیر ذخیره‌شده در هر ستون از دیتافریم را نشان دهید.
#     </font>
# </div>

# In[15]:


df.dtypes


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# جنس مقادیر ستون‌های  Area و Price  و Price(USD) را از رشته به مقدار عددی تغییر دهید و دیتافریم جدید را جایگزین قبلی کنید.    </font>
# </div>

# In[ ]:





# In[16]:


#df['Area'] = df['Area'].astype(float)
#df['Price'] = df['Price'].astype(float)
#df['Price(USD)'] = df['Price(USD)'].astype(float)
df['Area']=df['Area'].astype('string')
df['Area']=df['Area'].apply(lambda x: x.replace(',', '')).astype('float')
#df['Price']=df['Price'].astype('float')
#df['Price(USD)']=df['Price(USD)'].astype('float')
#df[['Area', 'Price','Price(USD)']] = df[['Area', 'Price','Price(USD)']].apply(pd.to_numeric)
#df['Area'].replace(',','')
#df['Area'].astype('float')
#df['Area'] = df['Area'].str.replace(',', '')
#df['Area']=df['Area'].astype('float')
df


# In[17]:


df.info()


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ستون‌هایی که جنس متغیر آن‌ها از نوع Boolean است را به مقادیر عددی تغییر دهید و دیتافریم جدید را جایگزین قبلی کنید. (به ازای True مقدار 1 و به ازای False مقدار 0 جایگزین شود.)
#     </font>
# </div>

# In[18]:


df['Parking']=df['Parking'].astype('int')
df['Warehouse']=df['Warehouse'].astype('int')
df['Elevator']=df['Elevator'].astype('int')
df


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         دیتافریم جدیدی تشکیل دهید به طوری که نام ستون‌های دیتافریم اصلی در ابتدای سطرها قرار گیرد و اطلاعاتی همانند min , max , mean و... که در قسمت‌های قبلی بدست آوردیم را به عنوان ستون‌های دیتافریم جدید قرار دهید. این دیتافریم جدید را در متغیری با نام df_T ذخیره کنید و چاپ کنید.
#     </font>
# </div>

# In[19]:


#df_T=pd.DataFrame()
df_T=df.describe().transpose()
df_T


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نام ستون‌های دیتافریم را در یک لیست با نام column_names ذخیره کنید و سپس لیست را چاپ کنید.
#     </font>
# </div>

# In[20]:


list_column_names = df.columns.tolist()#می شود با پرانتز لیست هم لیست کردlist(df.columns)
list_column_names


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         یک دیکشنری از نام ستون‌ها تشکیل داده و نام هر ستون را به عنوان key و نام هر ستون به صورت Pascal case را به عنوان value آن در نظر بگیرید.(این 
#         دیکشنری در مراحل بعدی مورد استفاده قرار می‌گیرد.)
#         <br>
#         </font>
#         <font face="IranSansX" size=2>
#         <a href="https://stackoverflow.com/questions/17326185/what-are-the-different-kinds-of-cases">می‌توانید از این لینک برای آشنایی با Case Styleها استفاده کنید.</a>
#     </font>
# </div>

# In[21]:


#list_row_names=list(df_T.index)
dict_df=dict()
for item in list_column_names:
    if item=='Warehouse':
        dict_df[item]='WareHouse'
    else:    
        dict_df[item]=item.capitalize()

pascal_column_names = list(dict_df.values())
dict_df
#از انجایی که نام بیشتر ستون ها یک کلمه است و اولش بزرگ  است در حالت اولیه هم پاسکال کیس هست 


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نام ستون‌هایی که طول آن‌ها از 8 کارکتر کمتر است را خروجی دهید.
#     </font>
# </div>

# In[22]:


list_name_with_less8=list()
for item in list_column_names:
    if len(item)<8:
        print(item)
        list_name_with_less8.append(item)
        
        


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# نام تمامی ستون‌ها را به صورت یک رشته‌ که نام هر ستون با کارکتر '-' از دیگری جدا شده، خروجی دهید.    </font>
# </div>

# In[23]:


str_culumn_names='_'.join(list_column_names)
str_culumn_names


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# با استفاده از دیکشنری ایجاد شده در مراحل قبل، نام ستون‌های دیتافریم را به صورت Pascal case تغییر دهید و در df ذخیره کنید.
#     </font>
# </div>

# In[24]:


df.rename(columns=dict_df, inplace=True)#همه نام ستون ها را خودش عوض می کند
df


# In[25]:


for item in list_column_names:
    df.rename(columns={ item : dict_df[item]}, inplace=True)
#print(df)


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ستون‌های مربوط به قیمت را حذف کرده و دیتافریم حاصل را در متغیری به نام df_without_price ذخیره کنید.
#     </font>
# </div>

# In[26]:


df_without_price = df.drop(['Price', 'Price(usd)'], axis=1)#این دو سطر حذف می کند
df_without_price


# In[27]:


df_without_price=pd.DataFrame()
for i in range(6):
    df_without_price[dict_df[list_column_names[i]]]=df[dict_df[list_column_names[i]]]
#df.drop(['Price', 'Price(usd)'], axis=1) با این روش هم می توان حذف کرد و در جدیده کپی یا دیپ کپی کرد
#s.copy() or s.copy(deep=False)


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         دیتافریم df_without_price را چاپ کنید.
#     </font>
# </div>

# In[28]:


df_without_price


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ستون‌های Area و Room و Price را در قالب یک دیتافریم جدید خروجی دهید.
#     </font>
# </div>

# In[29]:


df.columns#نام دقیقق ستون ها را در میاریم


# In[30]:


new_df = df[['Area', 'Room', 'Price']]#همه را یکجا در جدید بدهمیم
new_df


# In[31]:


df_pra=pd.DataFrame()#یک جدید تعرف کرده و دونه دونه اضافه کنیم
df_pra['Price']=df['Price']
df_pra['Room']=df['Room']
df_pra['Area']=df['Area']
#print(df_pra)


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# سطرهایی از دیتافریم df که index زوج دارند را در قالب یک دیتافریم خروجی دهید.
#     </font>
# </div>

# In[32]:


df.loc[df.index%2==0]#سطر های زوج را می دهد


# In[33]:


df_zoj=pd.DataFrame()
df_new_column_names=list(df.columns)
for i in range(len(df)):
    if i%2==0:
        dict_help=dict()
        for j in range(len(df_new_column_names)):
            dict_help[df_new_column_names[j]]=[df.iloc[i,j]]
        df_zoj=pd.concat([df_zoj,pd.DataFrame(dict_help)],ignore_index=True)
print(df_zoj)
#در اینجا دیتا فریم جدید به صورت دستی می سازیم


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         تعداد مقادیر متمایز موجود در هر ستون را در قالب یک دیکشنری با نام دلخواه ذخیره کنید و خروجی دهید.(در دیکشنری key برابر است با نام ستون و value تعداد مقادیر متمایز موجود در آن است.)
#     </font>
# </div>

# In[34]:


unique_values = dict(df.nunique())#مقادیر متمایز مشخص می کند
unique_values


# In[ ]:





# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         تمامی مقادیر متمایز موجود در ستون Address را در قالب یک لیست خروجی دهید.
#     </font>
# </div>

# In[35]:


df['Address'].unique().tolist()#مقادیر متفاوت ستون پیدا ولیست می کند


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# یک دیکشنری با نام دلخواه ایجاد کنید که key آن برابر با نام ستون‌های دیتافریم و value آن برابر است با لیستی از مقدار متمایز موجود در آن ستون از دیتافریم.در آخر دیکشنری را چاپ کنید.
#     </font>
# </div>

# In[36]:


data = dict()
for col in df.columns:
    data[col] = df[col].unique().tolist()
data
#نام ستون ها را میگیرد متفاوت هر ستون لیست می کند و در دیکشنری قرار می دهد


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         تعداد دفعات تکرار هر مقدار متمایز در ستون Address را مشخص کنید و نتایج را در یک دیکشنری ذخیره کرده و خروجی دهید.(در دیکشنری key برابر با نام مقادیر متمایز ستون Address و value برابر با تعداد دفعات تکرار آن است.)
#     </font>
# </div>

# In[37]:


dict(df['Address'].value_counts())#هر دفعه تکرار می شمرد


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ماکزیمم، مینیمم و طول بازه‌ی تغییرات مقادیر ستون‌هایی که متغیر آن‌ها عددی است را چاپ کنید.
#     </font>
# </div>

# In[38]:


df_describe = df.select_dtypes(include=np.number).describe().T[['max', 'min']]
df_describe['range'] = df_describe['max'] - df_describe['min']
df_describe
#ستون ماکس ومین میگیرد و رنج با اختلاف حساب می کنیم


# In[39]:


maximums = df.select_dtypes(include=np.number).max()
minimums = df.select_dtypes(include=np.number).min()
range_ = maximums - minimums
df_describe = pd.DataFrame({'maximum': maximums, 'minimums': minimums, 'range': range_})
df_describe


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         سطرهایی که مقدار Area آن‌ها از چارک اول مقادیر ستون Area کمتر است را در یک دیتافریم جدید با نام دلخواه ذخیره کرده و خروجی دهید.
#     </font>
# </div>

# In[40]:


df_area_q1 = df[df['Area']<df['Area'].quantile(0.25)]
df_area_q1
#اونایی که شرط برقارا میریزد


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         همانند قسمت قبل، آن سطرهایی که Area آن‌ها از چارک اول کمتر است را شناسایی کرده و فقط مقادیر ستون‌های Area، Room و Price خروجی دهید.
#     </font>
# </div>

# In[41]:


df[df['Area']<df['Area'].quantile(0.25)][['Price', 'Area', 'Room']]


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         دیتافریم اولیه را برحسب ستون قیمت sort کنید و آن را در متغیری به نام df_sorted_by_price ذخیره کنید و در آخر خروجی دهید.
#     </font>
# </div>

# In[42]:


df_sorted_by_price = df.sort_values(['Price'], ascending=False)
df_sorted_by_price
#به صورت کاهشی سورت کرده که می توان عوض کرد


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# دیتافریم df_sorted_by_price را به صورت معکوس خروجی دهید.(از آخر به اول)    </font>
# </div>

# In[43]:


df_sorted_by_price.loc[::-1]
#بر عکس می کند البته با سورت افزایشی هم می شد


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         سطرهایی که مقدار ستون Elevator برای آن‌ها True است را برحسب قیمت sort کنید و خروجی دهید.
#     </font>
# </div>

# In[44]:


df[df['Elevator']==1].sort_values(['Price'], ascending=False)


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         دیتافریم را برحسب Address گروه‌بندی کنید، سپس جمع Area خانه‌های هر گروه را محاسبه و خروجی دهید.
#     </font>
# </div>

# In[45]:


df[['Address', 'Area']].groupby('Address').sum()


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         دیتافریم را برحسب Address گروه‌بندی کنید، سپس میانگین Area خانه‌های هر گروه را با استفاده از Aggregate کردن گروه‌ها با تابع mean بیابید، سپس مقادیر بدست آمده را در یک دیتافریم جدید ذخیره کرده و خروجی دهید.
#     </font>
# </div>

# In[46]:


Groupby_Address_mean = df[['Address', 'Area']].groupby('Address').mean()
Groupby_Address_mean
#گروه بندی بر اساس ادرس ومیانگین گرفتن


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         یک crosstab برحسب Room و Parking رسم کنید.
#     </font>
# </div>

# In[47]:


pd.crosstab(df['Room'], df['Parking'])


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# یک crosstab برحسب Room و Warehouse رسم کنید.    </font>
# </div>

# In[48]:


pd.crosstab(df['Room'], df['WareHouse'])


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         یک crosstab برحسب Room و Elevator رسم کنید.
#     </font>
# </div>

# In[49]:


pd.crosstab(df['Room'], df['Elevator'])


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نشان دهید خانه‌هایی که 0 اتاق، 1 اتاق،....، 5اتاق دارند، به طور میانگین چه قیمتی دارند.
#     </font>
# </div>

# In[50]:


df[['Room', 'Price', 'Price(usd)']].groupby('Room').mean()


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# دیتافریم را برحسب Room و Parking گروه‌بندی کرده و میانگین قیمت هرکدام را حساب کنید.(ترجیحاً با استفاده از Aggregate کردن این کار را انجام دهید.)
#     </font>
# </div>

# In[51]:


df[['Room', 'Price', 'Price(usd)', 'Parking']].groupby(['Room', 'Parking']).agg('mean')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# یک ستون جدید به نام Score به دیتافریم اصلی اضافه کنید، به طوری که مقدار آن برای هرسطر برابر است با جمع مقادیر ستون‌های Parking و Warehouse و Elevator (البته با فرض این که مقادیر ستون‌ها را در مراحل قبل از True/False به 0و1 تغییر داده‌اید.)
#     </font>
# </div>

# In[52]:


df.loc[:,'Score'] = df[['Elevator', 'WareHouse', 'Parking']].sum(axis=1)
df


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         محاسبه کنید که چند درصد خانه‌هایی که مساحت کمتر از 100مترمربع دارند، دارای پارکینگ هستند؟
#     </font>
# </div>

# In[53]:


df[df['Area'] < 100]['Parking'].mean() * 100


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         محاسبه کنید که چند درصد از خانه‌های این دیتافریم حداقل یکی از سه ویژگی پارکینگ، انباری یا آسانسور را دارند؟
#     </font>
# </div>

# In[54]:


(1 - (df[(df['Parking']==0) & (df['WareHouse']==0) & (df['Elevator']==0)].shape[0] / df.shape[0])) * 100


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# خانه‌هایی از دیتافریم که تعداد اتاق‌های آن‌ها از 2 بیشتر است و حداقل یکی از سه ویژگی پارکینگ، انباری یا آسانسور را دارند، در قالب یک دیتافریم خروجی بدهید.    </font>
# </div>

# In[55]:


df[~((df['Parking']==0) & (df['WareHouse']==0) & (df['Elevator']==0)) & (df['Room']>2)]
#معکوس هیچ کدام نداشتن و بزرگتر از دو بودن


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         خانه‌هایی که حداقل 2 و حداکثر 4 اتاق دارند و دارای پارکینگ هستند را در قالب یک دیتافریم خروجی دهید.
#     </font>
# </div>

# In[56]:


df[(2<=df['Room']) & (df['Room']<=4) & (df['Parking']==1)]


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# یک ستون به دیتافریم اضافه کنید و در آن حاصل تقسیم Price بر Area را ذخیره کنید، سپس دیتافریم را برحسب این ستون sort کنید. حال بررسی کنید که 50 خانه‌ی اول این دیتافریم sort شده مربوط به کدام Addressهای متمایز هستند. این Addressها را در قالب یک لیست خروجی دهید.
#     </font>
# </div>

# In[57]:


df['Price_per_Area'] = df['Price'] / df['Area']
df


# In[58]:


df.sort_values('Price_per_Area', ascending=False).iloc[:50, :]['Address'].value_counts()


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         <b>
#         <font color=#006bcf size=5>فاز دوم پروژه: </font>
#         <font color=#006bcf size=5>
# Data Visualization
#             </font>
#          </b>
#         <br><br>
#          <font face="IranSansX" size=3>
#         بخش تصویرسازی داده‌ها در این پروژه، به دانشجوان فرصت می‌دهد تا با استفاده از ابزارها و تکنیک‌های مختلف، داده‌های خود را به شکل‌های بصری جذاب و قابل فهم ترسیم کنند. این بخش از پروژه امکان می‌دهد تا دانشجوان با استفاده از نمودارها، نقشه‌ها، چارت‌ها و دیگر روش‌های تصویری، اطلاعات و الگوهای مهم موجود در داده‌های خود را به روشی کارآمد و شفاف برای مخاطبان مختلف به نمایش بگذارند. این فرایند نه‌تنها به دانشجوان کمک می‌کند تا داده‌های خود را بهبود دهند و بازنمایی مناسبی از آن‌ها ارائه دهند، بلکه به آن‌ها این امکان را می‌دهد تا ارتباطات قوی‌تری بین داده‌ها را ایجاد کرده و الگوها یا تفاوت‌های مهم را به دیگران به شیوه‌ای واضح و قابل فهم نشان دهند. استفاده از تصاویر و گرافیک‌های مختلف به دانشجوان کمک می‌کند تا ارتباطات خود را بهبود بخشند و به دیگران کمک کنند تا داده‌ها را با یک دید بصری جذاب و موثرتر درک کنند.
#         </font>
#         <hr/>
#         <hr/>
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         <b><font color=#cf0000 size=4>نکات مهم فاز دوم</font></b>
#         <hr/>
#         <ul>
#             <li>در این فاز اجباری است که تمامی نمودارهایی که رسم می‌کنید دارای title و label و ... باشد.(جدای از این که داخل متن سوال اشاره شده یا خیر.)</li>
#             <li>همچنین لازم است که scale تمامی نمودارها را با استفاده از دستوراتی همانند xlim و ylim طوری تنظیم کنید که نمودار شکل و شمایل خوبی داشته باشد.</li>
#         </ul>
#         <img src="https://github.com/MoeeinAali/FOP2023-Python-Project-SUT/blob/main/public/pic1.jpg?raw=true" style="width:75%;">
#                 <hr>
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار پراکندگی Price برحسب Area را رسم کنید.(نام هر محور را با label مشخص کنید.)
#     </font>
# </div>

# In[59]:


plt.scatter(df['Area'], df['Price'])
plt.xlabel('Area')
plt.ylabel('Price')
plt.yscale('log')
plt.xscale('log')
plt.title('Price vs Area');
#بدون لگاریتم هم می شد ولی لگاریتم برای نمای بهتر است


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# نمودار قبلی را با رنگی غیر از رنگ default رسم کنید.    </font>
# </div>

# In[60]:


plt.scatter(df['Area'], df['Price'], c='r')
plt.xlabel('Area')
plt.ylabel('Price')
plt.yscale('log')
plt.xscale('log')
plt.title('Price vs Area');


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار قبلی را طوری رسم کنید که نقاط با کارکتر ستاره (*) نشان داده شوند.
#     </font>
# </div>

# In[61]:


plt.scatter(df['Area'], df['Price'], c='r', marker='*')
plt.xlabel('Area')
plt.ylabel('Price')
plt.yscale('log')
plt.xscale('log')
plt.title('Price vs Area');


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# نمودار پراکندگی Price برحسب Room را همانند نمودار قبلی با ویژگی‌های فوق به صورت یکجا رسم کنید.    </font>
# </div>

# In[62]:


plt.scatter(df['Room'], df['Price'], c='r', marker='*')
plt.xlabel('Room')
plt.ylabel('Price')
#plt.yscale('log')
plt.title('Price vs Room');


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار پراکندگی Price را برحسب ستون Score که خودمان در قسمت‌های قبل ایجاد کردیم رسم کنید.
#     </font>
# </div>

# In[63]:


plt.scatter(df['Score'], df['Price'], c='r', marker='*')
plt.xlabel('Score')
plt.ylabel('Price')
plt.xticks(range(4))
plt.title('Price vs Score');
#اسکور فقط مقدار صحیح بین 0و3 دارد


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار توزیع فراوانی را برای ستون Price رسم کنید. بازه‌ی تغییرات قیمت را به 30 قسمت تقسیم کرده و در نمودار نشان دهید.
#     </font>
# </div>

# In[128]:


plt.hist(df['Price'], bins=30);
plt.xlabel('price')
plt.ylabel('frequently')
plt.title('frequently distribution of prices')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# برای نمودار قسمت قبل، نمودار تخمین چگالی توزیع هم‌زمان (KDE) را رسم کنید.(این نمودار یک تخمین صاف و پیوسته از توزیع احتمال داده‌ها را نشان می‌دهد.)    </font>
# </div>

# In[129]:


sns.histplot(df[['Price']][df['Price']<df['Price'].quantile(0.7)], kde=True, bins=30)
plt.xlabel('price')
plt.ylabel('frequently')
plt.title('frequently distribution of prices')
# این برای ان است که بخواهیم در قسمت قبلی تیکه که بیشتر داده ها قرار دارد در نظر بگیریم و تیکه خیلی کم شده کنار بگذاریم


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         توضیح دهید که کاربرد نمودار توزیع فراوانی چیست؟
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;font-size:small;">
# 	<font face="IranSansX" size=2 color=#006bcf>
# 
#         نمایی کلی از همه مقادیر متمایز وتعداد تکرار ان ها می دهد و باعث می شود با یک نگاه کلی فهمید مقداری درچ
#         ه جاهایی به فراوانی و در چه جاهایی به ندرت وجود دارد
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# با استفاده از نمودار Pairplot برای هر دو جفت ستون موجود در دیتافریم یک نمودار پراکندگی به همراه KDE رسم کنید.
#     </font>
# </div>

# In[132]:


sns.pairplot(df, diag_kind='kde');
plt.suptitle('Pairplot with KDE')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# ابتدا ماتریس همبستگی (Correlation Matrix) دیتافریم را با استفاده از توابع آماده بسازید و ذخیره کنید، سپس نمودار Heatmap را بر اساس این ماتریس رسم کنید.
#     </font>
# </div>

# In[126]:


sns.heatmap(df.select_dtypes(include=np.number).corr())
plt.title('Correlation Matrix')
#قسمت وسط برای این است که فقط ستون های عددی جدا شوند    
#corr ماتریس می سازد


# In[125]:


corr_matrix=df.select_dtypes(include='number').corr()
plt.figure(figsize=(8, 6))
heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار Heatmap را به گونه‌ای رسم کنید که مقدار ماتریس همبستگی در هر خانه از نمودار نشان داده شود و از پالت رنگی RdYlGn برای رسم نمودار استفاده شود.
#     </font>
# </div>

# In[131]:


sns.heatmap(df.select_dtypes(include=np.number).corr(), vmin=-1, vmax=1, cmap='RdYlGn', annot=True, fmt='.2f')
plt.title('Correlation Matrix')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# توضیح دهید که کاربرد Heatmap چیست؟
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;font-size:small;">
# 	<font face="IranSansX" size=2 color=#006bcf>
# با توجه به ان در نگاه کلی و به سرعت می توان نسبت به شرایط کلی اگاهی پیدا کردو می توان فهمید در کجا بیشینه کمینه یا معمولی است که با این می توان کمبود ها را پیدا کرد و فهمید که به کدام بخش ها باید توجه بیشتری شود(که یک استفاده اصلی ان در انالیز وب سایت ها است)
#         
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         برای ستون Parking نمودار Pie Chart را به گونه‌ای رسم کنید که هر بخش نمودار یک رنگ دلخواه از طیف سبز داشته باشد و بخشی که فراوانی کمتری دارد از نمودار explode شود و هر بخش نمودار یک label داشته باشد.
#     </font>
# </div>

# In[69]:


df['Parking'].value_counts()


# In[122]:


plt.pie(df['Parking'].value_counts(), labels=['With Parking', 'Without Parking'], autopct='%1.1f%%', explode=(0, 0.1), colors=['green', 'red']);
plt.title('parking vs without parking')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# توضیح دهید که کاربرد Piechart چیست؟
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;font-size:small;">
# 	<font face="IranSansX" size=2 color=#006bcf>
# یکی از پر کاربرد ترین ها درهوش تجاری است و باعث می شود در نگاه کلی و به سرعت فهمید که بخش هدف از چه بخش هایی تشکیل شده و هر کدام چه مقدار سهم دارند که هر کدام بزرگتر باشد باشد سهم بیشتری دارد و موثر تر است و برای رتبه بندی و درصد فراوانی موثر است()برا مقایسه برند ها و سهم فروش و سود نیز موثر است
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         یک نمودار سه قسمتی از نوع Pie Chart رسم کنید. هربخش از این نمودار نشان دهنده توزیع یکی از سه متغیر Warehouse , Parking , Elevator است. نمودار را به گونه‌ای رسم کنید که طیف رنگی هر متغیر با دیگری فرق کند و هر بخش نمودار دارای label مناسب باشد و بخشی که فراوانی کمتری دارد از نمودار explode شود.
#     </font>
# </div>

# In[112]:


#برای سه نمودار در یکی
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#خط زیر برای اطمینان اومده است
plt.figure(figsize=(5, 15))
for col, ax, colors in zip(['WareHouse', 'Parking', 'Elevator'], axes, [('green', 'red'), ('r', 'c'), ('#2ca02c', '#d62728')]):
   ax.pie(df[col].value_counts(), labels=df[col].value_counts().index, autopct='%1.1f%%', explode=(0, 0.1), colors=colors);
#یک به معنی داشتن و صفر به معنی نداشتن است


# In[115]:


fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for col, ax, colors in zip(['WareHouse', 'Parking', 'Elevator'], axes, [('green', 'red'), ('r', 'c'), ('#2ca02c', '#d62728')]):
    ax.pie(df[col].value_counts(), labels=df[col].value_counts().index, autopct='%1.1f%%', explode=(0, 0.1), colors=colors)
    ax.set_title(f'{col} Distribution')
plt.show()


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# نمودار جعبه‌ای را برای ستون Price به گونه‌ای رسم کنید که رنگ آن قرمز باشد و نمودار دارای title و xlabel باشد. 
#     </font>
# </div>

# In[72]:


c = 'red'
plt.boxplot(df['Price'], boxprops=dict(color=c),
            capprops=dict(color=c),
            whiskerprops=dict(color=c),
            flierprops=dict(color=c, markeredgecolor=c),
            medianprops=dict(color=c))
plt.title('Price column Box plot')
plt.xlabel('Price')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
# نمودار قبلی را به گونه‌ای رسم کنید که قطر خطوط و اندازه فونت نوشته‌های نمودار را به میزان دلخواه زیاد کنید.    </font>
# </div>

# In[73]:


c = 'red'
plt.boxplot(df['Price'], 
            capprops=dict(color=c),
            whiskerprops=dict(color=c),
            boxprops = dict(color=c, linestyle='--', linewidth=1.5),
            flierprops=dict(color=c, markeredgecolor=c),
            meanline = dict(linestyle='--', linewidth=5.5, color='purple'),
            medianprops=dict(color=c))
plt.title('Price column Box plot')
plt.xlabel('Price')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار histogram را برای ستون Room رسم کنید و برای آن label و title و رنگ مناسب مشخص کنید.
#     </font>
# </div>

# In[74]:


sns.histplot(df['Room'])
plt.title('Room Histogram')
plt.xlabel('Room')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         یک نمودار سه قسمتی از نوع histogram رسم کنید. هر بخش از این نمودار نشان دهنده‌ی توزیع یکی از سه متغیر Elevator , Parking , Warehouse است.  نمودار را به گونه‌ای رسم کنید که طیف رنگی هر متغیر با دیگری فرق کند و هر بخش نمودار دارای label مناسب باشد.
#     </font>
# </div>

# In[117]:


fig, axes = plt.subplots(1, 3, figsize=(15, 5))
plt.figure(figsize=(5, 15))
for col, ax, colors in zip(['WareHouse', 'Parking', 'Elevator'], axes, ['green', 'red', 'blue']):
        ax.hist(df[col], color=colors)
        #ax.set_label(col)
        ax.set_title(col)
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ابتدا دامنه تغییرات ستون Price را محاسبه کنید و آن را به 4 بازه مساوی با نام‌های cheap , AveUnderMean , AveUpperMean , Expensive تقسیم کنید. به هر بازه تعداد خانه‌هایی که قیمتشان در این بازه قرار دارد را نسبت دهید و در آخر نمودار countplot را برای این بازه‌ها رسم کنید.
#     </font>
# </div>

# In[118]:


sub_df = pd.DataFrame(pd.qcut(df['Price'], 4, labels=['cheap' , 'AveUnderMean' , 'AveUpperMean' , 'Expensive']), columns=['Price'])
sns.countplot(sub_df, x='Price')
plt.title('Distribution of Price Categories')


# In[119]:


sub_df = pd.DataFrame(pd.cut(df['Price'], bins=4, labels=['Low', 'Medium', 'High', 'Very High']), columns=['Price'])
sns.countplot(sub_df, x='Price')
plt.title('Distribution of Price Categories')
#اگر بر حسب رنج مساوی تقسیم کنیم بالایی برحسب تعداد مساوی است


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         ابتدا 2 درصد از داده‌های ستون Price را به صورت تصادفی انتخاب کنید و سپس نمودار خط‌ شکسته را برای این داده‌ها رسم کنید.(محورها دارای label باشند و رنگ نمودار قرمز باشد.)
#     </font>
# </div>

# In[78]:


sub_df = df[['Price']].sample(frac=0.02)
plt.ylabel('Price')
plt.xlabel('Index')
plt.title(' Price vs index')
plt.plot(sub_df, 'r');


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         همانطور که میبینید نمودار قبلی ظاهر خوبی ندارد و شرط تابع بودن را نقض کرده است، داده‌های تصادفی مرحله قبل را به گونه‌ای sort کنید نمودار ما تبدیل به یک تابعی شود که اکیدا یکنوا نیست و نوسان دارد.
#     </font>
# </div>

# In[79]:


sub_df = df[['Price']].sample(frac=0.02).sort_values('Price').reset_index(drop=True)
plt.ylabel('Price')
plt.xlabel('Index')
plt.title(' Price vs index')
plt.plot(sub_df, 'r');


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار قسمت قبل را به گونه‌ای رسم کنید که نقاط شکستگی نمودار با یک دایره با رنگ آبی نشان داده شوند.
#     </font>
# </div>

# In[80]:


sub_df = df[['Price']].sample(frac=0.02).sort_values('Price').reset_index(drop=True)
plt.ylabel('Price')
plt.xlabel('Index')
plt.title(' Price vs index')
plt.plot(sub_df, 'r')
plt.scatter(sub_df.index, sub_df)
#برای نقاط شکستگی یک نمودار روی نمودار شکسته می کشیم


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار خط شکسته‌ی Price(USD) برحسب Area را رسم کنید.
#     </font>
# </div>

# In[85]:


sub_df = df[['Price(usd)', 'Area']].sort_values('Area')
sub_df
plt.plot(sub_df['Area'], sub_df['Price(usd)']);
plt.xlabel('Area')
plt.ylabel('Price(USD)');
plt.title(' Price(USD) vs Area')


# In[100]:


sub_df = df[['Price(usd)', 'Area']].sort_values('Area')
sub_df
plt.plot(sub_df['Area'], sub_df['Price(usd)']);
plt.xlabel('Area')
plt.ylabel('Price(USD)');
plt.xscale('log')
plt.title(' Price(USD) vs Area')
#برای نمای بهتر


# In[101]:


sub_df = df[df['Area'] < 1000][['Price(usd)', 'Area']].sort_values('Area')
sub_df
plt.plot(sub_df['Area'], sub_df['Price(usd)']);
plt.xlabel('Area')
plt.ylabel('Price(USD)');
#plt.xscale('log')
plt.title(' Price(USD) vs Area')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         به نمودار رسم شده در قسمت قبل، نمودار روند تغییرات مرتبه اول(خطی) را اضافه کنید.(برای پیدا کردن ضرایب رگرسیون می‌توانید از تابع polyfit در کتابخانه numpy استفاده کنید.)
#     </font>
# </div>

# In[107]:


#np.polyfit رگراسیون مرتبه اول می سازد
#np.poly1d یک تابع چند جمله ای از ضرایب رگراسیون می سازد
sub_df = df[df['Area'] < 1000][['Price(usd)', 'Area']].sort_values('Area')
plt.plot(sub_df['Area'], sub_df['Price(usd)'])
plt.plot(sub_df['Area'], np.poly1d(np.polyfit(sub_df['Area'], sub_df['Price(usd)'], 1))(sub_df['Area']))
plt.title(' Price(USD) vs Area')
plt.xlabel('Area')
plt.ylabel('Price(USD)');
plt.scatter(sub_df['Area'], sub_df['Price(usd)'],color='red')


# In[108]:


sub_df = df[['Price(usd)', 'Area']].sort_values('Area')
plt.plot(sub_df['Area'], sub_df['Price(usd)'])
plt.plot(sub_df['Area'], np.poly1d(np.polyfit(sub_df['Area'], sub_df['Price(usd)'], 1))(sub_df['Area']))
plt.title(' Price(USD) vs Area')
plt.xlabel('Area')
plt.ylabel('Price(USD)');


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار روند تغییرات خطی که در قسمت قبل رسم کردیم را به صورت خط‌چین با رنگ قرمز رسم کنید.
#     </font>
# </div>

# In[83]:


sub_df = df[['Price(usd)', 'Area']].sort_values('Area')

plt.plot(sub_df['Area'], sub_df['Price(usd)'])
plt.plot(sub_df['Area'], np.poly1d(np.polyfit(sub_df['Area'], sub_df['Price(usd)'], 1))(sub_df['Area']), '--r')
plt.title(' Price(USD) vs Area')
plt.xlabel('Area')
plt.ylabel('Price(USD)');


# In[110]:


sub_df = df[df['Area'] < 1000][['Price(usd)', 'Area']].sort_values('Area')
plt.plot(sub_df['Area'], sub_df['Price(usd)'])
plt.plot(sub_df['Area'], np.poly1d(np.polyfit(sub_df['Area'], sub_df['Price(usd)'], 1))(sub_df['Area']), '--r')
plt.title(' Price(USD) vs Area')
plt.xlabel('Area')
plt.ylabel('Price(USD)');
plt.scatter(sub_df['Area'], sub_df['Price(usd)'],color='green')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         نمودار Barplot را برای ستون Price برحسب ستون Room رسم کنید.(نمودار باید دارای title و label مناسب باشد.)
#     </font>
# </div>

# In[84]:


sns.barplot(df, y='Price', x='Room');
plt.title('Room vs Prices')


# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;line-height:250%;font-size:small;">
# 	<font face="IranSansX" size=3>
#         توضیح دهید که کاربرد Barplot چیست؟
#     </font>
# </div>

# <div dir = "rtl" style="font-face:IranSansX;direction:rtl;font-size:small;">
# 	<font face="IranSansX" size=2 color=#006bcf>
# برای مقایسه هایی را بین دسته های مجزا نشان می دهد یک محور مولفه هایی که مقایسه می شوند و محور دیگر مقدار اندازهگیری را نشان می دهد و باری نمایش اندازه های نسبی و مقایسه ای بسیار خوب است وبا نگاهی کوتاه می توان فهمید به نسبت کدام تیکه ها بیشتر وکدام تیکه ها نسبی کمتر هستند و برای حالات دسته بندی شده و غیر پیوسته مناسب هستند وبرای نشان دادن روند بازار نیز مناسب است    </font>
# </div>
