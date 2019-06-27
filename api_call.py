import requests
import json

api_url_base = "https://api.propublica.org/congress/v1/116/both/bills/introduced.json"
headers = {'Content-Type': 'application/json',
        'X-API-Key': 'PVJmuJD58mZ4dSc0Kh9T9fO6MYFfmBLSAsmICAqy'}
raw_data = []

b1_number = ''
b1_title = ''
b1_sponsor_title = ''
b1_sponsor_name = ''
b1_sponsor_party = ''
b1_sponsor_state = ''
b1_summary_short = ''

def get_bill_info():
    r = requests.get(api_url_base, headers=headers)
    
    data = r.json()
    with open('raw/data.json', 'w') as f:
        json.dump(data, f)

def read_bill():
    get_bill_info()
    i = 0

    with open('raw/data.json') as json_file:
        data = json.load(json_file)
        for p in data['results']:
            for q in p['bills']: 
                if i < 20:
                    i = i + 1

                    if i == 1:
                        read_bill.b1_number = q['number']
                        read_bill.b1_title = q['title']
                        read_bill.b1_sponsor_title = q['sponsor_title']
                        read_bill.b1_sponsor_name = q['sponsor_name']
                        read_bill.b1_sponsor_party = q['sponsor_party']
                        read_bill.b1_sponsor_state = q['sponsor_state']
                        read_bill.b1_summary_short = q['summary_short']
                    elif i == 2:
                        read_bill.b2_number = q['number']
                        read_bill.b2_title = q['title']
                        read_bill.b2_sponsor_title = q['sponsor_title']
                        read_bill.b2_sponsor_name = q['sponsor_name']
                        read_bill.b2_sponsor_party = q['sponsor_party']
                        read_bill.b2_sponsor_state = q['sponsor_state']
                        read_bill.b2_summary_short = q['summary_short']
                    elif i == 3:
                        read_bill.b3_number = q['number']
                        read_bill.b3_title = q['title']
                        read_bill.b3_sponsor_title = q['sponsor_title']
                        read_bill.b3_sponsor_name = q['sponsor_name']
                        read_bill.b3_sponsor_party = q['sponsor_party']
                        read_bill.b3_sponsor_state = q['sponsor_state']
                        read_bill.b3_summary_short = q['summary_short']
                    elif i == 4:
                        read_bill.b4_number = q['number']
                        read_bill.b4_title = q['title']
                        read_bill.b4_sponsor_title = q['sponsor_title']
                        read_bill.b4_sponsor_name = q['sponsor_name']
                        read_bill.b4_sponsor_party = q['sponsor_party']
                        read_bill.b4_sponsor_state = q['sponsor_state']
                        read_bill.b4_summary_short = q['summary_short']
                    elif i == 5:
                        read_bill.b5_number = q['number']
                        read_bill.b5_title = q['title']
                        read_bill.b5_sponsor_title = q['sponsor_title']
                        read_bill.b5_sponsor_name = q['sponsor_name']
                        read_bill.b5_sponsor_party = q['sponsor_party']
                        read_bill.b5_sponsor_state = q['sponsor_state']
                        read_bill.b5_summary_short = q['summary_short']
                    elif i == 6:
                        read_bill.b6_number = q['number']
                        read_bill.b6_title = q['title']
                        read_bill.b6_sponsor_title = q['sponsor_title']
                        read_bill.b6_sponsor_name = q['sponsor_name']
                        read_bill.b6_sponsor_party = q['sponsor_party']
                        read_bill.b6_sponsor_state = q['sponsor_state']
                        read_bill.b6_summary_short = q['summary_short']
                    elif i == 7:
                        read_bill.b7_number = q['number']
                        read_bill.b7_title = q['title']
                        read_bill.b7_sponsor_title = q['sponsor_title']
                        read_bill.b7_sponsor_name = q['sponsor_name']
                        read_bill.b7_sponsor_party = q['sponsor_party']
                        read_bill.b7_sponsor_state = q['sponsor_state']
                        read_bill.b7_summary_short = q['summary_short']
                    elif i == 8:
                        read_bill.b8_number = q['number']
                        read_bill.b8_title = q['title']
                        read_bill.b8_sponsor_title = q['sponsor_title']
                        read_bill.b8_sponsor_name = q['sponsor_name']
                        read_bill.b8_sponsor_party = q['sponsor_party']
                        read_bill.b8_sponsor_state = q['sponsor_state']
                        read_bill.b8_summary_short = q['summary_short']
                    elif i == 9:
                        read_bill.b9_number = q['number']
                        read_bill.b9_title = q['title']
                        read_bill.b9_sponsor_title = q['sponsor_title']
                        read_bill.b9_sponsor_name = q['sponsor_name']
                        read_bill.b9_sponsor_party = q['sponsor_party']
                        read_bill.b9_sponsor_state = q['sponsor_state']
                        read_bill.b9_summary_short = q['summary_short']
                    elif i == 10:
                        read_bill.b10_number = q['number']
                        read_bill.b10_title = q['title']
                        read_bill.b10_sponsor_title = q['sponsor_title']
                        read_bill.b10_sponsor_name = q['sponsor_name']
                        read_bill.b10_sponsor_party = q['sponsor_party']
                        read_bill.b10_sponsor_state = q['sponsor_state']
                        read_bill.b10_summary_short = q['summary_short']
                    elif i == 11:
                        read_bill.b11_number = q['number']
                        read_bill.b11_title = q['title']
                        read_bill.b11_sponsor_title = q['sponsor_title']
                        read_bill.b11_sponsor_name = q['sponsor_name']
                        read_bill.b11_sponsor_party = q['sponsor_party']
                        read_bill.b11_sponsor_state = q['sponsor_state']
                        read_bill.b11_summary_short = q['summary_short']
                    elif i == 12:
                        read_bill.b12_number = q['number']
                        read_bill.b12_title = q['title']
                        read_bill.b12_sponsor_title = q['sponsor_title']
                        read_bill.b12_sponsor_name = q['sponsor_name']
                        read_bill.b12_sponsor_party = q['sponsor_party']
                        read_bill.b12_sponsor_state = q['sponsor_state']
                        read_bill.b12_summary_short = q['summary_short']
                    elif i == 13:
                        read_bill.b13_number = q['number']
                        read_bill.b13_title = q['title']
                        read_bill.b13_sponsor_title = q['sponsor_title']
                        read_bill.b13_sponsor_name = q['sponsor_name']
                        read_bill.b13_sponsor_party = q['sponsor_party']
                        read_bill.b13_sponsor_state = q['sponsor_state']
                        read_bill.b13_summary_short = q['summary_short']
                    elif i == 14:
                        read_bill.b14_number = q['number']
                        read_bill.b14_title = q['title']
                        read_bill.b14_sponsor_title = q['sponsor_title']
                        read_bill.b14_sponsor_name = q['sponsor_name']
                        read_bill.b14_sponsor_party = q['sponsor_party']
                        read_bill.b14_sponsor_state = q['sponsor_state']
                        read_bill.b14_summary_short = q['summary_short']
                    elif i == 15:
                        read_bill.b15_number = q['number']
                        read_bill.b15_title = q['title']
                        read_bill.b15_sponsor_title = q['sponsor_title']
                        read_bill.b15_sponsor_name = q['sponsor_name']
                        read_bill.b15_sponsor_party = q['sponsor_party']
                        read_bill.b15_sponsor_state = q['sponsor_state']
                        read_bill.b15_summary_short = q['summary_short']
                    elif i == 16:
                        read_bill.b16_number = q['number']
                        read_bill.b16_title = q['title']
                        read_bill.b16_sponsor_title = q['sponsor_title']
                        read_bill.b16_sponsor_name = q['sponsor_name']
                        read_bill.b16_sponsor_party = q['sponsor_party']
                        read_bill.b16_sponsor_state = q['sponsor_state']
                        read_bill.b16_summary_short = q['summary_short']
                    elif i == 17:
                        read_bill.b17_number = q['number']
                        read_bill.b17_title = q['title']
                        read_bill.b17_sponsor_title = q['sponsor_title']
                        read_bill.b17_sponsor_name = q['sponsor_name']
                        read_bill.b17_sponsor_party = q['sponsor_party']
                        read_bill.b17_sponsor_state = q['sponsor_state']
                        read_bill.b17_summary_short = q['summary_short']
                    elif i == 18:
                        read_bill.b18_number = q['number']
                        read_bill.b18_title = q['title']
                        read_bill.b18_sponsor_title = q['sponsor_title']
                        read_bill.b18_sponsor_name = q['sponsor_name']
                        read_bill.b18_sponsor_party = q['sponsor_party']
                        read_bill.b18_sponsor_state = q['sponsor_state']
                        read_bill.b18_summary_short = q['summary_short']
                    elif i == 19:
                        read_bill.b19_number = q['number']
                        read_bill.b19_title = q['title']
                        read_bill.b19_sponsor_title = q['sponsor_title']
                        read_bill.b19_sponsor_name = q['sponsor_name']
                        read_bill.b19_sponsor_party = q['sponsor_party']
                        read_bill.b19_sponsor_state = q['sponsor_state']
                        read_bill.b19_summary_short = q['summary_short']
                    elif i == 20:
                        read_bill.b20_number = q['number']
                        read_bill.b20_title = q['title']
                        read_bill.b20_sponsor_title = q['sponsor_title']
                        read_bill.b20_sponsor_name = q['sponsor_name']
                        read_bill.b20_sponsor_party = q['sponsor_party']
                        read_bill.b20_sponsor_state = q['sponsor_state']
                        read_bill.b20_summary_short = q['summary_short']
