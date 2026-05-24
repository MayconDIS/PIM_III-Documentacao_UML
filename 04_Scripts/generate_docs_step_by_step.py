import os

use_cases = [
    {
        "id": "UC01_Realizar_Login",
        "title": "Realizar Login",
        "desc": "Acesso seguro do usuário ao sistema através de validação de credenciais.",
        "astah_tips": "Dica Astah: Utilize 'Activation Bars' para mostrar o processamento no Controlador.",
        "steps_class": [
            "Crie a classe 'Usuario' e aplique o Estereótipo <<Entidade>>.",
            "Adicione os atributos: '- email : string' e '- senha : string'.",
            "Crie a classe 'ServicoAutenticacao' e aplique o Estereótipo <<Controle>>.",
            "Adicione o método: '+ autenticar(email : string, senha : string) : bool'.",
            "Desenhe uma seta de 'Dependência' (tracejada) saindo do Controlador para a Entidade."
        ],
        "steps_seq": [
            "Adicione o Ator 'Usuario' e a Linha de Vida ':ServicoAutenticacao'.",
            "Mensagem 1: Usuario envia 'login(email, senha)' para o Controlador.",
            "Mensagem 1.1: O Controlador executa nele mesmo 'validarCredenciais()'.",
            "Mensagem de Retorno: Seta tracejada voltando para o Usuario com o Resultado."
        ],
        "mermaid_class": "classDiagram\n    class Usuario {\n        <<Entidade>>\n        -email : string\n        -senha : string\n    }\n    class ServicoAutenticacao {\n        <<Controle>>\n        +autenticar(email : string, senha : string) : bool\n    }\n    ServicoAutenticacao ..> Usuario : consulta",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant U as Usuário (Ator)\n    participant C as :ServicoAutenticacao\n    U->>C: login(email, senha)\n    activate C\n    C->>C: validarCredenciais()\n    C-->>U: Resultado (Sucesso/Erro)\n    deactivate C"
    },
    {
        "id": "UC02_Cadastrar_Usuario",
        "title": "Cadastrar Usuário",
        "desc": "Registro de novos alunos com inicialização automática de perfil de gamificação.",
        "astah_tips": "Dica Astah: A seta de Herança (Generalização) é a que possui o triângulo na ponta.",
        "steps_class": [
            "Crie a classe base 'Usuario' com '- nome : string' e '- email : string'.",
            "Crie a classe 'Aluno' (Estereótipo <<Entidade>>).",
            "Desenhe a 'Generalização' (Herança) de Aluno apontando para Usuario.",
            "Adicione em Aluno os atributos: '- pontos : int' e '- moedas : int'."
        ],
        "steps_seq": [
            "Linhas de Vida: :Visitante, :ServicoAutenticacao e :Aluno.",
            "Mensagem 1: Visitante solicita 'registrar(dados)'.",
            "Mensagem 2: O Controlador cria o objeto 'Aluno' usando a seta de 'Create Message'.",
            "Mensagem 3: O objeto recém-criado executa internamente 'inicializarPerfil()'."
        ],
        "mermaid_class": "classDiagram\n    Usuario <|-- Aluno\n    class Usuario {\n        -nome : string\n        -email : string\n    }\n    class Aluno {\n        <<Entidade>>\n        -pontos : int\n        -moedas : int\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant V as :Visitante\n    participant C as :ServicoAutenticacao\n    participant A as :Aluno\n    V->>C: registrar(dados)\n    activate C\n    C-->>A: <<create>>\n    activate A\n    A->>A: inicializarPerfil()\n    deactivate A\n    C-->>V: Cadastro Confirmado\n    deactivate C"
    },
    {
        "id": "UC03_Realizar_Teste_Nivelamento",
        "title": "Teste de Nivelamento",
        "desc": "Avaliação diagnóstica para posicionamento do aluno no mapa de conhecimento.",
        "astah_tips": "Dica Astah: Use Agregação (losango vazio) para mostrar que o Simulado agrega questões.",
        "steps_class": [
            "Crie 'Aluno' com o método '+ definirFaseInicial(nota : float)'.",
            "Crie 'Simulado' (<<Entidade>>) com o método '+ iniciarTeste()'.",
            "Ligue-os com uma 'Associação Unidirecional' do Aluno para o Simulado."
        ],
        "steps_seq": [
            "Linhas de Vida: :Aluno e :Simulado.",
            "Mensagem 1: Aluno chama 'iniciarTeste()' no Simulado.",
            "Mensagem de Retorno: Simulado devolve 'listaQuestoes'.",
            "Mensagem 2: Aluno envia 'enviarRespostas()'.",
            "Mensagem 3: Aluno executa nele mesmo 'definirFaseInicial(nota)'."
        ],
        "mermaid_class": "classDiagram\n    class Aluno {\n        <<Entidade>>\n        +definirFaseInicial(nota : float)\n    }\n    class Simulado {\n        <<Entidade>>\n        -nota : float\n        +iniciarTeste()\n    }\n    Aluno --> Simulado : realiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant S as :Simulado\n    A->>S: iniciarTeste()\n    activate S\n    S-->>A: listaQuestoes[]\n    A->>S: enviarRespostas()\n    S-->>A: notaFinal\n    deactivate S\n    A->>A: definirFaseInicial(nota)"
    },
    {
        "id": "UC04_Gerenciar_Perfis_Acessos",
        "title": "Gerenciar Perfis e Acessos",
        "desc": "Administração de papéis e permissões.",
        "astah_tips": "Dica Astah: O GerenciadorAcesso é um <<Controle>>.",
        "steps_class": [
            "Crie 'Admin' e 'Usuario'.",
            "Em 'Usuario', adicione '- papel : string'.",
            "Crie 'GerenciadorAcesso' (<<Controle>>).",
            "Desenhe uma 'Associação' simples de Admin para Usuario."
        ],
        "steps_seq": [
            "O Admin solicita 'alterarPapel()' ao GerenciadorAcesso.",
            "O GerenciadorAcesso chama 'setPapel()' no Usuario alvo.",
            "Retorno de confirmação para o Admin."
        ],
        "mermaid_class": "classDiagram\n    class Admin {\n        +gerenciarAcesso()\n    }\n    class Usuario {\n        <<Entidade>>\n        -papel : string\n    }\n    Admin --> Usuario : administra",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Admin\n    participant M as :GerenciadorAcesso\n    participant U as :Usuario\n    A->>M: alterarPapel(id, papel)\n    activate M\n    M->>U: setPapel(papel)\n    U-->>M: ok\n    M-->>A: Sucesso\n    deactivate M"
    },
    {
        "id": "UC05_Gerenciar_Conteudo_Cartas",
        "title": "Gerenciar Conteúdo e Cartas",
        "desc": "Criação de flashcards e módulos.",
        "astah_tips": "Dica Astah: A Composição no Astah é o ícone do losango preto.",
        "steps_class": [
            "Crie 'Modulo' e 'Flashcard_SM2'.",
            "Ligue com 'Composição' (losango no Módulo).",
            "Atributo em Módulo: '- nome : string'."
        ],
        "steps_seq": [
            "O Tutor solicita 'novoModulo()' ao Sistema.",
            "O Sistema cria (Create) o objeto 'Modulo'.",
            "O Tutor adiciona cartas via 'adicionarCarta()'."
        ],
        "mermaid_class": "classDiagram\n    Modulo *-- Flashcard_SM2\n    class Tutor {\n        +gerenciarConteudo()\n    }\n    class Modulo {\n        <<Entidade>>\n        -nome : string\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant T as :Tutor\n    participant S as :Sistema\n    participant M as :Modulo\n    T->>S: novoModulo(nome)\n    S->>M: <<create>>\n    T->>S: adicionarCarta(p, r)\n    S-->>T: Salvo"
    },
    {
        "id": "UC06_Acompanhar_Desempenho",
        "title": "Acompanhar Desempenho",
        "desc": "Métricas de progresso.",
        "astah_tips": "Dica Astah: PainelVisual deve usar o Estereótipo <<Fronteira>> (Boundary).",
        "steps_class": [
            "Crie 'Tutor', 'Aluno' e 'PainelVisual' (<<Fronteira>>).",
            "Em Aluno: '- progresso : float'.",
            "Ligue Tutor a Aluno via Dependência através do Painel."
        ],
        "steps_seq": [
            "Tutor pede 'visualizar(id)' no PainelVisual.",
            "PainelVisual chama 'obterMetricas()' no objeto :Aluno.",
            "Painel renderiza o relatório final."
        ],
        "mermaid_class": "classDiagram\n    class Tutor {\n        +acompanharDesempenho()\n    }\n    class Aluno {\n        <<Entidade>>\n        -progresso : float\n    }\n    class PainelVisual {\n        <<Fronteira>>\n        +renderizar()\n    }\n    Tutor ..> Aluno : visualiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant T as :Tutor\n    participant D as :PainelVisual\n    participant A as :Aluno\n    T->>D: visualizar(id)\n    activate D\n    D->>A: obterMetricas()\n    A-->>D: dados\n    D-->>T: Relatório Visual\n    deactivate D"
    },
    {
        "id": "UC07_Escalar_Duvida_Tutor",
        "title": "Escalar Dúvida para Tutor",
        "desc": "Transferência IA -> Humano.",
        "astah_tips": "Dica Astah: Agente_IA é um <<Controle>>.",
        "steps_class": [
            "Crie 'Agente_IA' (<<Controle>>) com '+ responderDuvida()'.",
            "Crie 'Tutor' com '+ responderDuvida()'.",
            "Associação simples entre os dois."
        ],
        "steps_seq": [
            "Agente_IA detecta complexidade.",
            "Agente_IA envia 'escalar(duvida)' para :Tutor.",
            "Tutor responde ao Aluno."
        ],
        "mermaid_class": "classDiagram\n    class Agente_IA {\n        <<Controle>>\n        +responderDuvida(duvida)\n    }\n    class Tutor {\n        <<Entidade>>\n        +responderDuvida()\n    }\n    Agente_IA --> Tutor : notifica",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant IA as :Agente_IA\n    participant T as :Tutor\n    participant Al as :Aluno\n    IA->>IA: detectarComplexidade()\n    IA->>T: escalar(duvida, id)\n    T-->>Al: Resposta"
    },
    {
        "id": "UC08_Consultar_Agente_IA",
        "title": "Consultar Agente IA",
        "desc": "Interação instantânea.",
        "astah_tips": "Dica Astah: Represente Duvida como <<Entidade>>.",
        "steps_class": [
            "Crie 'Agente_IA' com '+ responderDuvida()'.",
            "Crie 'Duvida' com '- descricao : string'.",
            "Dependência da IA para Duvida."
        ],
        "steps_seq": [
            "Aluno envia dúvida para :Agente_IA.",
            "Agente_IA processa linguagem natural.",
            "Agente_IA retorna resposta ao Aluno."
        ],
        "mermaid_class": "classDiagram\n    class Agente_IA {\n        <<Controle>>\n        +responderDuvida(duvida)\n    }\n    class Duvida {\n        <<Entidade>>\n        -descricao : string\n    }\n    Agente_IA ..> Duvida : consulta",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant IA as :Agente_IA\n    A->>IA: enviarDuvida(texto)\n    IA->>IA: processarLinguagem()\n    IA-->>A: Resposta"
    },
    {
        "id": "UC09_Estudar_Flashcards",
        "title": "Estudar Flashcards (SM-2)",
        "desc": "Repetição espaçada.",
        "astah_tips": "Dica Astah: No Astah, use 'Self-Message' para o algoritmo SM-2.",
        "steps_class": [
            "Crie 'MotorSM2' (<<Controle>>) e 'Flashcard_SM2'.",
            "Atributos no Flashcard: '- dataProximaRevisao : date'.",
            "Associação do Motor para o Flashcard."
        ],
        "steps_seq": [
            "Aluno lê pergunta.",
            "Aluno informa dificuldade (1-5) ao :MotorSM2.",
            "Motor aplica algoritmo e atualiza data no Flashcard_SM2."
        ],
        "mermaid_class": "classDiagram\n    class MotorSM2 {\n        <<Controle>>\n        +aplicarSM2(feedback)\n    }\n    class Flashcard_SM2 {\n        <<Entidade>>\n        -dataProximaRevisao : date\n    }\n    MotorSM2 --> Flashcard_SM2 : atualiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant M as :MotorSM2\n    participant F as :Flashcard_SM2\n    A->>F: lerPergunta()\n    A->>M: informarDificuldade(1-5)\n    M->>M: aplicarSM2()\n    M->>F: setDataProximaRevisao(data)\n    F-->>A: Ok"
    },
    {
        "id": "UC10_Criar_Flashcards",
        "title": "Criar Flashcards",
        "desc": "Personalização de deck.",
        "astah_tips": "Dica Astah: Editor é uma classe de <<Fronteira>>.",
        "steps_class": [
            "Crie 'Aluno' e 'Flashcard_SM2'.",
            "Método em Aluno: '+ criarCarta()'.",
            "Associação 1..*."
        ],
        "steps_seq": [
            "Aluno usa :Editor para digitar dados.",
            "Editor envia dados para criar :Flashcard_SM2.",
            "Confirmação de salvamento."
        ],
        "mermaid_class": "classDiagram\n    class Aluno {\n        <<Entidade>>\n        +criarCarta()\n    }\n    class Flashcard_SM2 {\n        <<Entidade>>\n        -pergunta : string\n        -resposta : string\n    }\n    Aluno \"1\" --> \"*\" Flashcard_SM2 : cria",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant E as :Editor\n    participant F as :Flashcard_SM2\n    A->>E: entrada(p, r)\n    E->>F: <<create>>(p, r)\n    F-->>A: Sucesso"
    },
    {
        "id": "UC11_Realizar_Simulado_ENADE",
        "title": "Realizar Simulado ENADE",
        "desc": "Treinamento intensivo.",
        "astah_tips": "Dica Astah: Questao é uma <<Entidade>>.",
        "steps_class": [
            "Crie 'Simulado' and 'Questao'.",
            "Composição (losango preto).",
            "Simulado: '- tempoRestante : int'."
        ],
        "steps_seq": [
            "Aluno inicia Simulado.",
            "Simulado liga o :Temporizador.",
            "Após responder tudo, Simulado desliga e dá a nota."
        ],
        "mermaid_class": "classDiagram\n    class Simulado {\n        <<Entidade>>\n        -tempoRestante : int\n        +iniciarTeste()\n    }\n    class Questao {\n        <<Entidade>>\n        -texto : string\n    }\n    Simulado \"1\" *-- \"*\" Questao",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant S as :Simulado\n    participant T as :Temporizador\n    A->>S: iniciarTeste()\n    S->>T: iniciar()\n    A->>S: responder()\n    S-->>A: Nota Final"
    },
    {
        "id": "UC12_Atribuir_XP_Moedas",
        "title": "Atribuir XP e Moedas",
        "desc": "Motor de recompensas.",
        "astah_tips": "Dica Astah: Gamificacao é um <<Controle>>.",
        "steps_class": [
            "Crie 'Gamificacao' (<<Controle>>) e 'Aluno'.",
            "Aluno: '- pontos : int', '- moedas : int'.",
            "Dependência de Gamificação para Aluno."
        ],
        "steps_seq": [
            "Sistema notifica :Gamificacao.",
            "Gamificação calcula bônus.",
            "Gamificação chama 'creditarXP()' no Aluno."
        ],
        "mermaid_class": "classDiagram\n    class Gamificacao {\n        <<Controle>>\n        +calcularBonus()\n    }\n    class Aluno {\n        <<Entidade>>\n        -pontos : int\n        -moedas : int\n    }\n    Gamificacao ..> Aluno : credita",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant S as :Sistema\n    participant G as :Gamificacao\n    participant A as :Aluno\n    S->>G: concluirTarefa()\n    G->>G: calcular()\n    G->>A: creditarXP(100)\n    G-->>S: Ok"
    },
    {
        "id": "UC13_Desbloquear_Fases_Modulos",
        "title": "Desbloquear Fases e Módulos",
        "desc": "Progressão condicionada.",
        "astah_tips": "Dica Astah: Use Dependência para mostrar verificação de progresso.",
        "steps_class": [
            "Crie 'Fase' com '- bloqueada : bool'.",
            "Crie 'GerenciadorProgresso' (<<Controle>>).",
            "Dependência do Gerenciador para Aluno e Fase."
        ],
        "steps_seq": [
            "Gerenciador pede progresso ao Aluno.",
            "Se ok, chama 'desbloquear()' na :Fase.",
            "Fase muda estado para liberada."
        ],
        "mermaid_class": "classDiagram\n    class Fase {\n        <<Entidade>>\n        -bloqueada : bool\n        +desbloquear()\n    }\n    class Aluno {\n        <<Entidade>>\n        -progresso : float\n    }\n    Fase ..> Aluno : verifica",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant M as :GerenciadorProgresso\n    participant A as :Aluno\n    participant F as :Fase\n    M->>A: obterProgresso()\n    M->>F: desbloquear()\n    F-->>M: Sucesso"
    },
    {
        "id": "UC14_Visualizar_Painel_Progresso",
        "title": "Visualizar Painel de Progresso",
        "desc": "Hub central.",
        "astah_tips": "Dica Astah: PainelVisual é uma <<Fronteira>>.",
        "steps_class": [
            "Crie 'PainelVisual' (<<Fronteira>>) e 'Aluno'.",
            "PainelVisual: '+ renderizar()'.",
            "Dependência para leitura de dados."
        ],
        "steps_seq": [
            "Aluno abre início.",
            "Painel pede dados de progresso ao Aluno.",
            "Painel exibe informações."
        ],
        "mermaid_class": "classDiagram\n    class PainelVisual {\n        <<Fronteira>>\n        +renderizar()\n    }\n    class Aluno {\n        <<Entidade>>\n        +obterProgresso()\n    }\n    PainelVisual ..> Aluno : lê",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant Al as :Aluno\n    participant D as :PainelVisual\n    Al->>D: abrirHome()\n    D->>D: renderizar()\n    D-->>Al: Ok"
    },
    {
        "id": "UC15_Ajustar_Acessibilidade",
        "title": "Ajustar Acessibilidade",
        "desc": "Personalização.",
        "astah_tips": "Dica Astah: Acessibilidade é uma <<Entidade>>.",
        "steps_class": [
            "Crie 'Acessibilidade' com '- altoContraste : bool' e '- tamanhoFonte : int'.",
            "Método: '+ salvar()'."
        ],
        "steps_seq": [
            "Usuario interage com :PainelConfiguracao.",
            "Painel envia 'salvar()' para :Acessibilidade.",
            "Interface atualiza."
        ],
        "mermaid_class": "classDiagram\n    class Acessibilidade {\n        <<Entidade>>\n        -altoContraste : bool\n        -tamanhoFonte : int\n        +salvar()\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant U as :Usuario\n    participant P as :PainelConfiguracao\n    participant A as :Acessibilidade\n    U->>P: selecionarOpcao()\n    P->>A: salvar()\n    A-->>P: ok"
    }
]

# Caminhos dinâmicos baseados no diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.abspath(os.path.join(script_dir, "..", "02_Modelagem_UML_Astah"))
dashboard_path = os.path.abspath(os.path.join(script_dir, "..", "01_Relatorios_e_Dashboard", "DASHBOARD_VISUAL.md"))

# 1. Gerar os READMEs individuais (Nível de Fidelidade Astah)
for uc in use_cases:
    folder_path = os.path.join(base_path, uc["id"])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, "README.md")
    
    content = f"# 📘 Guia de Modelagem Astah (Fiel à v10.x): {uc['title']}\n\n"
    content += f"## 🎯 Objetivo\n{uc['desc']}\n\n"
    content += f"> [!IMPORTANT]\n> {uc['astah_tips']}\n\n"
    
    content += "## 🚀 Tutorial Passo a Passo Detalhado (Interface Astah)\n\n"
    
    content += "### 1️⃣ Diagrama de Classe (Estrutura)\n"
    for i, step in enumerate(uc["steps_class"], 1):
        content += f"   - [ ] {i}. **{step}**\n"
    content += "\n**Como configurar no Astah:** Para adicionar o Estereótipo (ex: <<Entidade>>), selecione a classe, vá na aba **Stereotype** (na base da tela) e clique em **Add**.\n\n"
    
    content += "### 2️⃣ Diagrama de Sequência (Processo)\n"
    for i, step in enumerate(uc["steps_seq"], 1):
        content += f"   - [ ] {i}. **{step}**\n"
    content += "\n**Dica de Notação:** Note que os nomes das Linhas de Vida agora começam com dois pontos (ex: `:Controlador`), indicando que são instâncias anônimas da classe.\n\n"
    
    content += "---\n\n"
    content += "## 📊 Referência Visual (Estilo Astah UML)\n"
    content += "### Diagrama de Classe\n"
    content += f"```mermaid\n{uc['mermaid_class']}\n```\n\n"
    content += "### Diagrama de Sequência\n"
    content += f"```mermaid\n{uc['mermaid_seq']}\n```\n\n"
    content += "---\n*Este manual foi otimizado para a versão 10.1.0 do Astah UML.*"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Gerar o Dashboard
db_content = "# 🚀 Painel de Modelagem (Padrão Astah 10.x)\n\n"
db_content += "Este documento centraliza os diagramas em conformidade com a interface e notação do Astah UML.\n\n"
db_content += "## 📑 Índice de Casos de Uso\n"
for uc in use_cases:
    db_content += f"- [{uc['title']}](#{uc['id'].lower().replace('_', '-')})\n"

db_content += "\n---\n\n## 🏛️ Visão Global do Sistema Nex_TI\n"
db_content += "Esta seção apresenta a arquitetura holística do sistema, unificando todos os 15 Casos de Uso em uma visão coerente e profissional.\n\n"
db_content += "### 1. Diagrama de Casos de Uso Global (Mapa Geral)\n"
db_content += "Representa a fronteira do sistema, os atores envolvidos e a distribuição dos módulos.\n"
db_content += "![Diagrama_Casos_Uso_Global](../03_Artefatos_Gerados/Diagrama_Casos_Uso_Global.png)\n\n"
db_content += "### 2. Diagrama de Classes Global (Estrutura de Dados)\n"
db_content += "Unifica todas as entidades e controladores, servindo como a arquitetura de referência do sistema.\n"
db_content += "![Diagrama_Classes_Global](../03_Artefatos_Gerados/Diagrama_Classes_Global.png)\n\n"
db_content += "### 3. Diagrama de Sequência Global (Fluxo Arquitetural)\n"
db_content += "Ilustra o ciclo de vida de uma requisição típica, desde a interface até a persistência de dados.\n"
db_content += "![Diagrama_Sequencia_Global](../03_Artefatos_Gerados/Diagrama_Sequencia_Global.png)\n"

for uc in use_cases:
    db_content += f"\n---\n\n## {uc['id']} - {uc['title']}\n"
    db_content += f"**Objetivo:** {uc['desc']}\n\n"
    db_content += "### 📐 Diagramas Féis ao Astah\n"
    db_content += "#### Diagrama de Classe\n"
    db_content += f"```mermaid\n{uc['mermaid_class']}\n```\n"
    db_content += "#### Diagrama de Sequência\n"
    db_content += f"```mermaid\n{uc['mermaid_seq']}\n```\n"
    db_content += f"\n[👉 Abrir Manual de Modelagem Fiel](../02_Modelagem_UML_Astah/{uc['id']}/README.md)\n"

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(db_content)

print("Ajuste de fidelidade Astah 10.1 concluído com sucesso e caminhos dinâmicos gerados.")
