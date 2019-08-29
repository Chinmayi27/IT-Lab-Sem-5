%{ 
	#include<string.h>
	char filename[50];
	char find_word[50];
	char replace_word[50];
	FILE *fp, *fp2;
  
%} 
  
%%
[a-zA-z0-9]+ {
	if(strcmp(yytext, find_word)==0)
	fprintf(fp2, replace_word);

	else{
		fprintf(fp2, yytext);
	}
	printf("1");
} 
. {
	fprintf(fp2, yytext);
} 
\n {
	printf("2");
	fprintf(fp2, "\n");;
} 
%% 

int yywrap(){} ;
  
#include<string.h>
main() { 
	printf("Enter the filename: \n"); 
	scanf("%s",filename); 
	fp = fopen(filename,"r");
	yyin = fp;
	
	fp2 = fopen("op.txt", "w+"); 


	printf("Enter word to find: \n"); 
	scanf("%s",find_word);
	printf("Enter word to replace: \n"); 
	scanf("%s",replace_word);

	yylex(); 
 	printf("File successfully altered\n"); 
} 
