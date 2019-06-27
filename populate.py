from api_call import read_bill
import xml.etree.ElementTree as et

tree = et.parse('raw/gui.ui')
root = tree.getroot()

def b1_pop():
    i = 1

    for widget in root.iter('string'):
        print i

        line_text = widget.text
        
        if i == 2:
            widget.text = read_bill.b1_number
        elif i == 3:
            sponsor = read_bill.b1_sponsor_title + read_bill.b1_sponsor_name + ' ' + read_bill.b1_sponsor_party + '-' + read_bill.b1_sponsor_state
            widget.text = sponsor
        elif i == 4:
            widget.text = read_bill.b1_title

        i += 1

tree.write('raw/gui.ui')

read_bill()
b1_pop()
