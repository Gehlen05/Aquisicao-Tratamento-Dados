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

	FILE *fp;
	struct dados *lista;
	puts("------------------------");

	fp = fopen("heart_rate.csv", "r");


	if (fp == NULL){
		perror("main");
		exit(EXIT_FAILURE);
	}

	// conta o numero de pessoas
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

		/* Aloca memória para o nome mais \0 */
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
    float quantidade = 0.00;
    float desvio_padrao = 0.00;
    quantidade = i;
    float media;
    media = somatorio_heart/quantidade;
    printf("media: %f\n", media);
    for (i=0; i < dados; i++){
        // diferenca = (lista[i].heart - media);
        desvio_padrao+= (lista[i].heart - media)*(lista[i].heart - media);
	}
    desvio_padrao = desvio_padrao/quantidade;
    desvio_padrao = sqrt(desvio_padrao);
    // printf("diferenca: %f\n", diferenca);
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


// int somatorio(int *lista, int dados){
//     int somatorio_heart = 0;
//     for (int i=0; i < dados; i++){
//         somatorio_heart += lista[i].heart;
// 		// printf("date: %s\n", lista[i].date);
// 		// printf("time: %s\n", lista[i].time );
// 		// printf("heart: %d\n", lista[i].heart);
// 		// puts("------------------------");
// 	}
//     printf("%d", somatorio_heart);
// }