%{ 
    /* Definition section */
    #include <stdio.h> 
    #include <stdlib.h> 
    #include "y.tab.h" 
%} 
  
/* %option noyywrap */
  
/* Rule Section */
%% 
  
[a-zA-Z0-9]+   {yylval.f = yytext; return STR;} 
[-+()*/]    {return yytext[0];} 
[ \t\n]      {;} 
  
%% 
  
int yywrap() 
{  
  return -1;  
}   





