import os

use_cases = [
    {
        "id": "UC01_Realizar_Login",
        "title": "Realizar Login",
        "desc": "Acesso seguro do usuário ao sistema através de validação de credenciais.",
        "astah_tips": "Dica Astah: Utilize 'Activation Bars' para mostrar o processamento no Controlador.",
        "steps_class": [
            "Crie a classe 'MD_Usuarios' e aplique o Estereótipo <<Entidade>>.",
            "Adicione os atributos: '+ email : string' e '+ senha : string'.",
            "Crie a classe 'ControladorAutenticacao' e aplique o Estereótipo <<Controle>>.",
            "Adicione o método: '+ autenticar(email : string, senha : string) : bool'.",
            "Desenhe uma seta de 'Dependência' (tracejada) saindo do Controlador para a Entidade."
        ],
        "steps_seq": [
            "Adicione o Ator 'Usuario' e a Linha de Vida ':ControladorAutenticacao'.",
            "Mensagem 1: Usuario envia 'login(email, senha)' para o Controlador.",
            "Mensagem 1.1: O Controlador executa nele mesmo 'validarCredenciais()'.",
            "Mensagem de Retorno: Seta tracejada voltando para o Usuario com o Resultado."
        ],
        "mermaid_class": "classDiagram\n    class MD_Usuarios {\n        <<Entidade>>\n        +email : string\n        +senha : string\n    }\n    class ControladorAutenticacao {\n        <<Controle>>\n        +autenticar(email : string, senha : string) : bool\n    }\n    ControladorAutenticacao ..> MD_Usuarios : consulta",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant U as Usuário (Ator)\n    participant C as :ControladorAutenticacao\n    U->>C: login(email, senha)\n    activate C\n    C->>C: validarCredenciais()\n    C-->>U: Resultado (Sucesso/Erro)\n    deactivate C"
    },
    {
        "id": "UC02_Cadastrar_Usuario",
        "title": "Cadastrar Usuário",
        "desc": "Registro de novos alunos com inicialização automática de perfil de gamificação.",
        "astah_tips": "Dica Astah: A seta de Herança (Generalização) é a que possui o triângulo na ponta.",
        "steps_class": [
            "Crie a classe base 'MD_Usuarios' com 'nome : string' e 'email : string'.",
            "Crie a classe 'MD_Alunos' (Estereótipo <<Entidade>>).",
            "Desenhe a 'Generalização' (Herança) de MD_Alunos apontando para MD_Usuarios.",
            "Adicione em MD_Alunos os atributos: '+ pontos : int' e '+ moedas : int'."
        ],
        "steps_seq": [
            "Linhas de Vida: :Visitante, :ControladorAutenticacao e :MD_Alunos.",
            "Mensagem 1: Visitante solicita 'registrar(dados)'.",
            "Mensagem 2: O Controlador cria o objeto 'MD_Alunos' usando a seta de 'Create Message'.",
            "Mensagem 3: O objeto recém-criado executa internamente 'inicializarPerfil()'."
        ],
        "mermaid_class": "classDiagram\n    MD_Usuarios <|-- MD_Alunos\n    class MD_Usuarios {\n        +nome : string\n        +email : string\n    }\n    class MD_Alunos {\n        <<Entidade>>\n        +pontos : int\n        +moedas : int\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant V as :Visitante\n    participant C as :ControladorAutenticacao\n    participant A as :MD_Alunos\n    V->>C: registrar(dados)\n    activate C\n    C-->>A: <<create>>\n    activate A\n    A->>A: inicializarPerfil()\n    deactivate A\n    C-->>V: Cadastro Confirmado\n    deactivate C"
    },
    {
        "id": "UC03_Realizar_Teste_Nivelamento",
        "title": "Teste de Nivelamento",
        "desc": "Avaliação diagnóstica para posicionamento do aluno no mapa de conhecimento.",
        "astah_tips": "Dica Astah: Use Agregação (losango vazio) para mostrar que o Simulado agrega questões.",
        "steps_class": [
            "Crie 'MD_Alunos' com o método '+ definirFaseInicial(nota : float)'.",
            "Crie 'MD_Simulado' (<<Entidade>>) com o método '+ iniciarTeste()'.",
            "Ligue-os com uma 'Associação Unidirecional' do Aluno para o Simulado."
        ],
        "steps_seq": [
            "Linhas de Vida: :Aluno e :MD_Simulado.",
            "Mensagem 1: Aluno chama 'iniciarTeste()' no Simulado.",
            "Mensagem de Retorno: Simulado devolve 'listaQuestoes'.",
            "Mensagem 2: Aluno envia 'enviarRespostas()'.",
            "Mensagem 3: Aluno executa nele mesmo 'definirFaseInicial(nota)'."
        ],
        "mermaid_class": "classDiagram\n    class MD_Alunos {\n        <<Entidade>>\n        +definirFaseInicial(nota : float)\n    }\n    class MD_Simulado {\n        <<Entidade>>\n        +nota : float\n        +iniciarTeste()\n    }\n    MD_Alunos --> MD_Simulado : realiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant S as :MD_Simulado\n    A->>S: iniciarTeste()\n    activate S\n    S-->>A: listaQuestoes[]\n    A->>S: enviarRespostas()\n    S-->>A: notaFinal\n    deactivate S\n    A->>A: definirFaseInicial(nota)"
    },
    {
        "id": "UC04_Gerenciar_Perfis_Acessos",
        "title": "Gerenciar Perfis e Acessos",
        "desc": "Administração de papéis e permissões.",
        "astah_tips": "Dica Astah: O GerenciadorAcesso é um <<Controle>>.",
        "steps_class": [
            "Crie 'MD_Admin' e 'MD_Usuarios'.",
            "Em 'MD_Usuarios', adicione '+ papel : string'.",
            "Crie 'GerenciadorAcesso' (<<Controle>>).",
            "Desenhe uma 'Associação' simples de Admin para Usuarios."
        ],
        "steps_seq": [
            "O Admin solicita 'alterarPapel()' ao GerenciadorAcesso.",
            "O GerenciadorAcesso chama 'setPapel()' no MD_Usuarios alvo.",
            "Retorno de confirmação para o Admin."
        ],
        "mermaid_class": "classDiagram\n    class MD_Admin {\n        +gerenciarAcesso()\n    }\n    class MD_Usuarios {\n        <<Entidade>>\n        +papel : string\n    }\n    MD_Admin --> MD_Usuarios : administra",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Admin\n    participant M as :GerenciadorAcesso\n    participant U as :MD_Usuarios\n    A->>M: alterarPapel(id, papel)\n    activate M\n    M->>U: setPapel(papel)\n    U-->>M: ok\n    M-->>A: Sucesso\n    deactivate M"
    },
    {
        "id": "UC05_Gerenciar_Conteudo_Cartas",
        "title": "Gerenciar Conteúdo e Cartas",
        "desc": "Criação de flashcards e módulos.",
        "astah_tips": "Dica Astah: A Composição no Astah é o ícone do losango preto.",
        "steps_class": [
            "Crie 'MD_Modulos' e 'MD_Flashcards'.",
            "Ligue com 'Composição' (losango no Módulo).",
            "Atributo em Módulo: '+ nomeModulo : string'."
        ],
        "steps_seq": [
            "O Tutor solicita 'novoModulo()' ao Sistema.",
            "O Sistema cria (Create) o objeto 'MD_Modulos'.",
            "O Tutor adiciona cartas via 'adicionarCarta()'."
        ],
        "mermaid_class": "classDiagram\n    MD_Modulos *-- MD_Flashcards\n    class MD_Tutor {\n        +gerenciarConteudo()\n    }\n    class MD_Modulos {\n        <<Entidade>>\n        +nomeModulo : string\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant T as :Tutor\n    participant S as :Sistema\n    participant M as :MD_Modulos\n    T->>S: novoModulo(nome)\n    S->>M: <<create>>\n    T->>S: adicionarCarta(p, r)\n    S-->>T: Salvo"
    },
    {
        "id": "UC06_Acompanhar_Desempenho",
        "title": "Acompanhar Desempenho",
        "desc": "Métricas de progresso.",
        "astah_tips": "Dica Astah: PainelVisual deve usar o Estereótipo <<Fronteira>> (Boundary).",
        "steps_class": [
            "Crie 'MD_Tutor', 'MD_Alunos' e 'PainelVisual' (<<Fronteira>>).",
            "Em Alunos: '+ progresso : float'.",
            "Ligue Tutor a Aluno via Dependência através do Painel."
        ],
        "steps_seq": [
            "Tutor pede 'visualizar(id)' no PainelVisual.",
            "PainelVisual chama 'obterMetricas()' no objeto :MD_Alunos.",
            "Painel renderiza o relatório final."
        ],
        "mermaid_class": "classDiagram\n    class MD_Tutor {\n        +acompanharDesempenho()\n    }\n    class MD_Alunos {\n        <<Entidade>>\n        +progresso : float\n    }\n    class PainelVisual {\n        <<Fronteira>>\n        +renderizar()\n    }\n    MD_Tutor ..> MD_Alunos : visualiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant T as :Tutor\n    participant D as :PainelVisual\n    participant A as :MD_Alunos\n    T->>D: visualizar(id)\n    activate D\n    D->>A: obterMetricas()\n    A-->>D: dados\n    D-->>T: Relatório Visual\n    deactivate D"
    },
    {
        "id": "UC07_Escalar_Duvida_Tutor",
        "title": "Escalar Dúvida para Tutor",
        "desc": "Transferência IA -> Humano.",
        "astah_tips": "Dica Astah: AgenteIA é um <<Controle>>.",
        "steps_class": [
            "Crie 'AgenteIA' (<<Controle>>) com '+ analisar()' e '+ escalar()'.",
            "Crie 'MD_Tutor' com '+ responderDuvida()'.",
            "Associação simples entre os dois."
        ],
        "steps_seq": [
            "AgenteIA detecta complexidade.",
            "AgenteIA envia 'escalar(duvida)' para :MD_Tutor.",
            "Tutor responde ao Aluno."
        ],
        "mermaid_class": "classDiagram\n    class AgenteIA {\n        <<Controle>>\n        +analisar()\n        +escalar(duvida)\n    }\n    class MD_Tutor {\n        <<Entidade>>\n        +responderDuvida()\n    }\n    AgenteIA --> MD_Tutor : notifica",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant IA as :AgenteIA\n    participant T as :MD_Tutor\n    participant Al as :Aluno\n    IA->>IA: detectarComplexidade()\n    IA->>T: escalar(duvida, id)\n    T-->>Al: Resposta"
    },
    {
        "id": "UC08_Consultar_Agente_IA",
        "title": "Consultar Agente IA",
        "desc": "Interação instantânea.",
        "astah_tips": "Dica Astah: Represente MD_Duvidas como <<Entidade>>.",
        "steps_class": [
            "Crie 'AgenteIA' com '+ responder()'.",
            "Crie 'MD_Duvidas' com '+ pergunta : string' e '+ resposta : string'.",
            "Dependência da IA para MD_Duvidas."
        ],
        "steps_seq": [
            "Aluno envia dúvida para :AgenteIA.",
            "AgenteIA processa linguagem natural.",
            "AgenteIA retorna resposta ao Aluno."
        ],
        "mermaid_class": "classDiagram\n    class AgenteIA {\n        <<Controle>>\n        +responder(pergunta)\n    }\n    class MD_Duvidas {\n        <<Entidade>>\n        +pergunta : string\n        +resposta : string\n    }\n    AgenteIA ..> MD_Duvidas : consulta",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant IA as :AgenteIA\n    A->>IA: enviarDuvida(texto)\n    IA->>IA: processarLinguagem()\n    IA-->>A: Resposta"
    },
    {
        "id": "UC09_Estudar_Flashcards",
        "title": "Estudar Flashcards (SM-2)",
        "desc": "Repetição espaçada.",
        "astah_tips": "Dica Astah: No Astah, use 'Self-Message' para o algoritmo SM-2.",
        "steps_class": [
            "Crie 'MD_MotorSM2' (<<Controle>>) e 'MD_Flashcards'.",
            "Atributos no Flashcard: '+ proximaRevisao : date'.",
            "Associação do Motor para o Flashcard."
        ],
        "steps_seq": [
            "Aluno lê pergunta.",
            "Aluno informa dificuldade (1-5) ao :MD_MotorSM2.",
            "Motor aplica algoritmo e atualiza data no Flashcard."
        ],
        "mermaid_class": "classDiagram\n    class MD_MotorSM2 {\n        <<Controle>>\n        +aplicarSM2(feedback)\n    }\n    class MD_Flashcards {\n        <<Entidade>>\n        +proximaRevisao : date\n    }\n    MD_MotorSM2 --> MD_Flashcards : atualiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant M as :MD_MotorSM2\n    participant F as :MD_Flashcards\n    A->>F: lerPergunta()\n    A->>M: informarDificuldade(1-5)\n    M->>M: aplicarSM2()\n    M->>F: setProximaRevisao(data)\n    F-->>A: Ok"
    },
    {
        "id": "UC10_Criar_Flashcards",
        "title": "Criar Flashcards",
        "desc": "Personalização de deck.",
        "astah_tips": "Dica Astah: Editor é uma classe de <<Fronteira>>.",
        "steps_class": [
            "Crie 'MD_Alunos' e 'MD_Flashcards'.",
            "Método em Aluno: '+ criarCarta()'.",
            "Associação 1..*."
        ],
        "steps_seq": [
            "Aluno usa :Editor para digitar dados.",
            "Editor envia dados para criar :MD_Flashcards.",
            "Confirmação de salvamento."
        ],
        "mermaid_class": "classDiagram\n    class MD_Alunos {\n        <<Entidade>>\n        +criarCarta()\n    }\n    class MD_Flashcards {\n        <<Entidade>>\n        +pergunta : string\n        +resposta : string\n    }\n    MD_Alunos \"1\" --> \"*\" MD_Flashcards : cria",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant E as :Editor\n    participant F as :MD_Flashcards\n    A->>E: entrada(p, r)\n    E->>F: <<create>>(p, r)\n    F-->>A: Sucesso"
    },
    {
        "id": "UC11_Realizar_Simulado_ENADE",
        "title": "Realizar Simulado ENADE",
        "desc": "Treinamento intensivo.",
        "astah_tips": "Dica Astah: Questao é uma <<Entidade>>.",
        "steps_class": [
            "Crie 'MD_Simulado' e 'Questao'.",
            "Composição (losango preto).",
            "Simulado: '+ tempoRestante : int'."
        ],
        "steps_seq": [
            "Aluno inicia Simulado.",
            "Simulado liga o :Temporizador.",
            "Após responder tudo, Simulado desliga e dá a nota."
        ],
        "mermaid_class": "classDiagram\n    class MD_Simulado {\n        <<Entidade>>\n        +tempoRestante : int\n        +iniciarTeste()\n    }\n    class Questao {\n        <<Entidade>>\n        +texto : string\n    }\n    MD_Simulado \"1\" *-- \"*\" Questao",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as :Aluno\n    participant S as :MD_Simulado\n    participant T as :Temporizador\n    A->>S: iniciarTeste()\n    S->>T: iniciar()\n    A->>S: responder()\n    S-->>A: Nota Final"
    },
    {
        "id": "UC12_Atribuir_XP_Moedas",
        "title": "Atribuir XP e Moedas",
        "desc": "Motor de recompensas.",
        "astah_tips": "Dica Astah: Gamificacao é um <<Controle>>.",
        "steps_class": [
            "Crie 'MD_Gamificacao' (<<Controle>>) e 'MD_Alunos'.",
            "Alunos: '+ pontos : int', '+ moedas : int'.",
            "Dependência de Gamificação para Alunos."
        ],
        "steps_seq": [
            "Sistema notifica :MD_Gamificacao.",
            "Gamificação calcula bônus.",
            "Gamificação chama 'creditarXP()' no Aluno."
        ],
        "mermaid_class": "classDiagram\n    class MD_Gamificacao {\n        <<Controle>>\n        +calcularBonus()\n    }\n    class MD_Alunos {\n        <<Entidade>>\n        +pontos : int\n        +moedas : int\n    }\n    MD_Gamificacao ..> MD_Alunos : credita",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant S as :Sistema\n    participant G as :MD_Gamificacao\n    participant A as :MD_Alunos\n    S->>G: concluirTarefa()\n    G->>G: calcular()\n    G->>A: creditarXP(100)\n    G-->>S: Ok"
    },
    {
        "id": "UC13_Desbloquear_Fases_Modulos",
        "title": "Desbloquear Fases e Módulos",
        "desc": "Progressão condicionada.",
        "astah_tips": "Dica Astah: Use Dependência para mostrar verificação de progresso.",
        "steps_class": [
            "Crie 'MD_Fases' com '+ bloqueada : bool'.",
            "Crie 'GerenciadorProgresso' (<<Controle>>).",
            "Dependência do Gerenciador para Alunos e Fases."
        ],
        "steps_seq": [
            "Gerenciador pede progresso ao Aluno.",
            "Se ok, chama 'desbloquear()' na :MD_Fases.",
            "Fase muda estado para liberada."
        ],
        "mermaid_class": "classDiagram\n    class MD_Fases {\n        <<Entidade>>\n        +bloqueada : bool\n        +desbloquear()\n    }\n    class MD_Alunos {\n        <<Entidade>>\n        +progresso : float\n    }\n    MD_Fases ..> MD_Alunos : verifica",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant M as :GerenciadorProgresso\n    participant A as :MD_Alunos\n    participant F as :MD_Fases\n    M->>A: obterProgresso()\n    M->>F: desbloquear()\n    F-->>M: Sucesso"
    },
    {
        "id": "UC14_Visualizar_Painel_Progresso",
        "title": "Visualizar Painel de Progresso",
        "desc": "Hub central.",
        "astah_tips": "Dica Astah: PainelVisual é uma <<Fronteira>>.",
        "steps_class": [
            "Crie 'PainelVisual' (<<Fronteira>>) e 'MD_Alunos'.",
            "PainelVisual: '+ renderizar()'.",
            "Dependência para leitura de dados."
        ],
        "steps_seq": [
            "Aluno abre início.",
            "Painel pede dados de progresso ao Aluno.",
            "Painel exibe informações."
        ],
        "mermaid_class": "classDiagram\n    class PainelVisual {\n        <<Fronteira>>\n        +renderizar()\n    }\n    class MD_Alunos {\n        <<Entidade>>\n        +obterProgresso()\n    }\n    PainelVisual ..> MD_Alunos : lê",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant Al as :Aluno\n    participant D as :PainelVisual\n    Al->>D: abrirHome()\n    D->>D: renderizar()\n    D-->>Al: Ok"
    },
    {
        "id": "UC15_Ajustar_Acessibilidade",
        "title": "Ajustar Acessibilidade",
        "desc": "Personalização.",
        "astah_tips": "Dica Astah: MD_Acessibilidade é uma <<Entidade>>.",
        "steps_class": [
            "Crie 'MD_Acessibilidade' com '+ altoContraste : bool' e '+ tamanhoFonte : int'.",
            "Método: '+ salvar()'."
        ],
        "steps_seq": [
            "Usuario interage com :PainelConfiguracao.",
            "Painel envia 'salvar()' para :MD_Acessibilidade.",
            "Interface atualiza."
        ],
        "mermaid_class": "classDiagram\n    class MD_Acessibilidade {\n        <<Entidade>>\n        +altoContraste : bool\n        +tamanhoFonte : int\n        +salvar()\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant U as :Usuario\n    participant P as :PainelConfiguracao\n    participant A as :MD_Acessibilidade\n    U->>P: selecionarOpcao()\n    P->>A: salvar()\n    A-->>P: ok"
    }
]

# Caminhos organizados
base_path = "c:/Users/mayco/Documents/GitHub/Documentacao_UML/PIM_III/02_Modelagem_UML_Astah"
dashboard_path = "c:/Users/mayco/Documents/GitHub/Documentacao_UML/PIM_III/01_Gestao_e_Planejamento/DASHBOARD_VISUAL.md"

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

print("Ajuste de fidelidade Astah 10.1 concluído.")
