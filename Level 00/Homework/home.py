from turtle import *
width (5)
#home body
color ("blue")
begin_fill ()
forward (200)
left (90)
forward (200)  
left (90)
forward (200)
left (90)
forward (200)
end_fill ()

left (90)
forward (75)
#door
color ("brown")
begin_fill ()
left (90)
forward (75)
right (90) 
forward (50)
right (90)
forward (75)  
end_fill ()


penup ()
goto (200,200) 
pendown ()

#roof
color ("black")
begin_fill ()
right (135)
forward (141)
left (90) 
forward (141)
end_fill()


penup ()
goto (20,180) 
pendown ()

left (45)

#window 1
color ("cyan")
begin_fill ()
forward (40)
left (90)
forward (40)
left (90)
forward (40)
left (90)
forward (40)
end_fill ()




penup ()
goto (180,180) 
pendown ()

#window 2
color ("cyan")
begin_fill ()
forward (40)
left (90)
forward (40)
left (90)
forward (40)
left (90)
forward (40)
end_fill()
exitonclick ()