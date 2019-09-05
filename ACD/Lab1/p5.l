%{ 
	#include<string.h>
  
%} 
  
%%
[0-9][ ]*([+\-*/\%]+[ ]*[0-9][ ]*)*[\n] {
	printf("Arithmetic expression\n");
	return;
	
} 
.*[\n] {
	printf("Not an arithmetic expression\n");
	return;
} 
 
%% 

int yywrap(){} ;
  
#include<string.h>
main() { 
	printf("Enter an expression: \n");  
	yylex(); 
 	printf("\n"); 
} 

