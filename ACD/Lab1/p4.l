%{  
%} 
  
%% 
"/*"[^\n]+"*/" {
	fprintf(yyout, "\n");
}

"//"[^\n]+ {
	fprintf(yyout, "\n");
}

(var1|var2) {
	fprintf(yyout, " ");
}
. {
	fprintf(yyout, yytext);
}

\n {
	fprintf(yyout, "\n");
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
	yyout=fopen("output", "w"); 
	yylex(); 
 	printf("File successfully altered\n"); 
} 

