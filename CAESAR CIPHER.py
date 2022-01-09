alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ciphalphabet=[]
direction=input("Type encode to encrypt and decode to decrypt:\n").lower()
tex1=input("Enter the text:\n").lower()
shif1=int(input("Enter the shift number:\n"))
def caesar(text,shift):
    tex=[]
    for i in text:
        tex+=i
    enc=[]
    for i in tex:
        if i not in alphabet:
            enc.append(i)
            continue    
        curlet=alphabet.index(i)
        if direction=="encode":
            new_pos=(curlet + shift)%26
        elif direction=="decode":
             new_pos=(curlet - shift)%26
        newlet=alphabet[new_pos]
        enc.append(newlet)
    encstr=""
    for i in enc:
         encstr+=i
    print(encstr)
caesar(tex1,shif1)


    
