# 🌊 Fluxos dos Casos de Uso - Sistema Nex_TI

Abaixo estão detalhados o **Fluxo Normal** e o **Fluxo Alternativo** para cada um dos 15 Casos de Uso do sistema. Você pode copiar e colar essas descrições diretamente nos arquivos `README.md` de cada pasta correspondente.

---

### UC01 - Realizar Login
- **Fluxo Normal:** O usuário acessa a tela inicial e informa seu e-mail e senha. O sistema valida as credenciais criptografadas (Hash) no banco de dados e redireciona o usuário para o painel principal correspondente ao seu perfil (Aluno, Tutor ou Admin).
- **Fluxo Alternativo:** O usuário informa uma senha incorreta ou um e-mail não cadastrado. O sistema exibe uma mensagem de erro ("Credenciais inválidas") e solicita uma nova tentativa, sem revelar se o erro foi no e-mail ou na senha (segurança).

### UC02 - Cadastrar Novo Usuário
- **Fluxo Normal:** O usuário clica em "Criar Conta", preenche o formulário de registro com dados pessoais e escolhe uma senha. O sistema aplica o Hash na senha, persiste o usuário no banco de dados e o redireciona automaticamente para a etapa de Teste de Nivelamento.
- **Fluxo Alternativo:** O usuário insere um e-mail que já existe no banco de dados. O sistema bloqueia o cadastro e exibe um alerta sugerindo a recuperação de senha.

### UC03 - Realizar Teste de Nivelamento
- **Fluxo Normal:** Logo após o primeiro acesso, o sistema apresenta um questionário diagnóstico. O aluno responde às questões, e o sistema processa a nota para calcular o nível base, liberando os módulos de estudo adequados à sua proficiência.
- **Fluxo Alternativo:** O aluno decide pular o teste através do botão "Fazer depois". O sistema atribui o módulo básico (introdutório) por padrão.

### UC04 - Gerenciar Perfis e Acessos
- **Fluxo Normal:** O Administrador acessa o painel de gestão de usuários. Ele pesquisa por um usuário específico e altera sua permissão de acesso (ex: promovendo um Aluno a Tutor). O sistema salva a alteração e aplica na próxima sessão do usuário modificado.
- **Fluxo Alternativo:** O Administrador tenta revogar os seus próprios privilégios de administrador. O sistema bloqueia a ação para evitar que o sistema fique sem nenhum admin.

### UC05 - Gerenciar Conteúdo das Cartas
- **Fluxo Normal:** O Tutor acessa o repositório de disciplinas, cria um novo "Deck", cadastra os flashcards preenchendo as informações de "Frente" (Pergunta) e "Verso" (Resposta/Explicação) e publica o módulo para os alunos.
- **Fluxo Alternativo:** O Tutor tenta excluir um Deck que já está ativamente sendo estudado por vários alunos. O sistema emite um alerta de dependência (ON DELETE) e sugere apenas ocultar (arquivar) o conteúdo para novos alunos.

### UC06 - Acompanhar Desempenho dos Usuários
- **Fluxo Normal:** O Tutor acessa a aba de estatísticas e seleciona uma turma ou aluno. O sistema extrai os dados do motor SM-2 (taxa de acertos/erros e tempo de resposta) e exibe gráficos interativos de retenção de conhecimento.
- **Fluxo Alternativo:** O Tutor pesquisa por um aluno que ainda não iniciou nenhuma sessão de flashcards. O sistema exibe a mensagem: "Dados insuficientes para gerar estatísticas".

### UC07 - Escalar Dúvida para Tutor
- **Fluxo Normal:** Durante uma sessão de estudos, o aluno clica no botão "Tenho uma dúvida" no flashcard. Ele digita a pergunta e envia. O sistema notifica o Tutor responsável pela área de conhecimento. O Tutor responde e o aluno é notificado.
- **Fluxo Alternativo:** O prazo de resposta do Tutor (SLA) é ultrapassado. O sistema marca a dúvida com a flag de "Prioridade Alta" e dispara um e-mail de alerta para a coordenação (Admin).

### UC08 - Consultar Agente Especialista (IA)
- **Fluxo Normal:** O aluno solicita ajuda à IA no chat. A IA (Agente Especialista) recebe a dúvida, identifica o contexto do flashcard atual através de Processamento de Linguagem Natural (NLP) e retorna uma explicação detalhada e pedagógica.
- **Fluxo Alternativo:** A IA não consegue interpretar a pergunta ou o aluno faz uma pergunta muito fora de contexto. A IA solicita reformulação ou sugere automaticamente "Escalar a dúvida para o Tutor humano".

### UC09 - Estudar Flashcards
- **Fluxo Normal:** O aluno abre um deck e o sistema exibe a frente da carta. O aluno mentaliza a resposta e clica em "Mostrar Verso". O aluno autoavalia sua facilidade (Fácil, Bom, Difícil). O motor SM-2 recalcula e agenda a data da próxima revisão do card. (Aciona o *include* de Atribuir XP).
- **Fluxo Alternativo:** O aluno conclui todos os cards agendados para o dia de hoje. O sistema informa que as metas diárias foram cumpridas e sugere descanso ou revisar módulos opcionais.

### UC10 - Criar Flashcards (Personalizados)
- **Fluxo Normal:** O aluno deseja aprofundar um tema específico e clica em "Criar Card Pessoal". Preenche frente e verso e salva no seu deck privado, que agora também fará parte da rotina de repetição espaçada.
- **Fluxo Alternativo:** O aluno tenta salvar o card deixando o verso em branco. O sistema desabilita o botão de salvar e destaca o campo obrigatório em vermelho.

### UC11 - Realizar Simulado ENADE
- **Fluxo Normal:** O aluno acessa a área de preparação e inicia um simulado temporizado de múltipla escolha. Ao finalizar e enviar, o sistema corrige com base no gabarito, exibe o percentual de acerto e fornece um relatório detalhado. (Aciona o *include* de Atribuir XP).
- **Fluxo Alternativo:** A internet do aluno cai no meio do simulado. O sistema, utilizando persistência local (LocalStorage), salva o progresso e permite a retomada exata de onde parou ao reconectar.

### UC12 - Atribuir XP e Moedas
- **Fluxo Normal:** Ao final de um evento de aprendizagem validado (simulado ou sessão de flashcards), a rotina de gamificação é acionada invisivelmente no backend. O sistema soma os XP ao histórico do aluno, verifica se ele subiu de nível, e deposita o valor equivalente em moedas virtuais.
- **Fluxo Alternativo:** O sistema detecta que o aluno passou rápido demais pelas cartas (indício de burla/click spam). O sistema reduz drasticamente o multiplicador de XP para desestimular esse comportamento.

### UC13 - Desbloquear Fases e Módulos
- **Fluxo Normal:** O aluno acessa a "Loja" virtual. Ele escolhe um módulo avançado restrito, verifica que possui moedas suficientes e clica em "Comprar". O sistema deduz as moedas do saldo e libera o acesso permanente ao módulo.
- **Fluxo Alternativo:** O aluno tenta desbloquear um módulo, mas seu saldo de moedas virtuais é insuficiente. O botão de compra permanece inativo e o sistema exibe quanto falta para adquirir o item.

### UC14 - Visualizar Painel de Progresso
- **Fluxo Normal:** O aluno abre seu Dashboard. O sistema renderiza o nível atual, barra de experiência, total de moedas e um "mapa de calor" (heatmap) mostrando sua frequência de estudo (ofensiva diária).
- **Fluxo Alternativo:** É o primeiro acesso do aluno. O Dashboard exibe métricas zeradas, destacando botões interativos (Call to Action) que convidam o aluno a realizar a primeira sessão de estudos para preencher os gráficos.

### UC15 - Ajustar Acessibilidade
- **Fluxo Normal:** O usuário acessa o menu de configurações globais de interface e seleciona opções como "Aumentar Fonte" ou "Ativar Alto Contraste". O sistema aplica as regras de CSS na hora e salva a preferência na sessão ou banco de dados do usuário.
- **Fluxo Alternativo:** O usuário ativa uma configuração que conflita com o layout da tela. Ele clica em "Restaurar Padrões", e o sistema limpa as injeções de estilo, retornando o layout à folha de estilo original.
