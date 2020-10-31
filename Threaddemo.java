class Newthread implements Runnable
{
 Thread t;
 Newthread()
 {
  t=new Thread(this,"Demothread");
  System.out.println("Childthread",+t);
 }
public void run()
{
 try
 {
  for(i=5;i>0;i--)
  {
   System.out.println("Child thread",+t);
   Thread.sleep(500);
  }
  catch(InterruptedException e)
  {
   System.out.println("Child interrupted",+e);
  }
  System.out.println("Exiting child thread");
 }
}
class Threaddemo
{
public static void main(String args[])
{
NewThread nt=new NewThread();
nt.t.start();
try
{
for(int i=5;i>0;i--)
{
System.out.println("main thread"+i);
Thread.sleep(1000);
}
}
