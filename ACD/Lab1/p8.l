%{ 
  int counter = 0;
  char *longest;
%} 
  
%% 
[a-zA-Z]*["ab"][ 	.]+ {
	printf("%s\n", yytext); 
  counter = counter+1;
}
. {
	;
}
\n {
	;
}
%% 

int yywrap(){} ;

  
main() { 
	FILE *fp; 
	char filename[50]; 
	printf("Enter the filename: \n"); 
	scanf("%s",filename); 
	fp = fopen(filename,"r"); 
	yyin = fp; 
	yylex(); 
	printf("Words ending with tab: %d",counter); 
 	printf("\n"); 
} 

