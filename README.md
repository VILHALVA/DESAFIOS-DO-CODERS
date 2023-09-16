# DESAFIOS DE PROGRAMADORES DO GRUPO CODERS
Bem-vindo aos Desafios de Programação do Grupo CODERS! Neste repositório, você encontrará uma série de desafios voltados para aprimorar suas habilidades de programação e desenvolvimento. Estes desafios foram criados pelos membros entusiastas do [Grupo CODERS](https://t.me/CODIGOGP) e são projetados para oferecer oportunidades de aprendizado e colaboração.

Se você é apaixonado por codificação e deseja expandir seus conhecimentos, este é o lugar certo para começar. Antes de mergulhar nos desafios, certifique-se de atender aos requisitos e seguir as regras estabelecidas para uma experiência suave.

Fique à vontade para explorar os desafios, fazer fork deste repositório e participar ativamente. Lembre-se de que a comunidade está aqui para ajudar e fornecer suporte, então, se tiver dúvidas ou precisar de assistência, não hesite em entrar em contato no nosso [Grupo CODERS](https://t.me/CODIGOGP).

Vamos juntos embarcar nesta jornada de aprendizado e programação! 

Claro, aqui está o requisito com uma explicação sobre por que é importante:

## REQUISITOS:
1. Antes de começar você deve fazer o curso de [GITHUB](https://github.com/VILHALVA/CURSO-DE-GITHUB).

   **Por que este requisito é importante?**

   Ter um conhecimento básico sobre o uso do GitHub é essencial para garantir uma colaboração suave e eficaz neste repositório de desafios. Aqui está por que:

   - **Fork**: O fork permite que você crie sua própria cópia do repositório para fazer suas alterações. Isso é fundamental para trabalhar em seu próprio ambiente antes de contribuir de volta.

   - **Commit**: Compreender como fazer commits é fundamental para salvar e registrar suas alterações no GitHub. Isso ajuda a manter um histórico claro das contribuições.

   - **Branch**: Criar e gerenciar branches é importante para trabalhar em recursos ou desafios separados sem afetar a versão principal do código.

   - **Pull Request (PR)**: O PR é a maneira padrão de sugerir alterações e colaborar em projetos do GitHub. Ao saber como criar um PR, você pode submeter suas contribuições para revisão.

   Portanto, fazer o curso de GitHub garantirá que você tenha as habilidades necessárias para participar ativamente e contribuir de forma eficiente para os desafios deste repositório.

2. Você precisa saber alguma linguagem de programação. Se não souber, [clique aqui](https://github.com/VILHALVA?tab=repositories&q=CURSO&type=public&language=&sort=) para fazer um de nossos cursos.

   **Por que este requisito é importante?**

   Ter conhecimento em uma linguagem de programação é fundamental para participar efetivamente dos desafios deste repositório. Aqui está o motivo:

   - **Execução dos Desafios**: Os desafios neste repositório envolvem codificação e resolução de problemas. Se você já possui conhecimento em uma linguagem de programação, estará em uma posição melhor para implementar as soluções.

   - **Compreensão das Instruções**: Para entender completamente as instruções de cada desafio e os requisitos específicos, é essencial ter um conhecimento básico de programação. Isso facilitará a interpretação das tarefas e a implementação das soluções.

   - **Capacidade de Depurar**: Às vezes, os desafios podem apresentar erros ou bugs que precisam ser corrigidos. Ter habilidades de programação permite que você depure seu código de maneira eficaz e resolva problemas quando eles surgirem.

   - **Contribuição Significativa**: Se você já conhece uma linguagem de programação, estará em uma posição melhor para contribuir com soluções de alta qualidade para os desafios e ajudar outros membros que possam ter dúvidas.

   Portanto, a familiaridade com uma linguagem de programação é um pré-requisito importante para garantir que você possa aproveitar ao máximo os desafios oferecidos neste repositório. Se você não possui conhecimento em programação, oferecemos cursos para ajudá-lo a adquirir as habilidades necessárias e participar plenamente.

## REGRAS:
1. **Conformidade com os Modelos**: Certifique-se de seguir rigorosamente os modelos estabelecidos para o nome das pastas, localização das pastas, nome dos arquivos e localização dos arquivos. Se você não estiver certo de como seguir esses modelos, você pode consultar os desafios do "VILHALVA" em cada DESAFIO como referência.

2. **Relevância das Alterações**: É importante que todas as alterações propostas estejam diretamente relacionadas ao desafio em que você está trabalhando. Não serão aceitas ou consideradas quaisquer tentativas de alteração que não sejam pertinentes ao escopo do desafio em questão.

3. **Aguardar Aprovação de Pull Request (PR)**: Após concluir seu desafio e criar um PR, por favor, tenha em mente que todos os envolvidos neste grupo são voluntários. Portanto, após a submissão do PR, aguarde pacientemente a aprovação. Um dos administradores (ADM) avaliará e mesclará seu trabalho assim que estiver disponível para fazê-lo.

4. **Solicitar Ajuda no Grupo**: Se, mesmo seguindo as regras e instruções, você encontrar dificuldades ou tiver alguma dúvida, sinta-se à vontade para solicitar ajuda em nosso [GRUPO](https://t.me/CODIGOGP). Nossa comunidade está aqui para apoiar e orientar uns aos outros, tornando a jornada de aprendizado mais fácil e eficaz.

Estas regras visam garantir um ambiente de colaboração produtivo e respeitoso, onde todos os membros possam contribuir e aprender de maneira construtiva.

## INSTRUNÇÕES:
1. Visite o [repositório DESAFIOS DO CODERS no github](https://github.com/VILHALVA/DESAFIOS-DO-CODERS).

2. Faça um _fork_ deste repositório clicando no botão `Fork` no canto superior da tela. Isso criará uma cópia completa do repositório sob o seu controle, no github.

3. Faça um clone do repositório para a sua estação de trabalho:
   ```
   git clone https://github.com/<seu_usuario_no_github>/DESAFIOS-DO-CODERS.git
   ```
4. Entre no diretório criado pelo git (`DESAFIOS-DO-CODERS`).

5. Crie um "git remote" chamado "upstream" apontando para o repositório principal. Isso facilitará a atualização do seu repositório local:
   ```
   git remote add upstream https://github.com/VILHALVA/DESAFIOS-DO-CODERS
   ```

6. **Antes de começar a trabalhar em qualquer desafio**: é importante resetar os números de _commit_ entre a sua cópia local e o repositório principal (isso acontece porque o repositório principal usa _rebase_ ao invés de _feature branches_). Existem duas maneiras de efetuar essa operação, mas a mais simples é usar "git reset" como indicado abaixo:
   ```
   git remote update
   git reset upstream/master --hard
   ```

   > **ATENÇÃO**
   >
   > Os comandos acima irão reverter **TODAS** as modificações no seu repositório.
   > É importante executá-los antes de introduzir qualquer modificação. Se você tem
   > modificações a preservar, a maneira mais simples (para um iniciante) é copiar
   > os arquivos a serem preservados para outro diretório, efetuar o `git reset`
   > indicado acima, e copiar os arquivos de volta.

7. Crie um _branch_ de trabalho com um nome adequado. No nosso exemplo, usaremos o nome "dev":
   ```
   git checkout -b dev
   ```

8. Faça o desafio dentro do repositório correspondente ao desafio. E neste repositório crie uma pasta com o seu primeiro nome ou sobrenome ou user do GITHUB. Ex: Dentro da pasta "DESAFIO 03" crie uma pasta com o nome "FULANO" (Coloque seu nome/sobrenome/user). Dentro da pasta "FULANO" coloque seus arquivos/códigos com o README.md contendo a descrição do projeto e requerimentos. Veja uma representação:
```
Projeto de Desafio
|
|-- DESAFIO 01
|   |
|   |-- SEU_NOME
|   |   |
|   |   |-- SeuArquivo.py
|   |   |-- README.md
|
|-- DESAFIO 02
|   |
|   |-- SEU_NOME
|   |   |
|   |   |-- SeuArquivo.js
|   |   |-- README.md
|
|-- DESAFIO 03
|   |
|   |-- SEU_NOME
|       |
|       |-- SeuArquivo.java
|       |-- README.md
|
...
```

9. Trabalhe normalmente no _branch_ de desenvolvimento. Quando estiver satisfeito
   com o resultado, faça o _commit_ e o _push_ com:
   ```
   git push origin dev --force
   ```

10. O `git push` transfere o conteúdo do seu branch corrente ("dev" nesse caso) para a o seu _fork_ no github. Visite a página do seu _fork_ no github (normalmente, https://github.com/SEU-USUARIO-NO-GITHUB/DESAFIOS-DO-CODERS) e clique no botão para abrir um PR.

## O QUE FAZER DEPOIS DO ENVIO?
Quando um PR é criado, o github envia um email para os admins, que farão a revisão das modificações e, em caso de aprovação, a incorporação (ou _merge_) das suas mudanças no repositório principal.

Um PR (ou _pull request_) é um **pedido** para incorporar as suas modificações ao repositório principal. A sua tarefa só estará terminada quando os admins tiverem incorporado as suas mudanças ao repositório principal (através de uma operação _merge_).

O repositório principal contém testes de integração que procuram por erros comuns e bloqueiam a aprovação até que estes tenham sido corrigidos. Por isso,
**fique atento ao seu email e a página do seu PR no github**. Verifique que os testes de integração passaram e procure por mensagens dos admins relacionadas ao seu PR.

Em caso de erros nos testes de integração ou pedido de mudança por parte dos admins, corrija o problema no seu repositório local e crie outro commit com `git commit`, seguido por `git push`. **Não crie outro PR, e não use o comando git reset até que as suas modificações tenham sido incorporadas no repositório principal.**

PRs sem atividade por duas semanas serão automaticamente fechados.

## PERGUNTAS FREQUENTES:
* **01) É OBRIGATÓRIO FAZER ESSES DESAFIOS?**

> R: Não, os desafios não são obrigatórios, mas altamente recomendados para iniciantes.

* **02) O QUE EU GANHO FAZENDO ESSES DESAFIOS?**

> R: Embora você não receba pontos ou recompensas materiais, existem vantagens significativas, incluindo:
    > **APRENDIZADO:** Você não apenas aprimora suas habilidades de programação, mas também ganha experiência prática com o GitHub, uma plataforma essencial para desenvolvedores.
    > **CONTRIBUIÇÃO:** Sua participação nos desafios é registrada em seu perfil do GitHub, o que pode ser um acréscimo valioso ao seu portfólio, demonstrando seu comprometimento com projetos colaborativos.
    > **SEUS PROJETOS:** Programar não se resume apenas a fazer cursos; criar seus próprios projetos pessoais é uma maneira eficaz de aplicar seus conhecimentos e desenvolver habilidades autênticas.

* **3) QUEM GARANTE QUE O CONTRIBUINTE NÃO COPIOU O CÓDIGO DE ALGUÉM OU USOU O CHATGPT?**

> R: Não temos a capacidade de verificar individualmente as fontes de código dos contribuintes, nem podemos garantir que alguém não tenha utilizado recursos como o ChatGPT. No entanto, incentivamos fortemente a originalidade e a ética na programação. Lembre-se de que, ao buscar oportunidades de emprego na área de TI, as empresas valorizam a habilidade de escrever código original e compreender profundamente os conceitos. O plágio pode prejudicar sua reputação profissional no longo prazo.
> PS: Caso tenha copiado o código de alguém, cite os devidos créditos (A fonte) no seu README.

## CONSIDERAÇÕES FINAIS:
Agradecemos por escolher fazer parte dos Desafios de Programação do Grupo CODERS. Nossa comunidade é construída por pessoas apaixonadas por programação, aprendizado e colaboração, e estamos empolgados em tê-lo a bordo.

Lembre-se de que os desafios são uma oportunidade valiosa para expandir seus conhecimentos e aprimorar suas habilidades de programação. Não importa se você é um iniciante ou um especialista, todos têm algo a aprender e a contribuir. Aqui estão algumas palavras finais de incentivo:

- **Aprenda e Compartilhe**: Use os desafios como uma plataforma para aprender novas técnicas e compartilhar seu conhecimento com os outros. A colaboração é a essência do nosso grupo.

- **Erro não é Fracasso**: Não tenha medo de cometer erros. Eles são uma parte natural do processo de aprendizado. Cada desafio é uma oportunidade para crescer.

- **Ajude e Seja Ajudado**: Se você tiver dúvidas ou precisar de assistência, nossa comunidade está aqui para ajudar. Ao mesmo tempo, não hesite em oferecer ajuda aos outros membros.

- **Divirta-se**: A programação pode ser desafiadora, mas também é divertida. Aproveite o processo e celebre suas conquistas.

- **A Comunidade Faz a Diferença**: O sucesso deste grupo depende da participação ativa de cada membro. Sua contribuição é valiosa e apreciada.

Estamos ansiosos para ver suas soluções criativas para os desafios e observar seu crescimento como desenvolvedor. Juntos, podemos alcançar novos patamares na programação. Vamos codificar! 🚀

## CREDITOS:
* [OS DESAFIOS FORAM CRIADOS PELO VILHALVA (DESAFIOS 02-10)](https://github.com/VILHALVA)
* [A SABRINA NOS AJUDOU EM: 1) DEU A SUGESTÃO DE VINCULARMOS ESSE PROJETO AO GRUPO. 2) NOS EMPRESTOU A SUA CONTA DO GITHUB PARA FAZER OS TESTES](https://github.com/SABRINA1623)
* [FORAM CRIADOS COM INSPIRAÇÃO DO "OS PROGRAMADORES": 1) NA IDEIA DE CRIAR DESAFIOS PARA INICIANTES. 2) NO TRECHO DESSE README (INSTRUNÇÕES/O QUE FAZER DEPOIS DO ENVIO?). 3) NO DESAFIO 01](https://osprogramadores.com/desafios/)
* [O CHATGPT NOS AJUDOU COM MELHORIAS DOS READMES](https://chat.openai.com)
