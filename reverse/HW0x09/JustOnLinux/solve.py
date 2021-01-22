'''
base64 encode with different *table* and padding, [space]
https://richardstartin.github.io/posts/base64-encoding
https://github.com/gehaxelt/Python-MyBase64/blob/master/mybase64.py
'''
import re
def base64Encode(text):
    table = "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~o"
    bit_str=""	
    base64_str=""

    #Loop through all chars concatenate them as binary string
    for char in text:
        bin_char = bin(ord(char)).lstrip("0b")
        bin_char = (8-len(bin_char))*"0" + bin_char
        bit_str += bin_char

    #Add zero till text-length is divideable through 3
    while (((len(text)) % 3) != 0):
        bit_str += "00000000"	
        text += "0"
    
    #Split bit_str into 6bit long brackets
    brackets = re.findall('(\d{6})', bit_str)

    #Encode the brackets
    for bracket in brackets:
        if(bracket=="000000"):
            base64_str+=" "
        else:
            base64_str+=table[int(bracket,2)]
    return base64_str

def base64Decode(chiffre):
    table = "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~o"
    bit_str=""
    text_str=""
    
    #Loop through every char
    for char in chiffre:
        #Ignore characters, which are not in the table. Concatenate the binary representation of table index of char 
        if char in table:
            bin_char = bin(table.index(char)).lstrip("0b")
            bin_char = (6-len(bin_char))*"0" + bin_char
            bit_str += bin_char
    
    #Make 8bit - 2byte brackets
    brackets = re.findall('(\d{8})', bit_str)

    #Decode char binary -> asciii
    for bracket in brackets:
                    text_str+=chr(int(bracket,2))

    return text_str

flag = 'M&=wM].]VyA?GR&[GRA%I]Q#HOA_GRz/T%M?H?T@UR_%HBL?GRA.U?w>HSM*WS@ '
print (base64Decode(flag))