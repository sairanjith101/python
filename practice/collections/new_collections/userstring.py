from collections import UserString

class mystring(UserString):
    def append(self,s):
        self.data += s

    def remove(self,s):
        self.data = self.data.replace(s,"")

s1 = mystring("Sai")
print(s1.data)
s1.append("i")
print(s1.data)
s1.remove("a")
print(s1.data)