#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
	int i, j, gdzie, ile, em;
	printf("Ho Ho Ho\n");
	char drzewo[20][49], gwiazda[4][49];
	
	//   TAK TO MNIEJ WIECEJ TRZEBA ZROBIC
	
	printf("0123456789012345678901234^0123456789012345678901234\n");
	printf("                         ^                            \n");
	printf("                        / \\                           \n");
	printf("                      <  #  >                         \n");
	printf("                        \\ /                           \n");
	printf("                        / \\                           \n");
	printf("                       /   \\                         \n");
	printf("                      /_   _\\                         \n");
	printf("                       /   \\                         \n");
	printf("                      /     \\                         \n");
	
	gdzie = 1;
	
	for(j = 0; j < 4; j++){
		for(i = 0; i < 49; i++)		
		gwiazda[j][i] = ' ';
	}
	
	gwiazda[0][24] = '^';
	
	gwiazda[1][23] = '/';
	gwiazda[1][25] = '\\';
	
	gwiazda[2][22] = '<';
	gwiazda[2][24] = 'C';
	gwiazda[2][26] = '>';
	
	gwiazda[3][23] = '\\';
	gwiazda[3][25] = '/';
	
	
	for(j = 0; j < 20; j++){
		for (i = 0; i < 49; i++){
			drzewo[j][i] = ' ';
		}
	}
	
	/*
	
	drzewo[0][23] = '/';
	drzewo[0][25] = '\\';
	drzewo[1][22] = '/';
	drzewo[1][26] = '\\';
	drzewo[2][21] = '/';
	drzewo[2][27] = '\\';
	
	drzewo[3][20] = '/';
	drzewo[3][28] = '\\';
	drzewo[3][21] = '_';
	drzewo[3][22] = '_';
	
	drzewo[3][26] = '_';
	drzewo[3][27] = '_';
//--------------------------------------------------//	
	drzewo[4][22] = '/';
	drzewo[4][26] = '\\';
	drzewo[5][21] = '/';
	drzewo[5][27] = '\\';
	drzewo[6][20] = '/';
	drzewo[6][28] = '\\';
	
	drzewo[7][19] = '/';
	drzewo[7][29] = '\\';
	drzewo[7][20] = '_';
	drzewo[7][21] = '_';
	
	drzewo[7][27] = '_';
	drzewo[7][28] = '_';
//--------------------------------------------------//	
	
	*/
	
	ile = 0;
	em = 5;
	gdzie = 24;
	for(j = 0; j < 20; j++){
		ile++;
		gdzie--;
		drzewo[j][gdzie] = '/';
		if(ile%5 == 0){
			for(i = 0; i < 2; i++){
				gdzie++;
				drzewo[j][gdzie] = '_';
			}
			gdzie++;
			em++;
		}
	}
	
	ile = 0;
	em = 5;
	gdzie = 24;
	for(j = 0; j < 20; j++){
		ile++;
		gdzie++;
		drzewo[j][gdzie] = '\\';
		if(ile%5 == 0){
			for(i = 0; i < 2; i++){
				gdzie--;
				drzewo[j][gdzie] = '_';
			}
			gdzie--;
			em++;
		}
	}
	
	
	system("CLS");
	for(j = 0; j < 4; j++){
		for(i = 0; i < 49; i++){
			printf("%c",gwiazda[j][i]);
		}	
		printf("\n");	
	}
	
	for(j = 0; j < 20; j++){
		for(i = 0; i < 49; i++){
			printf("%c",drzewo[j][i]);
		}		
		printf("\n");
	}
	
	
	// super symbol na bombke ¤
	
	return 0;
}
