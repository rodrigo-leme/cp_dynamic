Imagine a Torre de Hanoi como um brinquedo com três varetas (A, B e C) e discos de diferentes tamanhos.
No início, todos os discos estão empilhados na vareta A, do maior (embaixo) até o menor (em cima), como uma barra de supino da academia.




Seguindo a explicação da logica do código;
A ideia fundamental é a seguinte:
1.	Para mover n discos da origem para o destino: 
Primeiro, movemos (n-1) discos da origem para a haste auxiliar

Depois, movemos o disco n (o maior que resta) da origem para o destino

Finalmente, movemos os (n-1) discos da haste auxiliar para o destino

Caso base: Se n=1, simplesmente movemos o disco diretamente da origem para o destino.
Recursão: Para cada subproblema de mover (n-1) discos, aplica a mesma lógica, criando uma cadeia de subproblemas cada vez menores
Isso porque não colocamos um disco maior em cima de um menor, pois sempre movemos primeiro os discos menores para fora do caminho
a recursão termina quando alcançamos o caso base (n=1)
  as chamadas recursivas encadeadas garantem que todos os discos são movidos seguindo as regras
