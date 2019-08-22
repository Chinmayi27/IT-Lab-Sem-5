%{ 
  int counter = 0; 
  char filename[50];
  FILE *fp;
  const char *r= "readf";
  const char *w="writef";
%} 
  
%% 
(printf) { 
  	fprintf(fp, "writef");
  }

(scanf) {
	fprintf(fp, "readf");
}
. {
	fprintf(fp, yytext);
} 
\n {
	fprintf(fp, "\n");;
} 
%% 

int yywrap(){} ;
  
main() { 
	char filename[50]; 
	printf("Enter the filename: \n"); 
	scanf("%s",filename); 
	fp = fopen(filename,"r");
	yyin = fp;

	printf("Enter the new filename: \n"); 
	scanf("%s",filename);
	fp = fopen(filename, "w+"); 
	yylex(); 
 	printf("File successfully altered\n"); 
} 

