import re

line="fsjknfdjknbfkdl;sfl"
line2 = "Cats are smarter than dogs"
# reg_str='^f.*l$'
reg_str=r'(.*) are (.*?) .*'
# result=re.match(reg_str,line2).group(0,1,2)
# result=re.match(reg_str,line2).groups()
result=re.finditer(reg_str,line2) #匹配所有的并作为迭代器返回
# result=re.match(reg_str,line).group()
for item in result:
    print('item:', item.group())

# if re.match(reg_str,line):
#     print('result:', 'yes')
# else:
#     print('result:', 'not match')

