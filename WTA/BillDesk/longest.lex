%{ 
  int counter = 0; 
%} 


%% 
[a - zA - Z] + { 
  if (yyleng > counter) { 
    counter = yyleng; 
  } 
}
%% 
  
main() { 
	FILE *fp; 
	char filename[50]; 
	printf("Enter the filename: \n"); 
	scanf("%s",filename); 
	fp = fopen(filename,"r"); 
	yyin = fp; 
	yylex(); 
	printf("largest: %d", counter); 
 	printf("\n"); 
} 

