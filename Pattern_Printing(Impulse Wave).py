#sample input 1
#plots=[10,7,12,2,4,7,2,4,1,2,6,6,3,2,1,4,7,2,7,3,1,3,11,4,2,1,5,2,3,3,3,6,1,3,9,5,2,1,2,11,9,2,3,8,2,5,1,2,7,2,4,11,2,12]



#sampe input 2
#plots=[1,2,3,4,5,6,7,8]

'''
sample output 2
                           /\       
              /\          /  \      
     /\      /  \        /    \     
/\  /  \    /    \      /      \    
  \/    \  /      \    /        \   
         \/        \  /          \  
                    \/            \ 
                                   \
'''


#sample input 3
plots=[1,2,3,4,5,5,4,3,2,1]
'''
sample output 3
              /\              
     /\      /  \      /\     
/\  /  \    /    \    /  \  /\
  \/    \  /      \  /    \/  
         \/        \/         
'''

def find_y_max_min(lis):
	step=0
	max_y=0
	min_y=max(plots)
	check=1
	for i in lis:
		if check%2==1:
			step = step+i
			if max_y<step:
				max_y=step
		if check%2==0:
			step=step-i
			if min_y > step:
				min_y=step
		check+=1
	return max_y,min_y
	
def gen_arr(x,y):
	res=[]
	for i in range(x):
		res.append([])
		for j in range(y):
				res[i].append(0)
	return res

y_max_min=find_y_max_min(plots)
neg_check=1 if y_max_min[1] < 0 else 0

y_max_min=(abs(y_max_min[0]),abs(y_max_min[1]))
x=sum(plots)
y=abs(y_max_min[0]+y_max_min[1])


if neg_check ==0: 
	c_pos=(0,y-1)
else:
	c_pos=(0,y-(1+y_max_min[1]))#(0,y-1)


check=1

a = gen_arr(x,y)#np.zeros((x,y))

def print_up(count,pos):
	x,y=pos
	u_pos=()
	for i in range(count):
		a[x+i][y-i]=1
		u_pos=(x+i,y-i)
	u_pos=(u_pos[0]+1,u_pos[1])
	return u_pos
	

def print_down(count,pos):
	x,y=pos
	u_pos=()
	for i in range(count):
		a[x+i][y+i]=2
		u_pos=(x+i,y+i)
	u_pos=(u_pos[0]+1,u_pos[1])
	return u_pos




for k in plots:
	if check%2==1:
		c_pos=print_up(k,c_pos)
	if check%2==0:
		c_pos=print_down(k,c_pos)
	check+=1




for i in range(y):
	
	for j in range(x):
		if a[j][i]==0:
			print(' ',end='')
		elif a[j][i]==1:
			print('/',end='')
		elif a[j][i]:
			print('\\',end='')
	print()
