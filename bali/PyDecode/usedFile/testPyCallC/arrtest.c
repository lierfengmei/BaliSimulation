#include <stdio.h>

void arrtest(char *p[], int c)
{
  int i;
  for(i=0; i<c; i++)
  {
//    printf("%s\n",p[i]);
   // sprintf(p[i],"I love linian and Does he love me?%d",i);
    sprintf(p[i],"Ive me ? %d",i);
  }
  return;
}
