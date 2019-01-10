import os

p = os.path.join("Users", "a.popov", "my.txt")
p = str(p)

st = open("/Users/a.popov/my.txt", "r")
print(st.read())
st.close()


#