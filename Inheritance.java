class Room
{
float length;
float breadth;

Room(int x,int y)
{
length=x;
breadth=y;
}
int area()
{
return(length*breadth);
}
}
class Drawingroom extends Room
{
int height;
Drawingroom(int x, int y, int z)
{
length=x;
breadth=y;
height=z;
}
int volume()
{
return(length*breadth*height);
}
}
class Inheritance
{
public static void main(String args[])
{
Drawingroom obj=new Drawingroom(8,9);

int area= obj.Area();
int volume=new volume();

System.out.println(area);
System.out.println(volume);
}
}