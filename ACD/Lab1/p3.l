%{ 
  int counter = 0; 
%} 
  
%% 
[a-z] {
	char ch = yytext[0];
	ch += 5;
	if (ch> 'z') 
		ch -= ('z'+1- 'a');
	printf ("%c" ,ch );
}
[A-Z] { 
	char ch = yytext[0] ;
	ch += 3;
	if (ch> 'Z') 
		ch -= ('Z'+1- 'A');
	printf("%c",ch);
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
 	printf("\n"); 
} 

