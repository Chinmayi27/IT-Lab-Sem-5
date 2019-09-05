%{
int COMMENT=0;
%}
identifier [a-zA-Z][a-zA-Z0-9]*
%%
#.* {
	printf("\n%s is a preprocessor directive",yytext);
}


int | 
float |
char |
double |
while |
for |
struct |
typedef |
do |
if |
break |
continue |
void |
switch |
return |
else |
goto {
	if(!COMMENT)
	printf("\n%s is a keyword",yytext);
}
"/*" {
	COMMENT=1;
	printf("this is a comment block"); 
}

"*/" { 
	COMMENT=0; 
}
"//".*\n { 
	printf("this is a comment"); 
}
{identifier}\( {
	if(!COMMENT)
	printf("\nfunction %s",yytext);
}
\{  {
	if(!COMMENT)
	printf("\nblock begins");
}
\}  {
	if(!COMMENT)
	printf("\nblock ends ");
}
{identifier}(\[[0-9]*\])? {
	if(!COMMENT) 
	printf("\n %s identifier",yytext);
}
\"(\\.|[^"\\])*\" {
	if(!COMMENT)
	printf("\n%s is a string",yytext);
}
[0-9]+ {if(!COMMENT) printf("\n%s is a number ",yytext);}
[-+*/] { 
	if (!COMMENT)
	printf("Arithmetic operator");
} 
\)(\:)? {
	if(!COMMENT)
	ECHO;
}
\( ECHO;
= {	
	if(!COMMENT)
		printf("\n%s is an assignment",yytext);
}

\<= | 
\>= |
\< |
== |
\> {
	if(!COMMENT) printf("\n%s is a relational operator",yytext);
}
. {

}
\n {

}
%%

int yywrap(){
	return 1;
} ;


int main(int argc, char **argv)
{
	FILE *file;
	file=fopen("sample.c","r");
	if(!file)
	{
		printf("could not open the file");
		exit(0);
	}
	yyin = file;
	yylex();
	printf("\n------\nFile is parsed");

}
