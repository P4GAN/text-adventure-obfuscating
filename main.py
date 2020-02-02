r=0
f="forward"
b="backward"
c="actions available: "
t=" tunnel."
d="You are in the depths of the"+t
p=print
a=1
l="You are standing at the entrance to a long"+t
x="look"
n=", ",x,"\n> "
z=input
while a!=f:
  if r<1:
    a=z(c+f+n)
    if a==x:p(l)
    elif a==f:p(d);r=1
  if r>0:
    a=z(c+f+f", {b}"+n)
    if a==b:p(l);r=0
    elif a==x:p(d)
p("You have escaped the"+t,"You win!")
