
# 探索美国单车共享数据  
  
  

## 项目背景
  
在过去十年内，自行车共享系统的数量不断增多，并且在全球多个城市内越来越受欢迎。自行车共享系统使用户能够按照一定的金额在短时间内租赁自行车。用户可以在 A 处借自行车，并在 B 处还车，每辆自行车每天可以供多位用户使用。由于信息技术的迅猛发展，共享系统的用户可以轻松地访问系统中的基座并解锁或还回自行车。这些技术还提供了大量数据，使我们能够探索这些自行车共享系统的使用情况。  


## 数据集分析

本数据来源于2017 年上半年三大美国城市的自行车共享系统相关的数据：芝加哥、纽约和华盛顿特区。
  
数据集都包括以下六个核心数据：
  
起始时间 Start Time  
结束时间 End Time  
骑行时长 Trip Duration  
起始车站 Start Station  
结束车站 End Station  
用户类型 User Type  
  
芝加哥和纽约市文件还包含以下两个数据：
  
性别 Gender  
出生年份 Birth Year  

  
如图所示：  
  
![image.png](attachment:image.png)

## 问题解决

我将编写代码并回答以下关于自行车共享数据的问题：
  
起始时间（Start Time 列）中哪个月份最常见？    
起始时间中，一周的哪一天（比如 Monday, Tuesday）最常见？     
起始时间中，一天当中哪个小时最常见？    
总骑行时长（Trip Duration）是多久，平均骑行时长是多久？    
哪个起始车站（Start Station）最热门，哪个结束车站（End Station）最热门？    
哪一趟行程最热门？      
每种用户类型有多少人？    
每种性别有多少人？    
出生年份最早的是哪一年、最晚的是哪一年，最常见的是哪一年？    

## 工具
  
本项目以Python语言为技术基础，通过编写代码导入数据，并计算描述性统计数据回答以上问题。还将写一个脚本，该脚本会接受原始输入并在终端中创建交互式体验，以展现这些统计信息。在这过程中，使用了Pandas,Numpy,Time 库包。
