import sys

variables={} # STORES ALL VARIABLES DECLARED
labels={} # STORES ALL THE LABELS USED
registers={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}

# CONTAINS OP CODE OF INSTRUCTIONS ALLOWED TO BE EXECUTED

type_a={'add':'10000','sub':'10001','mul':'10110','xor':'11010','or':'11011','and':'11100','addf':'00000','subf':'00001'}
type_b={'mov':'10010','rs':'11000','ls':'11001','movf':'00010'}
type_c={'mov':'10011','div':'10111','not':'11101','cmp':'11110'}
type_d={'ld':'10100','st':'10101'}
type_e={'jmp':'11111','jlt':'01100','jgt':'01101','je':'01111'}

# CONTAINS ALL THE INSTRUCTIONS
all_instructions=[]
while True:
    all_instructions=type_a.keys() |type_b.keys()|type_c.keys()|type_d.keys()|type_e.keys()
    all_instructions.add('hlt')
    all_instructions.add('var')
    break

count_instruction=0 # AFTER COUNTING ALL THE INSTRUCTIONS, WE ASSIGN MEMORY ADDRESS TO VAR USING THIS

count=0 # TO KEEP TRACK OF WHICH INSTRUCTION IS BEING EXECUTED

var_initial=0 # TO INDICATE MEMORY ADDRESSES TO VARIABLES IN AN ORDER (count+var_initial)

flag_var=1 # TO INDICATE VARIABLES ARE BEING DECLARED, IF 0 THEN RESULTS IN AN ERROR

output_list=[] # TO FIRST TRAVERSE THE WHOLE CODE AND PRINT A MACHINE CODE ONLY IF FULLY CORRECT

hlt = 0 # last command of input is hlt

count_i=0 # TO ASSIGN MEM_ADDR TO LABELS PRESENT IN ASSEMBLY CODE

label_emptyline=0 # TO ASSIGN MEMORY ADDRESS TO INSTRUCTIONS LIKE "Loop: "

#FUNCTIONS

def decimalTobinary(n):
    assert n>=0 and n<=255
    assert isinstance(n,int)
    n_bin=''
    n=int(n)
    while n>0:
        d=n%2
        n=n//2
        n_bin+=str(d)
    n_bin=n_bin[-1::-1]
    zero_left=8-len(n_bin)
    n_bin=('0'*zero_left)+n_bin
    return n_bin

def DecimalTobinary(n1):
    n,num=n1.split(".")
    n_bin=''
    n=int(n)
    while n>0:
        d=n%2
        n=n//2
        n_bin+=str(d)
    n_bin=n_bin[-1::-1]
    num=("0."+num)
    num=float(num)
    x=""
    count=0
    while (num%1!=0 and count<6-len(n_bin)):
        num=num*2
        x=x+str(num)[0]
        num=float("0"+str(num)[1::])
        count=count+1
    lis=[n_bin,x]
    return lis

def FloatToIeee(num):
    assert float(num)<252
    whole,decimal=DecimalTobinary(num)
    exponent=len(whole)-1
    assert int(exponent)<=111
    mantissa=whole[1::]+decimal
    assert int(mantissa)<=11111
    for j in range(5-len(mantissa)):
        mantissa=mantissa+"0"
    exponent=bin(exponent)[2::]
    for j in  range(3-len(exponent)):
        exponent="0"+exponent
    Ieee=exponent+mantissa
    return Ieee

def typeA(instruction):
    s=''
    s+=type_a[instruction[0]]
    s+='00'
    s+=registers[instruction[1]]
    s+=registers[instruction[2]]
    s+=registers[instruction[3]]
    output_list.append(s)

def typeB(instruction):
    s=''
    s+=type_b[instruction[0]]
    s+=registers[instruction[1]]
    imm=instruction[2]
    imm=imm[1:]
    assert imm.isdigit()
    s+=decimalTobinary(int(imm))
    output_list.append(s)

def typeC(instruction):
    s=''
    s+=type_c[instruction[0]]
    s+='00000'
    s+=registers[instruction[1]]
    s+=registers[instruction[2]]
    output_list.append(s)

def typeD(instruction):
    s=''
    s+=type_d[instruction[0]]
    s+=registers[instruction[1]]
    s+=variables[instruction[2]]
    output_list.append(s)
 
def typeE(instruction):
    s=''
    s+=type_e[instruction[0]]
    s+='000'
    s+=labels[instruction[1]]
    output_list.append(s)

def typeF(instruction):
    s=''
    s+=type_b[instruction[0]]
    s+=registers[instruction[1]]
    imm=instruction[2]
    imm=imm[1:]
    ieee=FloatToIeee(imm)
    s+=ieee
    output_list.append(s)

# decimal in movf check
# assert for 252 ya mantissa ya exponent

def errorgen(instruction,line_number):

    # Decimal in movf
    if instruction[0]=='movf':
        val_float=instruction[2][1:]
        if val_float.isdigit():
            print(f"ERROR @LINE{line_number}: INTEGER VALUE DETECTED FOR MOVF INSTRUCTION")
            return 0
        val_float=float(val_float)
        if val_float>252 or val<1:
            print(f"ERROR @LINE{line_number}: IMMEDIATE VALUE ENTERED CANNOT BE GREATER THAN 252 OR LESS THAN 1")
            return 0
        if int(exponent)>111 or int(mantissa)>11111:
            print(f"ERROR @LINE{line_number}: INVALID IMMEDIATE INPUT. IT CANNOT BE REPRESENTED IN 8 BIT FLOATING POINT FORM")

    #handling hlt
    if l[-1][-1]!="hlt":
        print(f"ERROR @LINE{len(l)}: SYNTAX ERROR: hlt instruction must be used at end")
        return 0


    # ILLEGAL/INVALID INSTRUCTION
    if instruction[0] not in all_instructions:
        print(f"ERROR @LINE{line_number}: SYNTAX ERROR:INVALID INSTRUCTION OR INSTRUCTION NOT FOUND")
        return 0

    # USE OF INVALID REGISTERS FOR LEN 3
    if len(instruction)==3:
        for i in range(1,3):
            if (instruction[i])[0] == "R":
                if(instruction[i]) not in registers.keys():
                    print(f"ERROR @LINE{line_number}: INVALID INPUT OF REGISTERS")
                    return 0

    #variable label not declared
    if instruction[0] in type_e.keys():
        if instruction[1] not in labels.keys():
            print(f"ERROR @LINE{line_number}: GENERAL ERROR : label not declared")
            return 0  
    
    # Extra length of type registers in type a
    if instruction[0] in type_a.keys():
        if len(instruction)!=4:
            print(f"ERROR @LINE{line_number}: GENERAL ERROR: invalid inputs for instructions")
            return 0

    # Extra length of type registers in type b
    if instruction[0] in type_b.keys():
        if len(instruction)!=3:
            print(f"ERROR @LINE{line_number}: GENERAL ERROR: invalid inputs for instructions")
            return 0
    
    # Extra length of type registers in type c
    if instruction[0] in type_c.keys():
        if len(instruction)!=3:
            print(f"ERROR @LINE{line_number}: GENERAL ERROR: invalid inputs for instructions")
            return 0
    
    # Extra length of type registers in type d
    if instruction[0] in type_d.keys():
        if len(instruction)!=3:
            print(f"ERROR @LINE{line_number}: GENERAL ERROR: invalid inputs for instructions")
            return 0
    
    # Extra length of type registers in type e
    if instruction[0] in type_e.keys():
        if len(instruction)!=2:
            print(f"ERROR @LINE{line_number}: GENERAL ERROR: invalid inputs for instructions")
            return 0
    
    # USE OF INVALID REGISTERS FOR LEN 4
    if len(instruction)==4:
        for i in range(1,4):
            if (instruction[i])[0] == "R":
                if(instruction[i]) not in registers.keys():
                    print(f"ERROR @LINE{line_number}: INVALID INPUT OF REGISTERS")
                    return 0
    
    #HAMDLING FLAG
    if instruction[0]=="mov":
        if instruction[2]=="FLAGS":
            print(f"ERROR @LINE{line_number}: INVALID USE OF FLAG IN THE COMMAND")
            return 0
                    
    # handling $
    if instruction[0] in type_b.keys():
        if instruction[2][0]!= "$":
            print(f"ERROR @LINE{line_number}: GENERAL ERROR: IMMEDIATE VALUE NOT FOUND")
            return 0

    # USE OF lmm <= 255 and >= 0.
    if len(instruction)==3:
        if (instruction[2])[0]=="$":
            value = instruction[2]
            value=value[1:]
            if float(value)>=256 or float(value)<0:
                print(f"ERROR @LINE{line_number}: ERROR IMMEDIATE VALUE OVERFLOW")
                return 0
    
    #handling immediate value floating number input
    if (instruction[0] in type_b.keys()) and (instruction[2][0]=="$"):
        print(f"ERROR @LINE{line_number}: VALUE ERROR: INPUT NOT A DECIMAL VALUE")
        return 0
    
    # A mem_addr in load and store must be a variable.
    if len(instruction)==3:
        if instruction[2][0] not in variables.keys():
            print(f"ERROR @LINE{line_number}: GENERAL ERROR : MEM ADDER MUST BE A DECLARED VARIABLE")
            return 0

    # Variable declared in middle of program
    if instruction[0]=='var' and flag_var==0:
        print(f"ERROR @LINE{line_number}: VARIABLES TO BE DECLARED AT THE STARTING ONLY")
        return 0     

    # HLT INSTRUCTION DECLARED IN MIDDLE
    if count!=len(l) and instruction[0]=="hlt":
        print(f"ERROR @LINE{line_number}: HLT INSTRUCTION MUST BE DECLARED AT THE END OF THE PROGRAM. ")
        return 0
    elif count==len(l) and len(instruction)==1 and instruction[0]!='hlt':
        print(f"ERROR @LINE{len(l)}: HLT INSTRUCTION NOT FOUND")
        return 0


#INPUT

l=[]
for line in sys.stdin:
    if line == "\n":
        pass
    else:
        x=line.strip().split()
        if len(x)==1 and x[0][-1]==':':
            label_name=x[0]
            label_name=label_name[:-1]
            labels[label_name]=decimalTobinary(count_instruction+label_emptyline)
            label_emptyline+=1
        else:
            l.append(x)
        if line[0:3]!='var':
            count_instruction+=1

#LINE 1: 'hlt'
#LINE 2: label: hlt or type E
#LINE 3: label: type_e or type_b,c,d
#LINE 4: type a or label: type_b,c,d
#LINE 5: label: type_a
#LIST 'l' TRAVERSING USING FOR LOOP ('l' is where our input code stored)


try:
    assert l[-1][-1]=="hlt"
    for line in l:
        if line[0]=='var':
            assert flag_var==1
            variables[line[1]]=decimalTobinary(var_initial+count_instruction)
            var_initial+=1
            count+=1
            continue
        else:
            flag_var=0
            if (len(line)==1):
                assert line[0]=='hlt'
                assert count==len(l)-1
                output_list.append('0101000000000000')

            elif (len(line)==2):
                if line[0][-1]==':':
                    label=line[0]
                    length_label=len(label)
                    label_name=label[0:length_label-1]
                    if label_name not in labels:
                        labels[label_name]=decimalTobinary(count_i+label_emptyline)
                    line=line[1:]

                    if line[0]=='hlt' and count==len(l)-1:
                        output_list.append('0101000000000000')
                    else:
                        assert False
                        
                else:
                    assert line[0] in type_e
                    if line[1] in labels:
                        typeE(line)
                    else:
                        flag_lab=0
                        for line_e in l:
                            if line_e[0][-1]==':':                               
                                label=line_e[0]                               
                                length_label=len(label)
                                label_name=label[0:length_label-1]
                                if label_name==line[1]:
                                    flag_lab=1                        
                                    assert label_name==line[1]                               
                                    index=l.index(line_e)-var_initial+label_emptyline
                                    labels[label_name]=decimalTobinary(index)
                                    break
                                else:
                                    continue
                        if flag_lab==1:
                            typeE(line)
                        else:
                            assert False
            elif len(line)==3:
                if line[0][-1]==':':
                    label=line[0]
                    length_label=len(label)
                    label_name=label[0:length_label-1]
                    if label_name not in labels:
                        labels[label_name]=decimalTobinary(count_i+label_emptyline)
                    line=line[1:]

                    if (len(line)==2):
                        assert line[0] in type_e
                        if line[1] in labels:
                            typeE(line)
                        else:
                            flag_lab=0
                            for line_e in l:
                                if line_e[0][-1]==':':                               
                                    label=line_e[0]                               
                                    length_label=len(label)
                                    label_name=label[0:length_label-1]
                                    if label_name==line[1]:
                                        flag_lab=1                        
                                        assert label_name==line[1]                               
                                        index=l.index(line_e)-var_initial+label_emptyline
                                        labels[label_name]=decimalTobinary(index)
                                        break
                                    else:
                                        continue
                            if flag_lab==1:
                                typeE(line)
                            else:
                                assert False
                else:
                    if line[0]=='mov':
                        if line[2][0]=='$':
                            if line[1]!='FLAGS':
                                typeB(line)
                            else:
                                assert False
                        else:
                            if line[2]!='FLAGS':
                                typeC(line)
                            else:
                                assert False
                    elif line[0]=="movf":
                        if line[1]!='FLAGS':
                            val_float=line[2][1:]
                            if val_float.isdigit():
                                assert False
                            else:
                                typeF(line)
                        else:
                            assert False
                    else:
                        if 'FLAGS' not in line:
                            if line[0] in type_b:
                                if line[2][0]=='$':
                                    typeB(line)
                                else:
                                    assert False
                            elif line[0] in type_c:
                                typeC(line)
                            elif line[0] in type_d:
                                typeD(line)
                            else:
                                assert False
                        else:
                            assert False

            elif len(line)==4:
            
                if line[0][-1]==':':
                    label=line[0]
                    length_label=len(label)
                    label_name=label[0:length_label-1]
                    labels[label_name]=decimalTobinary(count_i+label_emptyline)
                    line=line[1:]

                    if (len(line)==2):
                        assert line[0] in type_e
                        if line[1] in labels:
                            typeE(line)
                        else:
                            flag_lab=0
                            for line_e in l:
                                if line_e[0][-1]==':':                               
                                    label=line_e[0]                               
                                    length_label=len(label)
                                    label_name=label[0:length_label-1]
                                    if label_name==line[1]:
                                        flag_lab=1                        
                                        assert label_name==line[1]                               
                                        index=l.index(line_e)-var_initial+label_emptyline
                                        labels[label_name]=decimalTobinary(index)
                                        break
                                    else:
                                        continue
                            if flag_lab==1:
                                typeE(line)
                            else:
                                assert False
                    elif len(line)==3:
                        if line[0]=='mov':
                            if line[2][0]=='$':
                                if line[1]!='FLAGS':
                                    typeB(line)
                                else:
                                    assert False
                            else:
                                if line[2]!='FLAGS':
                                    typeC(line)
                                else:
                                    assert False
                        elif line[0]=="movf":
                            if line[1]!='FLAGS':
                                typeF(line)
                            else:
                                assert False
                        else:
                            if 'FLAGS' not in line:
                                if line[0] in type_b:
                                    if line[2][0]=='$':
                                        typeB(line)
                                    else:
                                        assert False
                                elif line[0] in type_c:
                                    typeC(line)
                                elif line[0] in type_d:
                                    typeD(line)
                                else:
                                    assert False
                            else:
                                assert False
                else:
                    if 'FLAGS' not in line:
                        assert line[0] in type_a
                        typeA(line)
                    else:
                        assert False
            elif len(line)==5:
                if line[0][-1]==':':
                    label=line[0]
                    length_label=len(label)
                    label_name=label[0:length_label-1]
                    labels[label_name]=decimalTobinary(count_i+label_emptyline)
                    line=line[1:]

                    if 'FLAGS' not in line:
                        assert line[0] in type_a
                        typeA(line)
                    else:
                        assert False
                else:
                    assert False
                

            else:
                assert False    

            count+=1
            count_i+=1

    # GENERATING OUTPUT
    for i in output_list:
        print(i)

except:
    errorgen(line,count+1)
