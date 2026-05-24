# Projeto: Nex_TI UML Documentation

## 🎯 Visão
Transformar requisitos de negócio em uma documentação técnica UML de alta fidelidade para o sistema Nex_TI, servindo como base sólida para a implementação e para a entrega do PIM III.

## 💻 Tech Stack
- **Documentação:** Markdown (GFM)
- **Diagramação:** Mermaid.js (Visualização) / Astah (Modelagem Profissional)
- **Automação:** Python (Geração de guias passo a passo)
- **Framework de Gestão:** GSD (Get Shit Done)

## 🚩 Objetivos Principais
1. Modelar 15 Casos de Uso (Classe e Sequência).
2. Fornecer guias de recriação detalhados para o software Astah.
3. Manter um Dashboard Visual centralizado para consulta rápida.
4. Garantir a consistência arquitetural seguindo o padrão MVC.

## 👥 Papéis
- **Analista de Sistemas:** Responsável pela lógica dos UCs.
- **Arquiteto de Software:** Responsável pelo Diagrama de Classes Global.
- **Desenvolvedor:** Responsável pela automação da documentação.


### 🔄 Refatoração de Maio (PIM III - Nex_TI)
- Todos os Casos de Uso (1-15) foram refatorados pelo agente GSD-Architect.
- Nomes de classes obsoletos (MD_Usuarios, MD_Alunos) foram substituídos pelas entidades definitivas C# (Usuario, Aluno, Flashcard_SM2, etc).
- O modelo UML agora está 100% aderente ao index.html do relatório final.

### 🧹 Reorganização e Manutenção Geral (Fase 10)
- Scripts de automação Python atualizados para utilizar caminhos relativos portáveis.
- Nomenclatura obsoleta com prefixo `MD_` removida dos manuais locais de Casos de Uso e do Dashboard Visual.
- Remoção de arquivos duplicados de imagens e arquivos temporários de backup `.bak`.
- Pasta de código gerado obsoleta (`03_Codigo_Gerado`) movida para `05_Legacy/Codigo_Gerado_Astah_Legado` para manter a raiz limpa.

