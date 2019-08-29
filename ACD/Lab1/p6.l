%{ 
  int counter = 0;
  char sentence[200]; 
%} 
  
%% 
([a-zA-Z]+[' ']+)*(and|or)[' ']+([a-zA-Z]+[' ']+)*[a-zA-Z]+[.] {
	printf("Compound Sentence");
	return;
}
([a-zA-Z]+[' ']+)*[a-zA-Z]+[.] { 
  printf("Simple Sentence");
  return;
}
%% 

int yywrap(){
	return 1;
} ;

  
main() { 
	
	printf("Enter a sentence: \n");  
	yylex(); 
 	printf("\n"); 
} 
