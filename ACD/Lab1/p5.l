%{ 
	#include<string.h>
  
%} 
  
%%
[0-9][ ]*([+\-*/][ ]*[0-9][ ]*)*[\n] {
	printf("\nArithmetic expression %s", yytext);
	break;
	
} 
.[\n] {
	printf("\nNot an arithmetic expression");
} 
 
%% 

int yywrap(){} ;
  
#include<string.h>
main() { 
	printf("Enter a sentence: \n");  
	yylex(); 
 	printf("\n"); 
} 

