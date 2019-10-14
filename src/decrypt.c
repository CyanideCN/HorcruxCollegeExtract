#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "xxtea.h"

char *KEY = "bogehcollege";
char *SIGN = "palmpi";

int main(int argc, char* argv[]){
	FILE *fin, *fout;
	char *infile, *outfile;
	char *buf;
	char *data;
	unsigned long size;
	int keylen, signlen, retlen;
	if(argc < 3){
		printf("usage: decrypt infile outfile\n");
		return -1;
	}
	else{
		infile = argv[1];
		outfile = argv[2];
		keylen = strlen(KEY);
		signlen = strlen(SIGN);
	}
	fin = fopen(infile,"rb");
	if(fin == NULL){
		perror("can't open the input file");
		return -1;
	}
	fseek(fin, 0L, SEEK_END);
	size = ftell(fin);
	rewind(fin);
	buf = (char*)malloc(size);
	fread(buf, size, 1, fin);
	fclose(fin);
	data = xxtea_decrypt(buf + signlen, size - signlen, KEY, keylen, &retlen);
	if(data == NULL){
		printf("%s decrypt fail\n", infile);
		return -1;
	}
	fout = fopen(outfile, "wb+");
	if(fout == NULL){
		perror("can't open the output file");
		return -1;
	}
	fwrite(data, retlen, 1, fout);
	fclose(fout);
	free(data);
	printf("%s decrypt successful\n", infile);
	return 0;
}

	
