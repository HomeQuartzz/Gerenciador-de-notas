#include <stdio.h>
#include <stdlib.h>

//Abaixo está a função responsável pela leitura dos relatórios.
int leitor_de_relatorio(char*nome_do_relatorio){

    FILE *arquivo; //Ponteiro do arquivo.
    char linha[300]; //Define quanto caracteres podem ser armazenados por linha.

    arquivo = fopen(nome_do_relatorio, "r"); //O relatório é aberto apenas para leitura.

    if (arquivo == NULL){
        printf("Erro! O arquivo não pode ser aberto.\n"); //Se o arquivo for inexistente, esse "if" é responsável por encerrar o programa.
        getchar();
        exit(1);

    }
    printf("---INÍCIO DO RELATORIO---\n");

    while(fgets(linha, 300, arquivo) !=NULL){ //O while é responsável para ler linha por linha, e quando for nulo(sem mais caracteres) finaliza a leitura.
        printf("%s", linha);
    }
    getchar();
    printf("---FIM DO RELATORIO---\n");
    getchar();

    fclose(arquivo); //Fecha o arquivo.

    return 0;


}

int main(){
    int opcao;
    int i = 0;
    printf("---Seja bem vindo(a) ao leitor de relatórios!---\n\n");
    getchar();

    while (i==0){//Responsável pelo loop do menu.
            printf("-------------------------------------\nQual matéria voce deseja visualizar?\n-------------------------------------\n\n");
            printf("---1:Língua Portuguesa---\n---2:Matemática---\n---3:Ciências---\n---4:História---\n---5:Geografia---\n---6:Artes---\n---7:Educação Física---\n---8:Língua Inglesa---\n---9:Todas as matérias---\n---0:Sair---\n");

            if(scanf("%i", &opcao) != 1){//Verifica se o caractere digitado é um número. 
                printf("Digite apenas um número.\n");
                while(getchar() != '\n');//A função getchar é responsável pela limpeza da variável "opcao", removendo o que quer que o usuário tenha digitado.
                opcao = -1;//Obriga o programa ir direto ao defeault.
            }
            switch (opcao){//O menu do programa
                case(0):
                    printf("Saindo...");
                    i++;//Adiciona mais 1 a variável "i" para quebrar o looping
                    break;

                case (1):
                    leitor_de_relatorio("relatorio_Lingua_Portuguesa.txt");
                    break;
                
                case (2):
                    leitor_de_relatorio("relatorio_Matematica.txt");
                    break;
                
                case (3):
                    leitor_de_relatorio("relatorio_Ciencias.txt");
                    break;

                case (4):
                    leitor_de_relatorio("relatorio_Historia.txt");
                    break;
                
                case (5):
                    leitor_de_relatorio("relatorio_Geografia.txt");
                    break;
                
                case (6):
                    leitor_de_relatorio("relatorio_Arte.txt");
                    break;
                
                case (7):
                    leitor_de_relatorio("relatorio_Educacao_Fisica.txt");
                    break;

                case (8):
                    leitor_de_relatorio("relatorio_Lingua_Inglesa.txt");
                    break;
                
                case (9):
                    leitor_de_relatorio("relatorio_geral_todas_as_disciplinas.txt");
                    break;
                
                default:
                    printf("Opção inválida.\n\n");
                    break;

            }
        }    
    return(0);
}