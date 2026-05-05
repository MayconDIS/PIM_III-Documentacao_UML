import os

use_cases = [
    {
        "id": "UC01_Realizar_Login",
        "title": "Realizar Login",
        "desc": "Acesso seguro do usuário ao sistema através de validação de credenciais.",
        "astah_tips": "Dica Astah: No Diagrama de Sequência, utilize 'Barras de Ativação' para mostrar o tempo de vida do processamento no Controlador.",
        "steps_class": ["Classe MD_Usuarios (Entidade)", "Classe ControladorAutenticacao (Controle)", "Atributos: email: texto, senha: hash", "Método: autenticar()"],
        "steps_seq": ["Usuario -> ControladorAutenticacao: login()", "ControladorAutenticacao -> ControladorAutenticacao: validarCredenciais()", "Retorno: Token de Acesso ou Erro"],
        "mermaid_class": "classDiagram\n    class MD_Usuarios {\n        +string email\n        +string senha\n    }\n    class ControladorAutenticacao {\n        +autenticar(email, senha)\n    }\n    ControladorAutenticacao ..> MD_Usuarios : consulta",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant U as Usuario\n    participant C as ControladorAutenticacao\n    U->>C: login(email, senha)\n    activate C\n    C->>C: validarCredenciais()\n    C-->>U: Retorno (Sucesso/Erro)\n    deactivate C"
    },
    {
        "id": "UC02_Cadastrar_Usuario",
        "title": "Cadastrar Usuário",
        "desc": "Registro de novos alunos com inicialização automática de perfil de gamificação.",
        "astah_tips": "Dica Astah: Use a 'Generalização' (seta fechada) de MD_Alunos para MD_Usuarios para indicar herança.",
        "steps_class": ["MD_Usuarios (Base)", "MD_Alunos (Extensão)", "Herança: MD_Alunos herda de MD_Usuarios", "Atributos: pontos: int, moedas: int"],
        "steps_seq": ["Visitante -> ControladorAutenticacao: registrar()", "ControladorAutenticacao -> MD_Alunos: <<create>>", "MD_Alunos -> MD_Alunos: inicializarPerfil()"],
        "mermaid_class": "classDiagram\n    MD_Usuarios <|-- MD_Alunos\n    class MD_Usuarios {\n        +string nome\n        +string email\n    }\n    class MD_Alunos {\n        +int pontos\n        +int moedas\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant V as Visitante\n    participant C as ControladorAutenticacao\n    participant A as MD_Alunos\n    V->>C: registrar(dados)\n    activate C\n    C-->>A: <<create>>\n    activate A\n    A->>A: inicializarPerfil()\n    deactivate A\n    C-->>V: Cadastro Confirmado\n    deactivate C"
    },
    {
        "id": "UC03_Realizar_Teste_Nivelamento",
        "title": "Teste de Nivelamento",
        "desc": "Avaliação diagnóstica para posicionamento do aluno no mapa de conhecimento.",
        "astah_tips": "Dica Astah: No diagrama de classe, use 'Agregação' para mostrar que um Simulado contém questões.",
        "steps_class": ["MD_Alunos", "MD_Simulado", "Método: definirFaseInicial(nota)", "Atributo: complexidade: texto"],
        "steps_seq": ["Aluno -> MD_Simulado: iniciarTeste()", "MD_Simulado -->> Aluno: listaQuestoes[]", "Aluno -> MD_Simulado: enviarRespostas()", "Aluno -> Aluno: definirFaseInicial(nota)"],
        "mermaid_class": "classDiagram\n    class MD_Alunos {\n        +definirFaseInicial(nota)\n    }\n    class MD_Simulado {\n        +float nota\n        +iniciarTeste()\n    }\n    MD_Alunos --> MD_Simulado : realiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant S as MD_Simulado\n    A->>S: iniciarTeste()\n    activate S\n    S-->>A: Lista de Questões\n    A->>S: enviarRespostas()\n    S-->>A: notaFinal\n    deactivate S\n    A->>A: definirFaseInicial(nota)"
    },
    {
        "id": "UC04_Gerenciar_Perfis_Acessos",
        "title": "Gerenciar Perfis e Acessos",
        "desc": "Administração de papéis (Admin, Tutor, Aluno) e permissões de sistema.",
        "astah_tips": "Dica Astah: Use 'Notas' para descrever os tipos de 'papéis' (roles) suportados no sistema.",
        "steps_class": ["MD_Admin", "MD_Usuarios", "GerenciadorAcesso (Controle)", "Atributo: papel: texto"],
        "steps_seq": ["Admin -> GerenciadorAcesso: alterarPapel()", "GerenciadorAcesso -> MD_Usuarios: setPapel()", "Retorno: Confirmação"],
        "mermaid_class": "classDiagram\n    class MD_Admin {\n        +gerenciarAcesso()\n    }\n    class MD_Usuarios {\n        +string papel\n    }\n    MD_Admin --> MD_Usuarios : administra",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Admin\n    participant M as GerenciadorAcesso\n    participant U as MD_Usuarios\n    A->>M: alterarPapel(usuario_id, papel)\n    activate M\n    M->>U: setPapel(papel)\n    U-->>M: ok\n    M-->>A: Alteração Concluída\n    deactivate M"
    },
    {
        "id": "UC05_Gerenciar_Conteudo_Cartas",
        "title": "Gerenciar Conteúdo e Cartas",
        "desc": "Criação e manutenção de flashcards e módulos de estudo pelos tutores.",
        "astah_tips": "Dica Astah: Use a 'Composição' (losango preenchido) de Módulo para Flashcards (Ciclo de vida dependente).",
        "steps_class": ["MD_Tutor", "MD_Modulos", "MD_Flashcards", "Composição: Módulo *-- Flashcard"],
        "steps_seq": ["Tutor -> MD_Modulos: criarModulo()", "Tutor -> MD_Flashcards: criarCarta(pergunta, resposta)"],
        "mermaid_class": "classDiagram\n    MD_Modulos *-- MD_Flashcards\n    class MD_Tutor {\n        +gerenciarConteudo()\n    }\n    class MD_Modulos {\n        +string nomeModulo\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant T as Tutor\n    participant S as Sistema\n    participant M as MD_Modulos\n    T->>S: novoModulo(nome)\n    S->>M: <<create>>\n    T->>S: adicionarCarta(p, r)\n    S-->>T: Conteúdo Salvo"
    },
    {
        "id": "UC06_Acompanhar_Desempenho",
        "title": "Acompanhar Desempenho",
        "desc": "Visualização de métricas de progresso e engajamento dos alunos.",
        "astah_tips": "Dica Astah: No diagrama de sequência, represente o 'Painel' como uma classe de 'Fronteira' (Boundary).",
        "steps_class": ["MD_Tutor", "MD_Alunos", "PainelVisual", "Atributo: progresso: decimal"],
        "steps_seq": ["Tutor -> PainelVisual: requisitarDados(aluno)", "PainelVisual -> MD_Alunos: obterMetricas()", "PainelVisual -->> Tutor: Renderiza Gráficos"],
        "mermaid_class": "classDiagram\n    class MD_Tutor {\n        +acompanharDesempenho()\n    }\n    class MD_Alunos {\n        +float progresso\n    }\n    MD_Tutor ..> MD_Alunos : visualiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant T as Tutor\n    participant D as PainelVisual\n    participant A as MD_Alunos\n    T->>D: visualizar(aluno_id)\n    activate D\n    D->>A: obterMetricas()\n    A-->>D: dados_progresso\n    D-->>T: Relatório Visual\n    deactivate D"
    },
    {
        "id": "UC07_Escalar_Duvida_Tutor",
        "title": "Escalar Dúvida para Tutor",
        "desc": "Transferência de suporte da IA para um tutor humano quando a complexidade excede o limite do agente.",
        "astah_tips": "Dica Astah: Use uma 'Mensagem Assíncrona' para indicar que o Tutor não responderá instantaneamente.",
        "steps_class": ["AgenteIA", "MD_Tutor", "MD_Duvidas", "Associação: IA sinaliza Tutor"],
        "steps_seq": ["AgenteIA -> AgenteIA: analisarAmbiguidade()", "AgenteIA -> MD_Tutor: escalar(duvida)", "Tutor -->> Aluno: Resposta (Offline)"],
        "mermaid_class": "classDiagram\n    class AgenteIA {\n        +analisarAmbiguidade()\n        +escalar(duvida)\n    }\n    class MD_Tutor {\n        +responderDuvida()\n    }\n    AgenteIA --> MD_Tutor : notifica",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant IA as AgenteIA\n    participant T as MD_Tutor\n    participant Al as Aluno\n    IA->>IA: detectarComplexidade()\n    IA->>T: escalar(duvida, aluno_id)\n    Note right of T: Tutor analisa o contexto\n    T-->>Al: Resposta Detalhada (Email/App)"
    },
    {
        "id": "UC08_Consultar_Agente_IA",
        "title": "Consultar Agente IA",
        "desc": "Interação instantânea com o especialista virtual para dúvidas pontuais.",
        "astah_tips": "Dica Astah: Represente a 'MD_Duvidas' como um objeto persistente (Store/Entity).",
        "steps_class": ["AgenteIA", "MD_Duvidas", "Método: responder(pergunta)"],
        "steps_seq": ["Aluno -> AgenteIA: perguntar()", "AgenteIA -> MD_Duvidas: salvar()", "AgenteIA -->> Aluno: resposta_formatada"],
        "mermaid_class": "classDiagram\n    class AgenteIA {\n        +responder(pergunta)\n    }\n    class MD_Duvidas {\n        +string pergunta\n        +string resposta\n    }\n    AgenteIA ..> MD_Duvidas : consulta",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant IA as AgenteIA\n    A->>IA: enviarDuvida(texto)\n    activate IA\n    IA->>IA: processarLinguagemNatural()\n    IA-->>A: Resposta Sugerida\n    deactivate IA"
    },
    {
        "id": "UC09_Estudar_Flashcards",
        "title": "Estudar Flashcards (SM-2)",
        "desc": "Ciclo de estudo principal utilizando o algoritmo de repetição espaçada.",
        "astah_tips": "Dica Astah: No diagrama de sequência, use um 'Fragmento de Loop' para indicar a revisão de múltiplos cartões.",
        "steps_class": ["MD_MotorSM2", "MD_Flashcards", "Atributos: intervalo: int, facilidade: decimal"],
        "steps_seq": ["Aluno -> MD_Flashcards: lerPergunta()", "Aluno -> MD_MotorSM2: calcularIntervalo(feedback)", "MD_MotorSM2 -> MD_Flashcards: atualizar()"],
        "mermaid_class": "classDiagram\n    class MD_MotorSM2 {\n        +aplicarSM2(feedback)\n    }\n    class MD_Flashcards {\n        +date proximaRevisao\n    }\n    MD_MotorSM2 --> MD_Flashcards : atualiza",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant M as MD_MotorSM2\n    participant F as MD_Flashcards\n    A->>F: lerPergunta()\n    A->>F: verResposta()\n    A->>M: informarDificuldade(1-5)\n    M->>M: aplicarSM2()\n    M->>F: setProximaRevisao(data)\n    F-->>A: Carta Agendada"
    },
    {
        "id": "UC10_Criar_Flashcards",
        "title": "Criar Flashcards",
        "desc": "Funcionalidade que permite ao aluno personalizar seu próprio deck de estudos.",
        "astah_tips": "Dica Astah: Utilize a associação '1..*' para indicar que um aluno pode criar múltiplas cartas.",
        "steps_class": ["MD_Alunos", "MD_Flashcards", "Método: criarCarta()"],
        "steps_seq": ["Aluno -> MD_Alunos: criarCarta()", "MD_Alunos -> MD_Flashcards: <<create>>"],
        "mermaid_class": "classDiagram\n    class MD_Alunos {\n        +criarCarta()\n    }\n    class MD_Flashcards {\n        +string pergunta\n        +string resposta\n    }\n    MD_Alunos \"1\" --> \"*\" MD_Flashcards : cria",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant E as Editor\n    participant F as MD_Flashcards\n    A->>E: entradaDados(p, r)\n    E->>F: <<create>>(p, r, usuario_id)\n    F-->>A: Carta Adicionada ao Deck"
    },
    {
        "id": "UC11_Realizar_Simulado_ENADE",
        "title": "Realizar Simulado ENADE",
        "desc": "Treinamento intensivo com tempo controlado e questões de exames oficiais.",
        "astah_tips": "Dica Astah: No diagrama de sequência, use um 'Fragmento Opt' para o caso de o tempo esgotar.",
        "steps_class": ["MD_Simulado", "Questao", "Atributo: tempoRestante: int"],
        "steps_seq": ["Aluno -> MD_Simulado: iniciarTeste()", "MD_Simulado -> MD_Simulado: calcularNota()", "Simulado -->> Aluno: Resultado Final"],
        "mermaid_class": "classDiagram\n    class MD_Simulado {\n        +int tempoRestante\n        +iniciarTeste()\n        +calcularNota()\n    }\n    class Questao {\n        +string texto\n    }\n    MD_Simulado \"1\" *-- \"*\" Questao",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant A as Aluno\n    participant S as MD_Simulado\n    participant T as Temporizador\n    A->>S: iniciarTeste()\n    activate S\n    S->>T: iniciar(120min)\n    loop Cada Questão\n        A->>S: responder(id, opcao)\n    end\n    A->>S: finalizar()\n    S->>T: parar()\n    S-->>A: Nota e Feedback\n    deactivate S"
    },
    {
        "id": "UC12_Atribuir_XP_Moedas",
        "title": "Atribuir XP e Moedas",
        "desc": "Motor de recompensas automático baseado na conclusão de atividades.",
        "astah_tips": "Dica Astah: No diagrama de classe, use uma 'Dependência' (seta tracejada) entre Sistema e Gamificação.",
        "steps_class": ["MD_Gamificacao", "MD_Alunos", "Método: creditarXP(valor)"],
        "steps_seq": ["Sistema -> MD_Gamificacao: calcularBonus()", "MD_Gamificacao -> MD_Alunos: creditarXP()"],
        "mermaid_class": "classDiagram\n    class MD_Gamificacao {\n        +calcularBonus()\n        +creditarXP(id, valor)\n    }\n    class MD_Alunos {\n        +int pontos\n        +int moedas\n    }\n    MD_Gamificacao ..> MD_Alunos : credita",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant S as Sistema\n    participant G as MD_Gamificacao\n    participant A as MD_Alunos\n    S->>G: notificarConclusao()\n    activate G\n    G->>G: calcularBonus()\n    G->>A: creditarXP(id, 100)\n    G-->>S: Atualizado\n    deactivate G"
    },
    {
        "id": "UC13_Desbloquear_Fases_Modulos",
        "title": "Desbloquear Fases e Módulos",
        "desc": "Progressão de conteúdo condicionada ao desempenho nas fases anteriores.",
        "astah_tips": "Dica Astah: Represente o estado 'bloqueada' como um atributo booleano público (+).",
        "steps_class": ["MD_Fases", "MD_Alunos", "Método: desbloquear()"],
        "steps_seq": ["GerenciadorProgresso -> MD_Alunos: obterProgressoTotal()", "GerenciadorProgresso -> MD_Fases: desbloquear()"],
        "mermaid_class": "classDiagram\n    class MD_Fases {\n        +bool bloqueada\n        +desbloquear()\n    }\n    class MD_Alunos {\n        +float progresso\n    }\n    MD_Fases ..> MD_Alunos : verifica",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant M as GerenciadorProgresso\n    participant A as MD_Alunos\n    participant F as MD_Fases\n    M->>A: obterProgressoTotal()\n    A-->>M: 0.85\n    M->>F: desbloquear()\n    F->>F: setBloqueada(false)\n    F-->>M: Liberada"
    },
    {
        "id": "UC14_Visualizar_Painel_Progresso",
        "title": "Visualizar Painel de Progresso",
        "desc": "Hub central onde o aluno acompanha sua jornada e conquistas.",
        "astah_tips": "Dica Astah: No diagrama de classe, mostre que o Painel lê dados de Aluno.",
        "steps_class": ["PainelVisual", "MD_Alunos", "Método: renderizarDados()"],
        "steps_seq": ["Aluno -> PainelVisual: renderizarDados()", "PainelVisual -> MD_Alunos: obterProgressoTotal()"],
        "mermaid_class": "classDiagram\n    class PainelVisual {\n        +renderizarDados()\n    }\n    class MD_Alunos {\n        +obterProgressoTotal()\n    }\n    PainelVisual ..> MD_Alunos : lê",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant Al as Aluno\n    participant D as PainelVisual\n    Al->>D: abrirInicio()\n    activate D\n    D->>D: renderizarDados()\n    D-->>Al: Visualização Completa\n    deactivate D"
    },
    {
        "id": "UC15_Ajustar_Acessibilidade",
        "title": "Ajustar Acessibilidade",
        "desc": "Personalização da interface para garantir inclusão e conforto visual.",
        "astah_tips": "Dica Astah: No diagrama de classe, adicione atributos como 'altoContraste' e 'tamanhoFonte'.",
        "steps_class": ["MD_Acessibilidade", "MD_Usuarios", "Método: salvarConfiguracao()"],
        "steps_seq": ["Usuario -> MD_Acessibilidade: salvarConfiguracao()"],
        "mermaid_class": "classDiagram\n    class MD_Acessibilidade {\n        +bool altoContraste\n        +int tamanhoFonte\n        +salvarConfiguracao()\n    }",
        "mermaid_seq": "sequenceDiagram\n    autonumber\n    participant U as Usuario\n    participant P as PainelConfiguracao\n    participant A as MD_Acessibilidade\n    U->>P: selecionarOpcoes(contraste, fonte)\n    P->>A: salvarConfiguracao()\n    A-->>P: ok\n    P-->>U: Interface Atualizada"
    }
]

# Novos caminhos organizados
base_path = "c:/Users/mayco/Documents/GitHub/Documentacao_UML/PIM_III/02_Modelagem_UML_Astah"
dashboard_path = "c:/Users/mayco/Documents/GitHub/Documentacao_UML/PIM_III/01_Gestao_e_Planejamento/DASHBOARD_VISUAL.md"

# 1. Gerar os READMEs individuais (Totalmente em PT-BR)
for uc in use_cases:
    folder_path = os.path.join(base_path, uc["id"])
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_path = os.path.join(folder_path, "README.md")
    
    content = f"# 📘 Guia de Modelagem: {uc['title']}\n\n"
    content += f"## 🎯 Objetivo do Caso de Uso\n{uc['desc']}\n\n"
    content += f"> [!TIP]\n> {uc['astah_tips']}\n\n"
    
    content += "## 🚀 Tutorial de Criação Passo a Passo (Astah)\n\n"
    
    content += "### 1️⃣ Criando o Diagrama de Classe\n"
    content += f"1. No Menu Superior, vá em **Projeto** > **Árvore de Estrutura**.\n"
    content += f"2. Clique com o botão direito e selecione **Adicionar Diagrama** > **Diagrama de Classe**.\n"
    content += f"3. Arraste as classes para a área de desenho:\n"
    for step in uc["steps_class"]:
        content += f"   - [ ] Criar **{step}**.\n"
    content += "4. Adicione os **Atributos** e **Métodos** clicando com o botão direito na classe.\n"
    content += "5. Use as ferramentas de **Associação, Dependência ou Herança** para ligar as classes conforme a referência abaixo.\n\n"
    
    content += "### 2️⃣ Criando o Diagrama de Sequência\n"
    content += f"1. Clique com o botão direito no Caso de Uso (na Árvore) e selecione **Adicionar Diagrama** > **Diagrama de Sequência**.\n"
    content += f"2. Adicione os **Participantes** (Linhas de Vida) no topo da tela.\n"
    content += f"3. Desenhe as setas de mensagem seguindo rigorosamente esta ordem:\n"
    for i, step in enumerate(uc["steps_seq"], 1):
        content += f"   - [ ] {i}. **{step}**\n"
    content += "4. Lembre-se de adicionar as **Barras de Ativação** clicando sobre a linha de vida onde houver processamento.\n\n"
    
    content += "---\n\n"
    content += "## 📊 Referência Visual (Padrão PT-BR)\n"
    content += "### Diagrama de Classe\n"
    content += f"```mermaid\n{uc['mermaid_class']}\n```\n\n"
    content += "### Diagrama de Sequência\n"
    content += f"```mermaid\n{uc['mermaid_seq']}\n```\n\n"
    content += "---\n*Manual técnico gerado em Português para conformidade com o PIM III.*"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Gerar o Dashboard Visual Centralizado (PT-BR)
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
    db_content += f"\n[Abrir Guia de Modelagem Passo a Passo](../02_Modelagem_UML_Astah/{uc['id']}/README.md)\n"

with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(db_content)

print("Processo 100% traduzido para PT-BR.")
