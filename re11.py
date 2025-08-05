import re

def reg_search(text, regex_list):
    #结果
    result = []
    for pattern_dict in regex_list:

        label, regex = list(pattern_dict.items())[0]
        
        match = re.search(regex, text)#表达式匹配
        
        result_value = None 

        if match:
            
            if label == '换股期限':
                groups = match.groups()#一次性全拿
                y1, m1, d1, y2, m2, d2 = groups
                start_date = f"{y1}-{int(m1):02d}-{int(d1):02d}"
                end_date = f"{y2}-{int(m2):02d}-{int(d2):02d}"
                result_value = [start_date, end_date]
            
            else:
                
                if match.groups():
                    result_value = match.group(1)#匹配第一个括号

        result.append({label: result_value})
            
    return [result]

text =""" 标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2 日至 2027 年 6 月 1 日止。"""



regex_list= [
    
    {'标的证券': r'股票代码：(.*?)[，,]'},
    
   
    {'换股期限': r'(\d{4}).*?年.*?(\d{1,2}).*?月.*?(\d{1,2}).*?日至.*?(\d{4}).*?年.*?(\d{1,2}).*?月.*?(\d{1,2}).*?日'}
]

final_result = reg_search(text, regex_list)
print(final_result)
