r=0
f="forward"
b="backward"
c="actions available: "
t=” tunnel.”
d="You are in the depths of the"+t
p=print
a=1
l="You are standing at the entrance to a long"+t
while a!=f:
  if r<1:
    a=input(c+f+", look\n> ")
    if a=="look":p(l)
    elif a==f:p(d);r=1
  if r>0:
    a=input(c+f+", {b}, look\n> ")
    if a==b:p(l);r=0
    elif a=="look":p(d)
p("You have escaped the”+t,”You win!")
