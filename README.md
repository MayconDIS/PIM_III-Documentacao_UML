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

- 📊 **[Diagramas Globais e Modelagem (.asta)](./02_Modelagem_UML)**: Diagramas globais de Classe, Sequência e Casos de Uso em alta definição (PNG), além do arquivo fonte `.asta` para ser carregado diretamente no software **Astah UML**.
- 📄 **[Documentação Teórica e Planejamento](./01_Documentacao_Teorica)**: Fundamentos teóricos, Backlog do produto Nex_TI e atas de planejamento de sprint em PDF.
- 💻 **[Classes C# Geradas (.cs)](./03_Codigo_Gerado)**: Esboço de arquivos de classe em C# gerados automaticamente pelo Astah a partir do modelo de classes final.

---

## 🏗️ Estrutura do Repositório

Organizamos este repositório focando na simplicidade, clareza e separação de conceitos:

```text
📁 PIM_III-Documentacao_UML/
├── 📁 .planning/                      # Gerenciamento ágil GSD (Roadmaps, Fases, Specs)
├── 📁 01_Documentacao_Teorica/        # Documentações teóricas e atas de planejamento em PDF
├── 📁 02_Modelagem_UML/               # Modelagem fonte do Astah (.asta) e imagens globais (.png)
└── 📁 03_Codigo_Gerado/               # Esboço das classes C# exportadas do modelo de classes
```



## 📐 Padrões Arquiteturais Adotados

A nossa modelagem foi desenvolvida estritamente sobre as melhores práticas da **Engenharia de Software Orientada a Objetos**:
1. **Encapsulamento Restrito**: Todos os atributos de Entidades foram definidos como privados (`-`), sendo expostos apenas via métodos públicos (`+`).
2. **Separação de Preocupações (MVC/ECB)**: Classes de Dados (`<<Entidade>>`) não misturam lógica com Agentes de Serviço (`<<Control>>`).
3. **Padrão Astah Otimizado**: O visual dos nossos diagramas no PlantUML foram parametrizados (`skinparam`) para replicar as cores, layout em cascata e identidades visuais da ferramenta Astah (versão 10).

---

> Desenvolvido com foco na excelência acadêmica e aplicação real no mercado de TI. 🚀
