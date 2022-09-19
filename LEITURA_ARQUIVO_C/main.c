#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>


#define TAM_BUFFER 100
// #define DEBUG

struct dados{
	char *date;
	char *time;
	int heart;
};

int main(){

	char buffer[TAM_BUFFER];
	char date[TAM_BUFFER];
	char time[TAM_BUFFER];
	int heart;
	int i = 0;
	int ret, dados = 0;
    int somatorio_heart = 0;
	float quantidade = 0.00;
    float desvio_padrao = 0.00;
	float media;

	FILE *fp;
	struct dados *lista;
	puts("------------------------");

	// Escolha do arquivo short ou long
	fp = fopen("heart_rate_short.csv", "r");
	// fp = fopen("heart_rate_long.csv", "r");


	if (fp == NULL){
		perror("main");
		exit(EXIT_FAILURE);
	}

	// conta o numero de aquisicoes
	while (fgets(buffer,TAM_BUFFER,fp) != NULL) dados++;

	// ignora linha do cabeçalho
	dados--;


	//aloca memoria
	lista = malloc(dados*sizeof(struct dados));

#ifdef DEBUG
	printf("H'a %d dados neste arquivo!\n", dados);
#endif

	// reinicia arquivo e ignora linha do cabeçalho
	rewind(fp);
	fgets(buffer,TAM_BUFFER,fp);

	//inicio do processamento
	while(fgets(buffer,TAM_BUFFER,fp) != 0)
	{

		/* sscanf é semelhando ao fscanf
		 * porém cada linha é lida previamente
		 * pelo fgets 		 */
		ret = sscanf(buffer, "%100[^,],%100[^,],%d\n", date,
				time, &heart);
        

		/* Se o arquivo estiver invalido */
		if (ret != 3) {
			fprintf(stderr, "Arquivo de entrada invalido\n");
			exit(EXIT_FAILURE);
		}

#ifdef DEBUG
		printf("Lido: %d\n", ret);
        printf("date: %s\n", date);
        printf("time: %s\n", time);
        printf("heary: %d\n", heart);
		puts("------------------------");

		printf("%d\n", strlen(nome) + 1);
#endif

		/* Aloca memória para o date e time mais \0 */
		lista[i].date = malloc(strlen(date) + 1);
        lista[i].time = malloc(strlen(time) + 1);

		/* Copia os dados para a lista alocada */
		strncpy(lista[i].date, date, strlen(date) + 1);
        strncpy(lista[i].time, time, strlen(time) + 1);
		
        lista[i].heart = heart;
	
		/* iterador da lista */
		i++;
	}

// 	/* Fecha arquivo */
	fclose(fp);

	/* Mostra os dados lidos */
	for (i=0; i < dados; i++){
        somatorio_heart += lista[i].heart;
	}
    quantidade = dados;
    media = somatorio_heart/quantidade;
    printf("media: %f\n", media);
    for (i=0; i < dados; i++){
        // diferenca = pow((lista[i].heart - media),2);
        desvio_padrao+= (lista[i].heart - media)*(lista[i].heart - media);
	}
	printf("desvio padrao: %f\n", desvio_padrao);
    desvio_padrao = desvio_padrao/quantidade;
	// Nao consegui incluir a bibliteca math, para executar pow e sqrt
    // desvio_padrao = sqrt(desvio_padrao);
	printf("quantidade de dados: %f\n", quantidade);
    printf("desvio padrao: %f\n", desvio_padrao);
    
    // ajustar as funcoes de calculo.

	/* Desaloca memória */
	for (i=0; i < dados; i++){
		free(lista[i].date);
        free(lista[i].time);
	}
	free(lista);


	return 0;
}