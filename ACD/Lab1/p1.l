%{ 
  int counter = 0;
  char *longest;
%} 
  
%% 
[a-zA-Z]+ { 
  if(yyleng>counter)
  { 
    counter=yyleng; 
    longest=yytext;
    longest[counter]='\0';
  }
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
	char subbuff[50];
	memcpy(subbuff, &longest[0], counter );
	subbuff[counter]='\0';
	int i=0;
	char temp;
	while(i<counter/2){
		temp = subbuff[i];
		subbuff[i] = subbuff[counter-i-1];
		subbuff[counter-i-1] = temp;
		i =i+1;
	}
	printf("largest string: %s(reversed) of len=%d",subbuff, counter); 
 	printf("\n"); 
} 

