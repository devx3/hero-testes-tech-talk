# Hero Tech Talk - Testes e TDD

Todo o conteúdo passado no tech talk vai estar nesse documento.

## TDD
O objetivo geral é trazer uma visão sobre o TDD e como podemos trazer isso para a nossa rotina de desenvolvimento.

### O que é TDD?
TDD vem de *Test Driven Development* ou, traduzido em terra tupiniquim como Desenvolvimento Orientado a Testes. A ideia do
TDD é trabalhar em ciclos, que acontecem na seguinte ordem: 

- Primeiro escrevemos um teste que deve falhar. Nessa etapa o código ainda não foi nem implementado;
- Depois, criamos o código que vai fazer o nosso teste passar;
- Feito isso, refatoramos o código para melhorar alguns pontos como deixá-lo legível. É necessário testar novamente e garantir que o novo código continue passando no teste.

E definitivamente o TDD não é uma forma de escrever testes, e sim, uma metodologia de desenvolvimento e escrita de códigos.


### Ciclo do TDD
![](https://dkrn4sk0rn31v.cloudfront.net/2019/11/04105020/img-tdd.png)

- **Red:** escreva um pequeno teste automatizado que, ao ser executado, irá falhar;
- **Green:** implemente um código que seja suficiente para ser aprovado no teste recém-escrito;
- **Refactor:** refatore o código, a fim dele ser melhorado, deixando-o mais funcional e mais limpo.

Esse ciclo é chamado de **red-green-refactor** ou **red-green-blue**.

### Por que utilizar TDD?

Um dos benefícios do TDD é que, como você vai saber exatamente o que precisa fazer antecipadamente, você acaba evitando criar algo muito complexo ou que não siga os pré-requisitos do negócio.

Outra vantagem é que quando você deixa para executar os testes posteriormente, provavelmente você não vai testar como deveria. Isso acaba abrindo margem para alterações no código para resolver testes que falharam, aumentando a possibilidade de criar bugs por conta dessas alterações.

Mesmo que pareça uma etapa a mais no desenvolvimento, usar TDD pode prevenir muitas falhas e re-trabalho no futuro.

### Quando utilizar TDD?
A ideia é que você utilize o TDD em testes unitários - testes que vão avaliar o comportamento de funções, classes e métodos em específico.

### Como os mocks se aplicam na nossa área

"PUTA MADRE, COMO EU VOU FAZER ESSE CARAJO?"

Essa frase soa familiar para você? Pois é, ela sempre vem na minha cabeça antes de começar a criar uma nova funcionalidade. 

A questão é que com o TDD, partimos do pressuposto que **você já sabe** qual o resultado que espera obter daquele trecho específico de código. Logo, isso nos força a parar, pensar e somente depois disso, começar a desenvolver uma solução. 



## Fontes: 

https://www.treinaweb.com.br/blog/afinal-o-que-e-tdd