str = "Ali"
print("Before the Reverse String")
s = list(str);
left = 0;
right = len(s) - 1;
while left < right:  
  temp = s[left];
  s[left] = s[right];
  s[right] = temp;
  left += 1;
  right -=1;

print ("After the Reverse String \n", s)
