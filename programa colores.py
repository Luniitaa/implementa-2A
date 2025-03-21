from turtle import *
color('gold','purple')
begin_fill()
while True:
	forward(500)
	left(470)
	if abs(pos()) < 1:
		break
end_fill()
color('gold','pink')
begin_fill()
while True:
	back(250)
	righ(245)
	if abs(pos()) < 1:
		break
done()
