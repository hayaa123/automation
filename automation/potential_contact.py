import re

phone_regex = r'\+[0-9]-[0-9]{2,9}-[0-9]{2,9}-[0-9]{2,9}|[0-9]{2,9}-[0-9]{2,9}-[0-9]{2,9}-[0-9]{2,9}|\([0-9]{1,3}\)[0-9]{2,9}-[0-9]{2,9}|[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,4}|[0-9]{9,10}|[0-9]{3}-[0-9]{4}'
# email_regex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
email_regex = r'[\w-]*@[\w-]*\.[\w-]{1,5}'

phone_formula1 = r'\+[0-9]-[0-9]{2,9}-[0-9]{2,9}'
phone_formula2 = r'[0-9]{2,9}-[0-9]{2,9}-[0-9]{2,9}-[0-9]{2,9}'
phone_formula3 = r'\([0-9]{1,3}\)[0-9]{2,9}-[0-9]{2,9}'
phone_formula4 = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,4}|[0-9]{9,10}'
phone_formula5 = r'[0-9]{3}-[0-9]{4}'
phone_formula6 = r'[0-9]{9,10}'

with open ("automation/assets/potential-contacts.txt") as file:
    content = file.read()
    
    filtered_phones = re.findall(phone_regex,content)
    filtered_email = re.findall(email_regex,content)
    # print(len(filtered_email))

def cleaning_phone_num(phone_array):
    clean_phones = []
    for num in phone_array :

        if re.match(phone_formula6,num):
            num = f'{num[:3]}-{num[3:6]}-{num[6:]}'
            clean_phones.append(num)

        elif re.match(phone_formula4,num):
            num = num.split('.')
            num = f'{num[0]}-{num[1]}-{num[2]}'
            clean_phones.append(num)

        elif re.match(phone_formula3,num):
            num = num.split(")")
            num = f'{num[0][1:]}-{num[1]}'
            clean_phones.append(num)
        
        elif re.match(phone_formula2,num):
            num = num[4:]
            clean_phones.append(num)
        
        elif re.match(phone_formula1,num):
            num=num[3:]
            clean_phones.append(num)
        elif re.match(phone_formula5,num):
            num = "206-" + num
            clean_phones.append(num)

        else:
            clean_phones.append(num)

    return clean_phones

clean_phones = cleaning_phone_num(filtered_phones)
# print(len(filtered_phones))

with open ("automation/assets/phone_numbers.txt", "w") as file :
    file.write(f"phones numbers ({len(clean_phones)}) \n")
    for phone in clean_phones :
        file.write(phone)
        file.write("\n")

with open ("automation/assets/emails.txt", "w") as file :    
    file.write(f"Email adress ({len(filtered_email)}) \n")
    for email in filtered_email :
        file.write(email)
        file.write("\n")
