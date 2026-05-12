# 📝 Definições de Fluxos Técnicos para Documentação UML (Nex_TI)

Este guia contém as definições técnicas de fluxo para os Diagramas de Classe e Sequência de todos os 15 Casos de Uso (UC) do sistema. Use estas descrições para preencher a documentação oficial e as notas do Astah.

---

### UC01: Realizar Login
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `ServicoAutenticacao` (Controle) estabelece uma dependência com a classe `Usuario` (Entidade) para validar as credenciais privadas `-email` e `-senha`. A validação é processada pelo método `autenticar()`.
*   **Fluxo Alternativo:** Em caso de falha, o método `autenticar()` retorna um valor booleano falso, impedindo o acionamento das relações de navegação com as classes de interface do Dashboard.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Ator envia a mensagem `login(email, senha)` para a linha de vida `:ServicoAutenticacao`. O objeto executa o método de auto-chamada `validarCredenciais()` e retorna uma confirmação de sucesso ao usuário.
*   **Fluxo Alternativo:** Após a mensagem de login, a validação interna no objeto `:ServicoAutenticacao` falha, disparando uma mensagem de retorno de erro ("Credenciais Inválidas") e encerrando a sessão de ativação.

---

### UC02: Cadastrar Usuário
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `ServicoAutenticacao` (Controle) gerencia a criação de uma nova instância da classe `Aluno` (Entidade), que herda atributos da classe base `Usuario`. O método `registrar()` aciona o construtor da entidade.
*   **Fluxo Alternativo:** Antes da instanciação, o controlador realiza uma consulta de unicidade no atributo `email`. Se o valor já existir, a relação de criação (<<create>>) com a classe `Aluno` não é executada.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Visitante solicita `registrar(dados)`. O objeto `:ServicoAutenticacao` envia uma mensagem de criação (<<create>>) para uma nova linha de vida `:Aluno`, que então executa `inicializarPerfil()`.
*   **Fluxo Alternativo:** O objeto `:ServicoAutenticacao` detecta um conflito de dados no banco e retorna uma mensagem de erro "E-mail já cadastrado" ao visitante, sem criar o objeto Aluno.

---

### UC03: Realizar Teste de Nivelamento
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `Aluno` (Entidade) possui uma associação unidirecional com a classe `Simulado` (Entidade). O método `definirFaseInicial(nota)` da classe Aluno utiliza o resultado da classe Simulado para atualizar o atributo `-progresso`.
*   **Fluxo Alternativo:** O aluno aciona um método de bypass. A classe Aluno ignora a associação com `Simulado` e define o atributo `-progresso` como "Nível 1" diretamente.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Aluno envia `iniciarTeste()` para `:Simulado`. O simulado retorna a lista de questões. Após `enviarRespostas()`, o Aluno executa uma auto-mensagem `definirFaseInicial(nota)`.
*   **Fluxo Alternativo:** O Aluno envia a mensagem `pularTeste()`. O `:Sistema` intercepta a solicitação e envia uma mensagem de atualização de estado diretamente para o objeto `:Aluno`.

---

### UC04: Gerenciar Perfis e Acessos
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** O `Administrador` interage com o `GerenciadorAcesso` (Controle). Este controlador possui permissão para invocar o método `setPapel()` na entidade `Usuario` para alterar permissões de sistema.
*   **Fluxo Alternativo:** O `GerenciadorAcesso` valida se o ID do `Usuario` alvo é idêntico ao do `Administrador` logado. Se positivo, o método de alteração é bloqueado por regras de integridade.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Admin envia `alterarPapel(id, papel)` para `:GerenciadorAcesso`. O controlador envia `setPapel()` para o objeto `:Usuario` correspondente e retorna uma confirmação de sucesso.
*   **Fluxo Alternativo:** Ao tentar alterar o próprio perfil, o `:GerenciadorAcesso` detecta a violação de regra e retorna uma mensagem de erro de segurança, bloqueando a execução.

---

### UC05: Gerenciar Conteúdo e Cartas
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** Existe uma relação de Composição entre a classe `Modulo` e a classe `Flashcard_SM2`. O `Tutor` utiliza métodos da classe `Sistema` para gerenciar o ciclo de vida dessas entidades.
*   **Fluxo Alternativo:** Ao solicitar a exclusão, a classe `Sistema` verifica a multiplicidade da associação entre `Flashcard_SM2` e `Aluno`. Se houver dependências ativas, o método de remoção é substituído por um método de arquivamento.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Tutor solicita `novoModulo()`. O `:Sistema` cria o objeto `:Modulo`. Em seguida, o Tutor envia `adicionarCarta()` repetidamente para preencher a composição.
*   **Fluxo Alternativo:** O Tutor solicita `excluirModulo()`. O `:Sistema` realiza uma verificação interna de dependências e retorna uma sugestão de arquivamento ao invés de prosseguir com a destruição do objeto.

---

### UC06: Acompanhar Desempenho
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `PainelVisual` (Fronteira) lê o atributo `-progresso` da classe `Aluno` (Entidade) através de uma interface de consulta mediada pelo `Tutor`.
*   **Fluxo Alternativo:** Se o atributo `-progresso` for nulo ou insuficiente, a classe `PainelVisual` desvia sua lógica de renderização para exibir uma mensagem de estado vazio.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Tutor solicita `visualizar(id)` ao `:PainelVisual`. Este envia `obterMetricas()` para o objeto `:Aluno` e, após receber os dados, executa a auto-mensagem `renderizarGráficos()`.
*   **Fluxo Alternativo:** O `:PainelVisual` recebe uma resposta vazia de `:Aluno`. Ele retorna uma mensagem de erro "Dados insuficientes" ao Tutor, encerrando o fluxo sem gráficos.

---

### UC07: Escalar Dúvida para Tutor
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `AgenteIA` (Controle) cria uma associação temporária com a classe `Tutor` (Entidade) ao instanciar um objeto da classe `Duvida` que necessita de intervenção humana.
*   **Fluxo Alternativo:** Uma classe de monitoramento de SLA verifica o tempo de vida do objeto `Duvida`. Se o prazo expirar, a `prioridade` da Dúvida é elevada através de um método de escalonamento crítico.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O `:AgenteIA` detecta complexidade e envia `escalar(duvida)` para o objeto `:Tutor`. O Tutor posteriormente envia a mensagem de retorno com a `resposta` para o Aluno.
*   **Fluxo Alternativo:** O `:Sistema` monitora o tempo de resposta. Ao atingir o limite, ele envia `setPrioridadeAlta()` para o objeto `:Duvida` e dispara um alerta externo para a Coordenação.

---

### UC08: Consultar Agente IA
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `AgenteIA` (Controle) mantém uma relação de leitura com a entidade `Flashcard_SM2` para extrair contexto pedagógico e responder a dúvidas do Aluno através do método `responder()`.
*   **Fluxo Alternativo:** Caso o processamento de linguagem natural (NLP) falhe, a classe `AgenteIA` aciona uma relação de fallback com o fluxo de escalonamento para Tutor.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Aluno envia `enviarDuvida(texto)` para o `:AgenteIA`. O objeto executa `processarNLP()` internamente e retorna uma explicação detalhada ao Aluno.
*   **Fluxo Alternativo:** O `:AgenteIA` não consegue interpretar a mensagem. Ele retorna uma sugestão de reformulação ou uma opção direta para "Escalar para Tutor".

---

### UC09: Estudar Flashcards (SM-2)
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `MotorSM2` (Controle) atualiza o atributo `-proximaRevisao` na entidade `Flashcard_SM2` com base no feedback de dificuldade recebido do Aluno.
*   **Fluxo Alternativo:** O sistema de controle de acesso verifica a data do sistema contra o atributo `-proximaRevisao`. Se a condição não for atendida, o acesso aos métodos de estudo da entidade é bloqueado.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Aluno envia `informarDificuldade(1-5)` para o `:MotorSM2`. O motor executa `aplicarSM2()` e envia `setProximaRevisao(data)` para o objeto `:Flashcard_SM2`.
*   **Fluxo Alternativo:** O Aluno tenta abrir o Deck. O `:Sistema` envia uma consulta de agenda. Ao detectar que não há cards para hoje, retorna a mensagem "Metas Cumpridas".

---

### UC10: Criar Flashcards
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `Editor` (Fronteira) fornece a interface para o Aluno instanciar novos objetos `Flashcard_SM2`, que são automaticamente associados à coleção privada do Aluno.
*   **Fluxo Alternativo:** A classe `Editor` realiza uma validação de pré-condição nos atributos de entrada. Se o campo "Resposta" estiver vazio, a operação de persistência da entidade é abortada.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Aluno envia `salvar(p, r)` para o `:Editor`. O editor envia uma mensagem de criação (<<create>>) para o objeto `:Flashcard_SM2` e retorna sucesso ao Aluno.
*   **Fluxo Alternativo:** O Aluno tenta salvar dados incompletos. O `:Editor` detecta o erro de validação e retorna um alerta visual, mantendo a ativação da tela de edição.

---

### UC11: Realizar Simulado ENADE
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `Simulado` (Entidade) agrega múltiplas instâncias da classe `Questao`. A classe `Temporizador` monitora a duração da sessão de teste.
*   **Fluxo Alternativo:** Em caso de interrupção, o estado atual das questões e do tempo é transferido para uma classe de persistência local para garantir a resiliência dos dados.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Aluno envia `iniciarTeste()`. O `:Simulado` envia `iniciar()` para o `:Temporizador`. O Aluno envia respostas e o simulado retorna o relatório final.
*   **Fluxo Alternativo:** Durante o teste, ocorre uma queda de conexão. O `:Sistema` detecta o evento e envia a mensagem `salvarProgressoLocal()` para o armazenamento do navegador.

---

### UC12: Atribuir XP e Moedas
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `SistemaGamificacao` (Controle) altera os atributos `-pontos` e `+moedas` na entidade `Aluno` após a conclusão bem-sucedida de atividades educacionais.
*   **Fluxo Alternativo:** O controlador aplica um modificador de penalidade ao detectar comportamentos de burla, resultando em um incremento menor nos atributos de recompensa.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O `:Sistema` envia `concluirTarefa()` para o `:SistemaGamificacao`. O controlador executa `calcularRecompensas()` e envia `creditarXP(valor)` para o objeto `:Aluno`.
*   **Fluxo Alternativo:** O `:Sistema` detecta atividade suspeita e notifica o `:SistemaGamificacao`. O controlador altera sua lógica interna e envia um valor reduzido de XP para o `:Aluno`.

---

### UC13: Desbloquear Fases e Módulos
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `Loja` (Fronteira) verifica o saldo de `moedas` na entidade `Aluno`. Se suficiente, aciona o método `desbloquear()` para alterar o estado do atributo `bloqueada` na classe `Modulo`.
*   **Fluxo Alternativo:** Se o saldo for insuficiente, a transação entre as classes Aluno e Modulo é interrompida, mantendo o estado de bloqueio da entidade.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Aluno envia `comprar()` para a `:Loja`. A loja consulta `obterSaldo()` no `:Aluno`. Confirmado o saldo, envia `desbloquear()` para o objeto `:Modulo`.
*   **Fluxo Alternativo:** Após a consulta de saldo, a `:Loja` identifica insuficiência de fundos e retorna uma mensagem de erro "Saldo Insuficiente" ao Aluno.

---

### UC14: Visualizar Painel de Progresso
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `PainelVisual` (Fronteira) realiza consultas de leitura nos atributos de progresso e recompensas da entidade `Aluno` para composição do Dashboard.
*   **Fluxo Alternativo:** Caso a entidade `Aluno` não possua registros históricos, a classe `PainelVisual` ativa um estado de exibição inicial (Onboarding).

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Aluno solicita `abrirDashboard()`. O `:PainelVisual` envia `obterDadosProgresso()` para o `:Aluno` e executa a auto-mensagem `gerarHeatmap()`.
*   **Fluxo Alternativo:** O `:PainelVisual` recebe dados vazios de `:Aluno`. Ele altera o fluxo de renderização e exibe uma mensagem de boas-vindas com convites para estudo.

---

### UC15: Ajustar Acessibilidade
**1. Fluxo para Diagrama de Classe:**
*   **Fluxo Normal:** A classe `PainelConfiguracao` (Fronteira) persiste as escolhas do usuário na entidade `Acessibilidade`, que armazena configurações como tamanho de fonte e contraste.
*   **Fluxo Alternativo:** O método `restaurarPadroes()` limpa os estados da classe `Acessibilidade`, retornando os atributos aos valores originais do sistema.

**2. Fluxo para Diagrama de Sequência:**
*   **Fluxo Normal:** O Usuario envia `alterarConfiguracao()` para o `:PainelConfiguracao`. O objeto envia `salvarPreferencias()` para a entidade `:Acessibilidade` e atualiza a interface.
*   **Fluxo Alternativo:** O Usuario envia `restaurarPadroes()`. O `:PainelConfiguracao` envia uma mensagem de reset para a entidade `:Acessibilidade` e recarrega os estilos padrão.

---
*Fim do guia técnico de definições UML.*
