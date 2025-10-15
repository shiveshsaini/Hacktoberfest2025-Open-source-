import sys
 
input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
outs = []
for i in range(1, t+1):
    n = int(input_data[i])
    outs.append("Sakurako" if n % 2 == 0 else "Kosuke")
print("\n".join(outs))
