import math

# FUNCTIONS :

def matMul(A,B):
    r2,c2=len(B),len(B[0])
    mul=[]
    B_t=[]

    # TRANSPOSE MATRIX
    for i in range(c2):
        row=[]
        for j in range(r2):
            row.append(B[j][i])
        B_t.append(row)

    # MULTIPLICATION USING TRANSPOSING
    for i in A:
        row=[]
        for j in B_t:
            el=0
            for k in range(len(i)):
                el+=i[k]*j[k]
            row.append(el)
        mul.append(row)
    return mul

def scale(x,y,z,sx,sy,sz,n):
    S=[[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
    l=[]
    for i in range(n):
        l.append(1)
    C=[x,y,z,l]
    ans=matMul(S,C)
    ans_x,ans_y,ans_z,l=ans
    return ans_x,ans_y,ans_z

def translate(x,y,z,tx,ty,tz,n):
    T=[[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
    l=[]
    for i in range(n):
        l.append(1)
    C=[x,y,z,l]
    ans=matMul(T,C)
    ans_x,ans_y,ans_z,l=ans
    return ans_x,ans_y,ans_z

def rotate(x,y,z,axis,phi,n):
    if axis=='Z':
        R=[[math.cos(phi),-math.sin(phi),0,0],[math.sin(phi),math.cos(phi),0,0],[0,0,1,0],[0,0,0,1]]
        l=[]
        for i in range(n):
            l.append(1)
        C=[x,y,z,l]
        ans=matMul(R,C)
        ans_x,ans_y,ans_z,l=ans
        return ans_x,ans_y,ans_z

    if axis=='X':
        R=[[1,0,0,0],[0,math.cos(phi),-math.sin(phi),0],[0,math.sin(phi),math.cos(phi),0],[0,0,0,1]]
        l=[]
        for i in range(n):
            l.append(1)
        C=[x,y,z,l]
        ans=matMul(R,C)
        ans_x,ans_y,ans_z,l=ans
        return ans_x,ans_y,ans_z

    if axis=='Y':
        R=[[math.cos(phi),0,math.sin(phi),0],[0,1,0,0],[-math.sin(phi),0,math.cos(phi),0],[0,0,0,1]]
        l=[]
        for i in range(n):
            l.append(1)
        C=[x,y,z,l]
        ans=matMul(R,C)
        ans_x,ans_y,ans_z,l=ans
        return ans_x,ans_y,ans_z
    
