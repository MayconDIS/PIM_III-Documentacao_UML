import os

use_cases = [
    {
        "id": "UC01_Realizar_Login",
        "title": "Realizar Login",
        "desc": "Acesso seguro do usuário ao sistema através de validação de credenciais.",
        "astah_tips": "Dica Astah: Utilize 'Activation Bars' para mostrar o processamento no Controlador.",
        "steps_class": [
            "Crie a classe 'MD_Usuarios' (Entidade de Dados).",
            "Adicione os atributos: '+ email: texto' e '+ senha: texto'.",
            "Crie a classe 'ControladorAutenticacao' (Lógica de Controle).",
            "Adicione o método: '+ autenticar(email, senha)'.",
            "Desenhe uma seta de 'Dependência' (tracejada) saindo do Controlador para a Entidade."
        ],
        "steps_seq": [
            "Adicione o Ator 'Usuario' e o Participante 'ControladorAutenticacao'.",
            "Desenhe uma 'Mensagem Síncrona' do Usuario para o Controlador chamando 'login(email, senha)'.",
            "No Controlador, adicione uma 'Mensagem para si mesmo' (Self-Message) chamada 'validarCredenciais()'.",
            "Desenhe a 'Mensagem de Resposta' (seta tracejada) voltando para o Usuario com o resultado."
        ],
        "mermaid_class": "classDiagram\n    class MD_Usuarios {\n        +string email\n        +string senha\n    }\n    class ControladorAutenticacao {\n        +autenticar(email, senha)\n    }\n    ControladorAutenticacao ..> MD_Usuarios : consulta",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant U as Usuario\n    participant C as ControladorAutenticacao\n    U->>C: login(email, senha)\n    activate C\n    C->>C: validarCredenciais()\n    C-->>U: Retorno (Sucesso/Erro)\n    deactivate C"
    },
    {
        "id": "UC02_Cadastrar_Usuario",
        "title": "Cadastrar Usuário",
        "desc": "Registro de novos alunos com inicialização automática de perfil de gamificação.",
        "astah_tips": "Dica Astah: A seta de Herança (Generalização) é a que possui o triângulo na ponta.",
        "steps_class": [
            "Crie a classe base 'MD_Usuarios' com 'nome' e 'email'.",
            "Crie a classe 'MD_Alunos'.",
            "Desenhe a 'Generalização' (Herança) de MD_Alunos apontando para MD_Usuarios.",
            "Adicione em MD_Alunos os atributos: '+ pontos: int' e '+ moedas: int'."
        ],
        "steps_seq": [
            "Coloque os participantes: Visitante, ControladorAutenticacao e MD_Alunos.",
            "Mensagem 1: Visitante solicita 'registrar(dados)' ao Controlador.",
            "Mensagem 2: O Controlador cria o objeto 'MD_Alunos' (utilize a mensagem de criação 'Create').",
            "Mensagem 3: O objeto recém-criado executa internamente 'inicializarPerfil()'."
        ],
        "mermaid_class": "classDiagram\n    MD_Usuarios <|-- MD_Alunos\n    class MD_Usuarios {\n        +string nome\n        +string email\n    }\n    class MD_Alunos {\n        +int pontos\n        +int moedas\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant V as Visitante\n    participant C as ControladorAutenticacao\n    participant A as MD_Alunos\n    V->>C: registrar(dados)\n    activate C\n    C-->>A: <<create>>\n    activate A\n    A->>A: inicializarPerfil()\n    deactivate A\n    C-->>V: Cadastro Confirmado\n    deactivate C"
    },
    {
        "id": "UC03_Realizar_Teste_Nivelamento",
        "title": "Teste de Nivelamento",
        "desc": "Avaliação diagnóstica para posicionamento do aluno no mapa de conhecimento.",
        "astah_tips": "Dica Astah: Use Agregação (losango vazio) para mostrar que o Simulado agrega questões.",
        "steps_class": [
            "Crie 'MD_Alunos' com o método '+ definirFaseInicial(nota)'.",
            "Crie 'MD_Simulado' com o método '+ iniciarTeste()'.",
            "Desenhe uma 'Associação Unidirecional' (seta simples) do Aluno para o Simulado."
        ],
        "steps_seq": [
            "O Aluno chama 'iniciarTeste()' no objeto MD_Simulado.",
            "O Simulado retorna uma lista de questões para o Aluno.",
            "Após responder, o Aluno chama 'enviarRespostas()' no Simulado.",
            "O Aluno executa em si mesmo 'definirFaseInicial(nota)' após receber o resultado."
        ],
        "mermaid_class": "classDiagram\n    class MD_Alunos {\n        +definirFaseInicial(nota)\n    }\n    class MD_Simulado {\n        +float nota\n        +iniciarTeste()\n    }\n    MD_Alunos --> MD_Simulado : realiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant S as MD_Simulado\n    A->>S: iniciarTeste()\n    activate S\n    S-->>A: Lista de Questões\n    A->>S: enviarRespostas()\n    S-->>A: notaFinal\n    deactivate S\n    A->>A: definirFaseInicial(nota)"
    },
    {
        "id": "UC04_Gerenciar_Perfis_Acessos",
        "title": "Gerenciar Perfis e Acessos",
        "desc": "Administração de papéis (Admin, Tutor, Aluno) e permissões de sistema.",
        "astah_tips": "Dica Astah: Utilize 'Notes' (Notas) para explicar o que cada papel (role) pode fazer.",
        "steps_class": [
            "Crie 'MD_Admin' e 'MD_Usuarios'.",
            "Em 'MD_Usuarios', adicione o atributo '+ papel: texto'.",
            "Crie 'GerenciadorAcesso' para mediar a troca de papéis.",
            "Desenhe uma seta de 'Associação' de Admin para Usuarios."
        ],
        "steps_seq": [
            "O Admin solicita 'alterarPapel()' ao GerenciadorAcesso.",
            "O GerenciadorAcesso valida a permissão e chama 'setPapel()' no MD_Usuarios alvo.",
            "O MD_Usuarios confirma a atualização e o Gerenciador retorna o sucesso ao Admin."
        ],
        "mermaid_class": "classDiagram\n    class MD_Admin {\n        +gerenciarAcesso()\n    }\n    class MD_Usuarios {\n        +string papel\n    }\n    MD_Admin --> MD_Usuarios : administra",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Admin\n    participant M as GerenciadorAcesso\n    participant U as MD_Usuarios\n    A->>M: alterarPapel(usuario_id, papel)\n    activate M\n    M->>U: setPapel(papel)\n    U-->>M: ok\n    M-->>A: Alteração Concluída\n    deactivate M"
    },
    {
        "id": "UC05_Gerenciar_Conteudo_Cartas",
        "title": "Gerenciar Conteúdo e Cartas",
        "desc": "Criação e manutenção de flashcards e módulos de estudo pelos tutores.",
        "astah_tips": "Dica Astah: A Composição é representada por um losango preenchido no lado do Módulo.",
        "steps_class": [
            "Crie 'MD_Modulos' e 'MD_Flashcards'.",
            "Desenhe uma 'Composição' de MD_Modulos para MD_Flashcards (losango preto no Módulo).",
            "Adicione em MD_Modulos o atributo '+ nomeModulo: texto'."
        ],
        "steps_seq": [
            "O Tutor solicita a criação de um 'novoModulo(nome)' ao Sistema.",
            "O Sistema instancia (Create) um novo objeto 'MD_Modulos'.",
            "O Tutor adiciona cartas chamando 'adicionarCarta(p, r)' no sistema, que vincula ao módulo criado."
        ],
        "mermaid_class": "classDiagram\n    MD_Modulos *-- MD_Flashcards\n    class MD_Tutor {\n        +gerenciarConteudo()\n    }\n    class MD_Modulos {\n        +string nomeModulo\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant T as Tutor\n    participant S as Sistema\n    participant M as MD_Modulos\n    T->>S: novoModulo(nome)\n    S->>M: <<create>>\n    T->>S: adicionarCarta(p, r)\n    S-->>T: Conteúdo Salvo"
    },
    {
        "id": "UC06_Acompanhar_Desempenho",
        "title": "Acompanhar Desempenho",
        "desc": "Visualização de métricas de progresso e engajamento dos alunos.",
        "astah_tips": "Dica Astah: O PainelVisual é uma classe de 'Fronteira' (Interface de Usuário).",
        "steps_class": [
            "Crie as classes 'MD_Tutor', 'MD_Alunos' e 'PainelVisual'.",
            "Em 'MD_Alunos', defina '+ progresso: decimal'.",
            "Desenhe uma 'Dependência' do Tutor para o Aluno através do PainelVisual."
        ],
        "steps_seq": [
            "Tutor interage com 'PainelVisual' solicitando 'visualizar(aluno_id)'.",
            "O PainelVisual busca dados reais no objeto 'MD_Alunos' chamando 'obterMetricas()'.",
            "O Aluno devolve os dados e o Painel renderiza o relatório final para o Tutor."
        ],
        "mermaid_class": "classDiagram\n    class MD_Tutor {\n        +acompanharDesempenho()\n    }\n    class MD_Alunos {\n        +float progresso\n    }\n    MD_Tutor ..> MD_Alunos : visualiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant T as Tutor\n    participant D as PainelVisual\n    participant A as MD_Alunos\n    T->>D: visualizar(aluno_id)\n    activate D\n    D->>A: obterMetricas()\n    A-->>D: dados_progresso\n    D-->>T: Relatório Visual\n    deactivate D"
    },
    {
        "id": "UC07_Escalar_Duvida_Tutor",
        "title": "Escalar Dúvida para Tutor",
        "desc": "Transferência de suporte da IA para um tutor humano quando a complexidade excede o limite do agente.",
        "astah_tips": "Dica Astah: Represente a escala de dúvida como uma seta de 'Associação' simples entre os dois agentes.",
        "steps_class": [
            "Crie a classe 'AgenteIA' com os métodos '+ analisarAmbiguidade()' e '+ escalar(duvida)'.",
            "Crie 'MD_Tutor' com '+ responderDuvida()'.",
            "Ligue 'AgenteIA' a 'MD_Tutor' com uma seta de 'Associação'."
        ],
        "steps_seq": [
            "O AgenteIA detecta internamente que a pergunta é complexa demais ('detectarComplexidade').",
            "O AgenteIA dispara uma mensagem para o MD_Tutor: 'escalar(duvida, aluno_id)'.",
            "O Tutor processa a dúvida e envia a resposta final diretamente ao Aluno."
        ],
        "mermaid_class": "classDiagram\n    class AgenteIA {\n        +analisarAmbiguidade()\n        +escalar(duvida)\n    }\n    class MD_Tutor {\n        +responderDuvida()\n    }\n    AgenteIA --> MD_Tutor : notifica",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant IA as AgenteIA\n    participant T as MD_Tutor\n    participant Al as Aluno\n    IA->>IA: detectarComplexidade()\n    IA->>T: escalar(duvida, aluno_id)\n    Note right of T: Tutor analisa o contexto\n    T-->>Al: Resposta Detalhada (Email/App)"
    },
    {
        "id": "UC08_Consultar_Agente_IA",
        "title": "Consultar Agente IA",
        "desc": "Interação instantânea com o especialista virtual para dúvidas pontuais.",
        "astah_tips": "Dica Astah: A dependência aqui indica que a IA 'conhece' a estrutura das dúvidas salvas.",
        "steps_class": [
            "Crie 'AgenteIA' com '+ responder(pergunta)'.",
            "Crie 'MD_Duvidas' com os atributos '+ pergunta: texto' e '+ resposta: texto'.",
            "Desenhe uma 'Dependência' da IA para a classe MD_Duvidas."
        ],
        "steps_seq": [
            "O Aluno envia sua dúvida para o AgenteIA.",
            "O AgenteIA ativa seu processamento de linguagem natural ('processarLinguagemNatural').",
            "O AgenteIA gera uma resposta e a entrega instantaneamente ao Aluno."
        ],
        "mermaid_class": "classDiagram\n    class AgenteIA {\n        +responder(pergunta)\n    }\n    class MD_Duvidas {\n        +string pergunta\n        +string resposta\n    }\n    AgenteIA ..> MD_Duvidas : consulta",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant IA as AgenteIA\n    A->>IA: enviarDuvida(texto)\n    activate IA\n    IA->>IA: processarLinguagemNatural()\n    IA-->>A: Resposta Sugerida\n    deactivate IA"
    },
    {
        "id": "UC09_Estudar_Flashcards",
        "title": "Estudar Flashcards (SM-2)",
        "desc": "Ciclo de estudo principal utilizando o algoritmo de repetição espaçada.",
        "astah_tips": "Dica Astah: No Astah, use o símbolo de 'Loop' (Combined Fragment) para cercar a revisão de cartas.",
        "steps_class": [
            "Crie 'MD_MotorSM2' e 'MD_Flashcards'.",
            "Em 'MD_MotorSM2', adicione o método '+ aplicarSM2(feedback)'.",
            "Desenhe uma seta de 'Associação' do Motor para o Flashcard."
        ],
        "steps_seq": [
            "O Aluno lê uma pergunta no MD_Flashcards.",
            "O Aluno informa a dificuldade (feedback de 1 a 5) ao MD_MotorSM2.",
            "O Motor processa o algoritmo ('aplicarSM2') e chama 'setProximaRevisao(data)' no Flashcard.",
            "O Flashcard é agendado para o futuro e o processo termina."
        ],
        "mermaid_class": "classDiagram\n    class MD_MotorSM2 {\n        +aplicarSM2(feedback)\n    }\n    class MD_Flashcards {\n        +date proximaRevisao\n    }\n    MD_MotorSM2 --> MD_Flashcards : atualiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant M as MD_MotorSM2\n    participant F as MD_Flashcards\n    A->>F: lerPergunta()\n    A->>F: verResposta()\n    A->>M: informarDificuldade(1-5)\n    M->>M: aplicarSM2()\n    M->>F: setProximaRevisao(data)\n    F-->>A: Carta Agendada"
    },
    {
        "id": "UC10_Criar_Flashcards",
        "title": "Criar Flashcards",
        "desc": "Funcionalidade que permite ao aluno personalizar seu próprio deck de estudos.",
        "astah_tips": "Dica Astah: Use a multiplicidade '1' no Aluno e '*' no Flashcard para indicar posse.",
        "steps_class": [
            "Crie 'MD_Alunos' e 'MD_Flashcards'.",
            "Adicione em MD_Alunos o método '+ criarCarta()'.",
            "Desenhe uma 'Associação' de MD_Alunos para MD_Flashcards."
        ],
        "steps_seq": [
            "O Aluno utiliza um 'Editor' (Interface) para digitar pergunta e resposta.",
            "O Editor envia os dados para 'MD_Flashcards' via comando '<<create>>'.",
            "A nova carta é salva vinculada ao ID do Aluno."
        ],
        "mermaid_class": "classDiagram\n    class MD_Alunos {\n        +criarCarta()\n    }\n    class MD_Flashcards {\n        +string pergunta\n        +string resposta\n    }\n    MD_Alunos \"1\" --> \"*\" MD_Flashcards : cria",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant E as Editor\n    participant F as MD_Flashcards\n    A->>E: entradaDados(p, r)\n    E->>F: <<create>>(p, r, usuario_id)\n    F-->>A: Carta Adicionada ao Deck"
    },
    {
        "id": "UC11_Realizar_Simulado_ENADE",
        "title": "Realizar Simulado ENADE",
        "desc": "Treinamento intensivo com tempo controlado e questões de exames oficiais.",
        "astah_tips": "Dica Astah: Utilize o 'Combined Fragment' do tipo 'Loop' para as questões e 'Opt' para o estouro de tempo.",
        "steps_class": [
            "Crie 'MD_Simulado' e 'Questao'.",
            "Ligue-as com uma 'Composição' (losango preto no Simulado).",
            "Em 'MD_Simulado', adicione '+ tempoRestante: int' e '+ calcularNota()'."
        ],
        "steps_seq": [
            "O Aluno inicia o Simulado.",
            "O Simulado aciona um 'Temporizador' para controlar os 120 minutos.",
            "Dentro de um 'Loop', o Aluno responde cada questão.",
            "Ao final, o Simulado desliga o cronômetro e devolve a Nota Final."
        ],
        "mermaid_class": "classDiagram\n    class MD_Simulado {\n        +int tempoRestante\n        +iniciarTeste()\n        +calcularNota()\n    }\n    class Questao {\n        +string texto\n    }\n    MD_Simulado \"1\" *-- \"*\" Questao",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant S as MD_Simulado\n    participant T as Temporizador\n    A->>S: iniciarTeste()\n    activate S\n    S->>T: iniciar(120min)\n    loop Cada Questão\n        A->>S: responder(id, opcao)\n    end\n    A->>S: finalizar()\n    S->>T: parar()\n    S-->>A: Nota e Feedback\n    deactivate S"
    },
    {
        "id": "UC12_Atribuir_XP_Moedas",
        "title": "Atribuir XP e Moedas",
        "desc": "Motor de recompensas automático baseado na conclusão de atividades.",
        "astah_tips": "Dica Astah: A dependência aqui mostra que a Gamificação 'atualiza' o Aluno.",
        "steps_class": [
            "Crie 'MD_Gamificacao' e 'MD_Alunos'.",
            "Em 'MD_Alunos', certifique-se de ter os atributos '+ pontos' e '+ moedas'.",
            "Desenhe uma 'Dependência' de MD_Gamificacao para MD_Alunos."
        ],
        "steps_seq": [
            "O Sistema notifica o motor de 'MD_Gamificacao' sobre uma tarefa concluída.",
            "O motor executa o cálculo de bônus internamente ('calcularBonus').",
            "O motor chama 'creditarXP(valor)' no objeto Aluno correspondente."
        ],
        "mermaid_class": "classDiagram\n    class MD_Gamificacao {\n        +calcularBonus()\n        +creditarXP(id, valor)\n    }\n    class MD_Alunos {\n        +int pontos\n        +int moedas\n    }\n    MD_Gamificacao ..> MD_Alunos : credita",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant S as Sistema\n    participant G as MD_Gamificacao\n    participant A as MD_Alunos\n    S->>G: notificarConclusao()\n    activate G\n    G->>G: calcularBonus()\n    G->>A: creditarXP(id, 100)\n    G-->>S: Atualizado\n    deactivate G"
    },
    {
        "id": "UC13_Desbloquear_Fases_Modulos",
        "title": "Desbloquear Fases e Módulos",
        "desc": "Progressão de conteúdo condicionada ao desempenho nas fases anteriores.",
        "astah_tips": "Dica Astah: Use a Dependência para mostrar que as Fases dependem do progresso do Aluno.",
        "steps_class": [
            "Crie 'MD_Fases' com '+ bloqueada: booleano' e '+ desbloquear()'.",
            "Crie 'GerenciadorProgresso' (Controle).",
            "Desenhe uma 'Dependência' do Gerenciador para MD_Alunos e MD_Fases."
        ],
        "steps_seq": [
            "O GerenciadorProgresso solicita ao Aluno o seu 'obterProgressoTotal()'.",
            "Se o valor for satisfatório, o Gerenciador chama 'desbloquear()' na classe MD_Fases.",
            "A classe Fases altera seu estado interno de 'bloqueada' para falso."
        ],
        "mermaid_class": "classDiagram\n    class MD_Fases {\n        +bool bloqueada\n        +desbloquear()\n    }\n    class MD_Alunos {\n        +float progresso\n    }\n    MD_Fases ..> MD_Alunos : verifica",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant M as GerenciadorProgresso\n    participant A as MD_Alunos\n    participant F as MD_Fases\n    M->>A: obterProgressoTotal()\n    A-->>M: 0.85\n    M->>F: desbloquear()\n    F->>F: setBloqueada(false)\n    F-->>M: Liberada"
    },
    {
        "id": "UC14_Visualizar_Painel_Progresso",
        "title": "Visualizar Painel de Progresso",
        "desc": "Hub central onde o aluno acompanha sua jornada e conquistas.",
        "astah_tips": "Dica Astah: O PainelVisual é uma classe de 'Fronteira'. Use o estereótipo <<boundary>> no Astah.",
        "steps_class": [
            "Crie 'PainelVisual' e 'MD_Alunos'.",
            "Em 'PainelVisual', adicione o método '+ renderizarDados()'.",
            "Desenhe uma 'Dependência' do Painel para o Aluno (leitura de dados)."
        ],
        "steps_seq": [
            "O Aluno abre a tela de início ('abrirInicio').",
            "O PainelVisual executa internamente a renderização dos componentes gráficos.",
            "O Painel solicita ao Aluno os dados de progresso e exibe tudo na tela."
        ],
        "mermaid_class": "classDiagram\n    class PainelVisual {\n        +renderizarDados()\n    }\n    class MD_Alunos {\n        +obterProgressoTotal()\n    }\n    PainelVisual ..> MD_Alunos : lê",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant Al as Aluno\n    participant D as PainelVisual\n    Al->>D: abrirInicio()\n    activate D\n    D->>D: renderizarDados()\n    D-->>Al: Visualização Completa\n    deactivate D"
    },
    {
        "id": "UC15_Ajustar_Acessibilidade",
        "title": "Ajustar Acessibilidade",
        "desc": "Personalização da interface para garantir inclusão e conforto visual.",
        "astah_tips": "Dica Astah: Adicione atributos como 'tamanhoFonte' com valores padrão (ex: 12).",
        "steps_class": [
            "Crie 'MD_Acessibilidade' com os atributos '+ altoContraste: bool' e '+ tamanhoFonte: int'.",
            "Adicione o método '+ salvarConfiguracao()'.",
            "Não são necessárias associações externas para este UC isolado."
        ],
        "steps_seq": [
            "O Usuario interage com o 'PainelConfiguracao' escolhendo as opções.",
            "O Painel envia o comando 'salvarConfiguracao()' para a classe MD_Acessibilidade.",
            "A interface é atualizada instantaneamente para refletir as novas escolhas."
        ],
        "mermaid_class": "classDiagram\n    class MD_Acessibilidade {\n        +bool altoContraste\n        +int tamanhoFonte\n        +salvarConfiguracao()\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant U as Usuario\n    participant P as PainelConfiguracao\n    participant A as MD_Acessibilidade\n    U->>P: selecionarOpcoes(contraste, fonte)\n    P->>A: salvarConfiguracao()\n    A-->>P: ok\n    P-->>U: Interface Atualizada"
    }
]

# Caminhos organizados
base_path = "c:/Users/mayco/Documents/GitHub/Documentacao_UML/PIM_III/02_Modelagem_UML_Astah"
dashboard_path = "c:/Users/mayco/Documents/GitHub/Documentacao_UML/PIM_III/01_Gestao_e_Planejamento/DASHBOARD_VISUAL.md"

# 1. Gerar os READMEs individuais (Super Detalhados)
for uc in use_cases:
    folder_path = os.path.join(base_path, uc["id"])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, "README.md")
    
    content = f"# 📘 Guia de Modelagem Detalhado: {uc['title']}\n\n"
    content += f"## 🎯 Objetivo\n{uc['desc']}\n\n"
    content += f"> [!IMPORTANT]\n> {uc['astah_tips']}\n\n"
    
    content += "## 🚀 Tutorial de Execução Passo a Passo no Astah\n\n"
    
    content += "### 1️⃣ Construindo o Diagrama de Classe (O QUE criar)\n"
    content += f"Siga esta ordem exata para garantir a consistência:\n"
    for i, step in enumerate(uc["steps_class"], 1):
        content += f"   - [ ] {i}. **{step}**\n"
    content += "\n**Como conectar?** Utilize as ferramentas de ligação na barra lateral do Astah. Se for Herança, procure pelo ícone de triângulo. Se for Dependência, use a linha tracejada.\n\n"
    
    content += "### 2️⃣ Construindo o Diagrama de Sequência (COMO o processo flui)\n"
    content += f"Desenhe a interação temporal entre as classes:\n"
    for i, step in enumerate(uc["steps_seq"], 1):
        content += f"   - [ ] {i}. **{step}**\n"
    content += "\n**Dica Visual:** No Astah, as mensagens de retorno (setas tracejadas) são configuradas nas propriedades da mensagem enviada ou desenhadas separadamente.\n\n"
    
    content += "---\n\n"
    content += "## 📊 Referência Visual (Modelo Final)\n"
    content += "### Diagrama de Classe\n"
    content += f"```mermaid\n{uc['mermaid_class']}\n```\n\n"
    content += "### Diagrama de Sequência\n"
    content += f"```mermaid\n{uc['mermaid_seq']}\n```\n\n"
    content += "---\n*Este guia foi projetado para ser infalível. Siga os passos acima e sua modelagem estará tecnicamente perfeita.*"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Gerar o Dashboard Visual
db_content = "# 🚀 Painel de Modelagem: 15 Casos de Uso\n\n"
db_content += "Este documento centraliza os **Diagramas de Classe e Sequência** individuais em Português.\n\n"
db_content += "## 📑 Índice de Casos de Uso\n"
for uc in use_cases:
    db_content += f"- [{uc['title']}](#{uc['id'].lower().replace('_', '-')})\n"

for uc in use_cases:
    db_content += f"\n---\n\n## {uc['id']} - {uc['title']}\n"
    db_content += f"**Objetivo:** {uc['desc']}\n\n"
    db_content += "### 📐 Diagramas Dedicados\n"
    db_content += "#### Diagrama de Classe\n"
    db_content += f"```mermaid\n{uc['mermaid_class']}\n```\n"
    db_content += "#### Diagrama de Sequência\n"
    db_content += f"```mermaid\n{uc['mermaid_seq']}\n```\n"
    db_content += f"\n[👉 Abrir Tutorial de Execução Detalhado](../02_Modelagem_UML_Astah/{uc['id']}/README.md)\n"

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(db_content)

print("Tutorial Avançado gerado com sucesso em todos os READMEs.")
