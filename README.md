# 🎓 Nex_TI: Plataforma de Aprendizado Adaptativo com Gamificação e IA

<p align="center">
  <img src="https://img.shields.io/badge/Projeto-PIM_III-blue.svg" alt="PIM III">
  <img src="https://img.shields.io/badge/UML-Astah_10.1-orange.svg" alt="Astah">
  <img src="https://img.shields.io/badge/Documenta%C3%A7%C3%A3o-PlantUML-green.svg" alt="PlantUML">
</p>

Bem-vindo ao repositório oficial da **Documentação UML e Arquitetura do Sistema Nex_TI**, desenvolvido como parte do Projeto Integrado Multidisciplinar (PIM III) da UNIP. 

O **Nex_TI** é um sistema educacional revolucionário que utiliza o algoritmo de Repetição Espaçada (SM-2), mecânicas de gamificação (XP e Moedas) e um Agente Especialista baseado em Inteligência Artificial para otimizar a jornada de aprendizado do aluno.

---

## 📌 Links Rápidos para a Banca Avaliadora

Para facilitar a navegação pelos principais artefatos do projeto:

- 📊 **[Dashboard Visual Completo](./01_Relatorios_e_Dashboard/DASHBOARD_VISUAL.md)**: Visão interativa de todos os Casos de Uso, Diagramas Globais e Arquitetura.
- 📄 **[Relatório Final PIM III (Teórico)](./01_Relatorios_e_Dashboard/RELATORIO_FINAL_PIM_III.md)**: Base teórica e fundamentos arquiteturais (POO).
- 🧩 **[Artefatos Gerados (Diagramas PNG)](./03_Artefatos_Gerados)**: Repositório com todas as imagens renderizadas dos diagramas de Classe, Sequência e Casos de Uso.
- 🧠 **[Detalhamento e Fluxos dos 15 Casos de Uso](./02_Modelagem_UML_Astah)**: Documentação granular com Fluxo Normal, Fluxo Alternativo e diagramas locais.

---

## 🏗️ Estrutura do Repositório

Organizamos este repositório focando na alta legibilidade, separação de conceitos (SoC) e manutenção contínua:

```text
📁 PIM_III-Documentacao_UML/
├── 📁 .planning/                      # Gerenciamento ágil GSD (Roadmaps, Fases, Specs)
├── 📁 01_Documentacao_Teorica/        # Documentações complementares em PDF (Atas, Backlogs)
├── 📁 01_Relatorios_e_Dashboard/      # Relatório final PIM III e Painel de Controle Visual
├── 📁 02_Modelagem_UML/               # Modelagem fonte no Astah (.asta) e diagramas globais
├── 📁 02_Modelagem_UML_Astah/         # Manuais passo-a-passo e Mermaid de cada um dos 15 UCs
├── 📁 03_Artefatos_Gerados/           # Diagramas globais exportados (.png e códigos PlantUML)
├── 📁 04_Scripts/                     # Automações portáveis em Python (Geração de Docs, Compilação UML)
└── 📁 05_Legacy/                      # Códigos gerados antigos e diagramas antigos legados
```


## 📐 Padrões Arquiteturais Adotados

A nossa modelagem foi desenvolvida estritamente sobre as melhores práticas da **Engenharia de Software Orientada a Objetos**:
1. **Encapsulamento Restrito**: Todos os atributos de Entidades foram definidos como privados (`-`), sendo expostos apenas via métodos públicos (`+`).
2. **Separação de Preocupações (MVC/ECB)**: Classes de Dados (`<<Entidade>>`) não misturam lógica com Agentes de Serviço (`<<Control>>`).
3. **Padrão Astah Otimizado**: O visual dos nossos diagramas no PlantUML foram parametrizados (`skinparam`) para replicar as cores, layout em cascata e identidades visuais da ferramenta Astah (versão 10).

---

> Desenvolvido com foco na excelência acadêmica e aplicação real no mercado de TI. 🚀
