from utils import Stack

s = input().split()

st = Stack()

def operate(x1, x2, opr):
    x1 = int(x1)
    x2 = int(x2)
    if opr == '+':
        return x1 + x2
    elif opr == '-':
        return x1 - x2
    elif opr =='x':
        return x1 * x2
    elif opr == '/':
        return x1/x2


for c in s:
    if c == '+' or c == '-' or c == 'x' or c == '/':
        x1 = st.pop()
        x2 = st.pop()
        st.push(operate(x2,x1,c))
    else:
        st.push(c)
    
print(st.peak())