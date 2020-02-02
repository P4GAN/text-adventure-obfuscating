r=0
f="forward"
b="backward"
c="actions available: "
d="You are in the depths of the tunnel."
p=print
a=1
l="You are standing at the entrance to a long tunnel."
while a!=f:
  if r<1:
    a=input(c+f+", look\n> ")
    if a=="look":p(l)
    elif a==f:p(d);r=1
  if r==1:
    a=input(c+f+", {b}, look\n> ")
    if a==b:p(l);r=0
    elif a=="look":p(d)
p("You have escaped the tunnel. You win!")
