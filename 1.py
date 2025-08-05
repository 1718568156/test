import requests
import csv
import time

url = "https://www.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
headers = {'User-Agent': 'Mozilla/5.0'}
payload = {
    'bondType': '100001',
    'issueYear': '2023',
    'pageNo': 1,
    'pageSize': 15
}
total = 8 #一共就8页
all_records = []
page = 1

while True:
    payload['pageNo'] = page#翻页唯一改变的地方
    print(f"第{page}页")
    
    response = requests.post(url, headers=headers, data=payload)
    #接受数据
    data = response.json()
    #分解数据
    records = data.get('data', {}).get('resultList', [])
    
    all_records.extend(records)
    
    if page >= total:
        print("抓完了")
        break
        
    page += 1
    time.sleep(1)

output_file = 'data.csv' 

csv_headers = [
    'ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'
]

original_keys = [
    'isin', 'bondCode', 'entyFullName', 'bondType', 'issueStartDate', 'debtRtng'
]

with open(output_file, mode='w', encoding='utf-8-sig') as f:#创建文件
    writer = csv.writer(f)
    writer.writerow(csv_headers)
    
    for record in all_records:
        row_data = [record.get(key, '') for key in original_keys]
        writer.writerow(row_data)
