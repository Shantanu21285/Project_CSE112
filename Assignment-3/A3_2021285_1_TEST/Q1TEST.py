import FUNCTIONS

# READING MATRIX MULTIPLICATION I/P AND O/P AND VERIFYING

for k in range(1,3):
    with open(f'A3_2021285_1_TEST/input{k}','r') as f:
        input=[i.strip() for i in f]
        r1=int(input[0])
        c1=int(input[1])
        A=[]
        for i in range(2,2+r1):
            row_s=input[i]
            row_l=row_s.split()
            row=[]
            for j in row_l:
                row.append(int(j))
            A.append(row)    
        B=[]
        r2=int(input[2+r1])
        c2=int(input[3+r1])
        for i in range(4+r1,4+r1+r2):
            row_s=input[i]
            row_l=row_s.split()
            row=[]
            for j in row_l:
                row.append(int(j))
            B.append(row)

    true_c=[]
    with open(f'A3_2021285_1_TEST/output{k}','r') as f:
        output=[i.strip() for i in f]
        for i in range(r1):
            row_s=output[i]
            row_l=row_s.split()
            row=[]
            for j in row_l:
                row.append(int(j))
            true_c.append(row)

    def test_matMul(A,B,true_c):
        C=FUNCTIONS.matMul(A,B)
        try:
            assert C==true_c
            return True
        except:
            return False

    print(test_matMul(A,B,true_c))

# SCALING TESTING

for k in range(3,5):
    with open(f'A3_2021285_1_TEST/input{k}','r') as f:
        input=[i.strip() for i in f]

        n=int(input[0])

        s_x=input[1]
        l_x=s_x.split()
        x=[]
        for i in l_x:
            x.append(int(i))

        s_y=input[2]
        l_y=s_y.split()
        y=[]
        for i in l_y:
            y.append(int(i))

        s_z=input[3]
        l_z=s_z.split()
        z=[]
        for i in l_z:
            z.append(int(i))

        q=input[4]
        q_l=q.split()
        q=[]
        for i in q_l:
            q.append(int(i))
        sx,sy,sz=q

    with open(f'A3_2021285_1_TEST/output{k}','r') as f:
        output=[i.strip() for i in f]

        true_x=output[0]
        l_x=true_x.split()
        true_x=[]
        for i in l_x:
            true_x.append(int(i))

        true_y=output[1]
        l_y=true_y.split()
        true_y=[]
        for i in l_y:
            true_y.append(int(i))

        true_z=output[2]
        l_z=true_z.split()
        true_z=[]
        for i in l_z:
            true_z.append(int(i))

        def test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z):
            ans_x,ans_y,ans_z=FUNCTIONS.scale(x,y,z,sx,sy,sz,n)
            try:
                assert true_x==ans_x
                assert true_y==ans_y
                assert true_z==ans_z
                return True
            except:
                return False
        print(test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z))

# TRANSLATE TESTING

for k in range(5,7):
    with open(f'A3_2021285_1_TEST/input{k}','r') as f:
        input=[i.strip() for i in f]

        n=int(input[0])

        s_x=input[1]
        l_x=s_x.split()
        x=[]
        for i in l_x:
            x.append(int(i))

        s_y=input[2]
        l_y=s_y.split()
        y=[]
        for i in l_y:
            y.append(int(i))

        s_z=input[3]
        l_z=s_z.split()
        z=[]
        for i in l_z:
            z.append(int(i))

        q=input[4]
        q_l=q.split()
        q=[]
        for i in q_l:
            q.append(int(i))
        tx,ty,tz=q

    with open(f'A3_2021285_1_TEST/output{k}','r') as f:
        output=[i.strip() for i in f]

        true_x=output[0]
        l_x=true_x.split()
        true_x=[]
        for i in l_x:
            true_x.append(int(i))

        true_y=output[1]
        l_y=true_y.split()
        true_y=[]
        for i in l_y:
            true_y.append(int(i))

        true_z=output[2]
        l_z=true_z.split()
        true_z=[]
        for i in l_z:
            true_z.append(int(i))

        def test_scale(x,y,z,tx,ty,tz,true_x,true_y,true_z):
            ans_x,ans_y,ans_z=FUNCTIONS.translate(x,y,z,sx,sy,sz,n)
            #print(ans_x,ans_y,ans_z)
            try:
                assert true_x==ans_x
                assert true_y==ans_y
                assert true_z==ans_z
                return True
            except:
                return False

        #print(true_x,true_y,true_z)
        print(test_scale(x,y,z,tx,ty,tz,true_x,true_y,true_z))

# ROTATE TESTING:
for k in range(7,9):
    with open(f'A3_2021285_1_TEST/input{k}','r') as f:
        input=[i.strip() for i in f]

        n=int(input[0])

        s_x=input[1]
        l_x=s_x.split()
        x=[]
        for i in l_x:
            x.append(int(i))

        s_y=input[2]
        l_y=s_y.split()
        y=[]
        for i in l_y:
            y.append(int(i))

        s_z=input[3]
        l_z=s_z.split()
        z=[]
        for i in l_z:
            z.append(int(i))

        q=input[4]
        q_l=q.split()
        axis=q_l[0]
        angle=float(q_l[1])

    with open(f'A3_2021285_1_TEST/output{k}','r') as f:
        output=[i.strip() for i in f]

        true_x=output[0]
        l_x=true_x.split()
        true_x=[]
        for i in l_x:
            true_x.append(float(i))

        true_y=output[1]
        l_y=true_y.split()
        true_y=[]
        for i in l_y:
            true_y.append(float(i))

        true_z=output[2]
        l_z=true_z.split()
        true_z=[]
        for i in l_z:
            true_z.append(float(i))

    def test_rotate(x,y,z,axis,phi,true_x,true_y,true_z):
        ans_x,ans_y,ans_z=FUNCTIONS.rotate(x,y,z,axis,phi,n)
        try:
            assert ans_x==true_x
            assert ans_y==true_y
            assert ans_z==true_z
            return True
        except:
            return False

    print(test_rotate(x,y,z,axis,angle,true_x,true_y,true_z))









        


    
    