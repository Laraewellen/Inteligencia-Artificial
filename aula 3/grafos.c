#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100
int i=0;
int j=0;
// ========== ESTRUTURAS BÁSICAS ==========

// Estrutura para fila (usada na BFS)
typedef struct {
    int itens[MAX_VERTICES];
    int frente, tras;
} Fila;

// Estrutura do grafo com matriz de adjacência
typedef struct {
    int matriz[MAX_VERTICES][MAX_VERTICES];
    int numVertices;
    int direcionado; // 0 = não direcionado, 1 = direcionado
} GrafoMatriz;

// Estrutura para um nó da lista de adjacência
typedef struct No {
    int vertice;
    int peso;
    struct No* proximo;
} No;

// Estrutura do grafo com lista de adjacência
typedef struct {
    No** listaAdj;
    int numVertices;
    int direcionado;
} GrafoLista;

// ========== FUNÇÕES DA FILA ==========

void inicializarFila(Fila *fila) {
    fila->frente = -1;
    fila->tras = -1;
}

int filaVazia(Fila *fila) {
    return fila->frente == -1;
}

void enfileirar(Fila *fila, int valor) {
    if (fila->tras == MAX_VERTICES - 1) {
        printf("Fila cheia!\n");
    } else {
        if (fila->frente == -1) {
            fila->frente = 0;
        }
        fila->tras++;
        fila->itens[fila->tras] = valor;
    }
}

int desenfileirar(Fila *fila) {
    int item;
    if (filaVazia(fila)) {
        printf("Fila vazia!\n");
        return -1;
    } else {
        item = fila->itens[fila->frente];
        fila->frente++;
        if (fila->frente > fila->tras) {
            fila->frente = fila->tras = -1;
        }
        return item;
    }
}

// ========== FUNÇÕES DO GRAFO COM MATRIZ ==========

// Função para inicializar o grafo
void inicializarGrafoMatriz(GrafoMatriz *grafo, int numVertices, int direcionado) {
    grafo->numVertices = numVertices;
    grafo->direcionado = direcionado;
    
    // Inicializa a matriz com 0 (sem arestas)
    for ( i = 0; i < numVertices; i++) {
        for ( j = 0; j < numVertices; j++) {
            grafo->matriz[i][j] = 0;
        }
    }
}

// Função para adicionar aresta
void adicionarArestaMatriz(GrafoMatriz *grafo, int origem, int destino, int peso) {
    if (origem >= 0 && origem < grafo->numVertices && 
        destino >= 0 && destino < grafo->numVertices) {
        
        grafo->matriz[origem][destino] = peso;
        
        // Se não for direcionado, adiciona na direção oposta também
        if (!grafo->direcionado) {
            grafo->matriz[destino][origem] = peso;
        }
    }
}

// Função para imprimir o grafo
void imprimirGrafoMatriz(GrafoMatriz *grafo) {
    printf("Matriz de Adjacência:\n");
    printf("   ");
    for (i = 0; i < grafo->numVertices; i++) {
        printf("%2d ", i);
    }
    printf("\n");
    
    for ( i = 0; i < grafo->numVertices; i++) {
        printf("%2d ", i);
        for ( j = 0; j < grafo->numVertices; j++) {
            printf("%2d ", grafo->matriz[i][j]);
        }
        printf("\n");
    }
}

// ========== FUNÇÕES DO GRAFO COM LISTA ==========

// Função para criar um novo nó
No* criarNo(int vertice, int peso) {
    No* novoNo = (No*)malloc(sizeof(No));
    novoNo->vertice = vertice;
    novoNo->peso = peso;
    novoNo->proximo = NULL;
    return novoNo;
}

// Função para inicializar o grafo com lista de adjacência
void inicializarGrafoLista(GrafoLista *grafo, int numVertices, int direcionado) {
    grafo->numVertices = numVertices;
    grafo->direcionado = direcionado;
    
    grafo->listaAdj = (No**)malloc(numVertices * sizeof(No*));
    
    for ( i = 0; i < numVertices; i++) {
        grafo->listaAdj[i] = NULL;
    }
}

// Função para adicionar aresta na lista de adjacência
void adicionarArestaLista(GrafoLista *grafo, int origem, int destino, int peso) {
    if (origem >= 0 && origem < grafo->numVertices && 
        destino >= 0 && destino < grafo->numVertices) {
        
        // Adiciona da origem para o destino
        No* novoNo = criarNo(destino, peso);
        novoNo->proximo = grafo->listaAdj[origem];
        grafo->listaAdj[origem] = novoNo;
        
        // Se não for direcionado, adiciona na direção oposta também
        if (!grafo->direcionado) {
            No* novoNoInverso = criarNo(origem, peso);
            novoNoInverso->proximo = grafo->listaAdj[destino];
            grafo->listaAdj[destino] = novoNoInverso;
        }
    }
}

// Função para imprimir o grafo com lista de adjacência
void imprimirGrafoLista(GrafoLista *grafo) {
    printf("Lista de Adjacência:\n");
    for ( i = 0; i < grafo->numVertices; i++) {
        printf("Vértice %d: ", i);
        No* temp = grafo->listaAdj[i];
        while (temp) {
            printf("-> %d(peso:%d) ", temp->vertice, temp->peso);
            temp = temp->proximo;
        }
        printf("\n");
    }
}

// Função para liberar a memória do grafo com lista de adjacência
void liberarGrafoLista(GrafoLista *grafo) {
    for ( i = 0; i < grafo->numVertices; i++) {
        No* atual = grafo->listaAdj[i];
        while (atual) {
            No* temp = atual;
            atual = atual->proximo;
            free(temp);
        }
    }
    free(grafo->listaAdj);
}

// ========== ALGORITMOS DE GRAFOS ==========

// Algoritmo de Busca em Largura (BFS)
void BFS(GrafoMatriz *grafo, int verticeInicial) {
    int visitado[MAX_VERTICES] = {0};
    Fila fila;
    
    inicializarFila(&fila);
    
    // Marca o vértice inicial como visitado e o enfileira
    visitado[verticeInicial] = 1;
    enfileirar(&fila, verticeInicial);
    
    printf("Busca em Largura (BFS) a partir do vértice %d: ", verticeInicial);
    
    while (!filaVazia(&fila)) {
        int verticeAtual = desenfileirar(&fila);
        printf("%d ", verticeAtual);
        
        // Visita todos os vértices adjacentes não visitados
        for ( i = 0; i < grafo->numVertices; i++) {
            if (grafo->matriz[verticeAtual][i] != 0 && !visitado[i]) {
                visitado[i] = 1;
                enfileirar(&fila, i);
            }
        }
    }
    printf("\n");
}

// Algoritmo de Busca em Profundidade (DFS) - versão recursiva
void DFSRecursivo(GrafoMatriz *grafo, int vertice, int visitado[]) {
    visitado[vertice] = 1;
    printf("%d ", vertice);
    
    for ( i = 0; i < grafo->numVertices; i++) {
        if (grafo->matriz[vertice][i] != 0 && !visitado[i]) {
            DFSRecursivo(grafo, i, visitado);
        }
    }
}

void DFS(GrafoMatriz *grafo, int verticeInicial) {
    int visitado[MAX_VERTICES] = {0};
    printf("Busca em Profundidade (DFS) a partir do vértice %d: ", verticeInicial);
    DFSRecursivo(grafo, verticeInicial, visitado);
    printf("\n");
}

// ========== FUNÇÃO PRINCIPAL ==========

int main() {
    printf("=== EXEMPLO DE GRAFOS EM C ===\n\n");
    
    // Exemplo com matriz de adjacência
    printf("1. Grafo com Matriz de Adjacência:\n");
    GrafoMatriz grafoMatriz;
    inicializarGrafoMatriz(&grafoMatriz, 5, 0); // 5 vértices, não direcionado
    
    adicionarArestaMatriz(&grafoMatriz, 0, 1, 1);
    adicionarArestaMatriz(&grafoMatriz, 0, 2, 1);
    adicionarArestaMatriz(&grafoMatriz, 1, 3, 1);
    adicionarArestaMatriz(&grafoMatriz, 2, 4, 1);
    adicionarArestaMatriz(&grafoMatriz, 3, 4, 1);
    
    imprimirGrafoMatriz(&grafoMatriz);
    printf("\n");
    
    // Executa BFS e DFS
    BFS(&grafoMatriz, 0);
    DFS(&grafoMatriz, 0);
    printf("\n");
    
    // Exemplo com lista de adjacência
    printf("2. Grafo com Lista de Adjacência:\n");
    GrafoLista grafoLista;
    inicializarGrafoLista(&grafoLista, 5, 0); // 5 vértices, não direcionado
    
    adicionarArestaLista(&grafoLista, 0, 1, 2);
    adicionarArestaLista(&grafoLista, 0, 2, 3);
    adicionarArestaLista(&grafoLista, 1, 3, 1);
    adicionarArestaLista(&grafoLista, 2, 4, 4);
    adicionarArestaLista(&grafoLista, 3, 4, 5);
    
    imprimirGrafoLista(&grafoLista);
    
    // Libera memória
    liberarGrafoLista(&grafoLista);
    
    return 0;
}