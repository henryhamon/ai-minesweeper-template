# 💣 Campo Minado - AI Sweeper: Survival Mode (Template)
![Badge Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Badge Python](https://img.shields.io/badge/Python-3.8+-blue)
![Badge IA](https://img.shields.io/badge/AI-Deep_Learning-purple)

Bem-vindos ao projeto final da Unidade 3 da disciplina de Fundamentos de IA.
Sua missão é construir uma Rede Neural capaz de jogar Campo Minado e sobreviver à Arena do Professor.

## 🚀 Como começar (Onboarding)

1. Clique no botão verde **"Use this template"** (Usar este modelo) no topo desta página do GitHub para criar uma cópia deste repositório na sua conta.
2. Clone o **SEU** novo repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/SEU-USUARIO/nome-do-seu-repo.git](https://github.com/SEU-USUARIO/nome-do-seu-repo.git)
   cd nome-do-seu-repo
   ```
3. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Escolha a sua Arma (Starter Kit):**
   Navegue até a pasta `starter_kits/` e escolha o nível de abstração que sua equipe vai utilizar. Recomendamos fortemente o `nivel_3_keras_dl.py` para a nota máxima da disciplina.
5. **Pegue os Dados:**
   Na pasta `dataset/` você encontrará as instruções e o link para baixar as matrizes do Campo Minado.

## 📥 Preparando o Dataset (Os Dados de Treino)

Para facilitar a vida do Squad, o dataset oficial já foi incluído no repositório, mas está compactado para respeitar os limites do GitHub.

**Antes de rodar qualquer código, faça o seguinte:**

1. Navegue até a pasta `data/` do seu repositório local.
2. Você encontrará o arquivo `minesweeper_data.zip`.
3. **Extraia (Unzip)** este arquivo na própria pasta `data/`.
4. O arquivo extraído deve se chamar obrigatoriamente `minesweeper_data.csv`.

Sua estrutura final deve ficar exatamente assim para o código funcionar:
```text
ai-sweeper/
├── data/
│   ├── minesweeper_data.zip    <-- O arquivo original compactado
│   └── minesweeper_data.csv    <-- O arquivo que você extraiu (O código lerá este!)
├── src/
...
```

### Opção Kaggle

Caso queira você pode utilizar o dataset diretamente do Kaggle. 

**Siga este passo a passo rigorosamente:**

1. Crie uma conta gratuita no [Kaggle](https://www.kaggle.com/) (se ainda não tiver uma).
2. Acesse a página do dataset oficial procurando por **"Minesweeper Game Dataset"** (ou acesse o link fornecido pelo professor no portal da disciplina).
3. Clique no botão **Download** (Geralmente baixa um arquivo compactado `.zip`).
4. **Extraia o arquivo .zip** no seu computador.
5. Pegue o arquivo extraído (que deve ser um `.csv`) e mova-o para dentro da pasta `data/` do seu repositório local.
6. ⚠️ **Muito Importante:** Renomeie o arquivo para `minesweeper_data.csv`. Os Starter Kits estão programados para procurar exatamente por este nome!

Se a sua estrutura ficar assim, você está pronto para codar:

```text
ai-sweeper/
├── data/
│   └── minesweeper_data.csv    <-- Seu arquivo deve estar exatamente aqui!
├── src/
...
```

⚠️ **Aviso de Engenharia:** O arquivo `.csv` tem mais de 100 MB. O `.gitignore` do projeto já está configurado para **ignorar** esse arquivo CSV gigante. Não tentem forçar o commit dele, ou o repositório de vocês será bloqueado pelo GitHub!


## 📂 Estrutura do Projeto

A organização do código reflete os padrões da indústria para MLOps:

* 📁 `data/` : Onde você deve colocar o dataset `minesweeper_data.csv` baixado do Kaggle.
* 📁 `starter_kits/` : Scripts de exemplo criados pelo professor demonstrando a estrutura em Python Puro, Scikit-Learn e Keras/TensorFlow. Use-os como inspiração!
* 📁 `src/` : **Seu ambiente de trabalho.** O arquivo `ai_sweeper.py` principal fica aqui.

## ⚔️ A Regra de Ouro da Arena (MUITO IMPORTANTE)
O arquivo `src/ai_sweeper.py` possui uma função chamada `prever_jogada_segura(tabuleiro_atual, modelo)`. 
**NÃO ALTERE O NOME DESTA FUNÇÃO NEM OS SEUS PARÂMETROS!**

No dia da apresentação, o Simulador do Professor vai importar o seu arquivo e chamar esta função. **Se a função não existir, tiver outro nome, ou não retornar uma tupla (x, y), o seu bot será desclassificado instantaneamente.**

## 🚨 Regra Anti-Cheat e Uso de IA

O uso de IAs Generativas (ChatGPT, GitHub Copilot, Claude) é **permitido** como assistente de sintaxe e tutor. No entanto, **vocês são os Arquitetos**. 

No dia do torneio, haverá uma sabatina (Code Review). Se o código possuir arquiteturas complexas ou funções que nenhum membro do squad consiga explicar de imediato, o projeto sofrerá **Cartão Vermelho (nota zerada)** por terceirização de código. Entendam cada linha do que estão entregando!

---

## 📝 Check-list de Entrega do Squad

Antes da data limite, garantam que o repositório de vocês possui:

- [ ] Código fonte modularizado e comentado na pasta `src/`.
- [ ] O arquivo do modelo treinado exportado (ex: `modelo_v1.pth` ou `modelo_v1.keras`) salvo na raiz do projeto.
- [ ] O formulário abaixo preenchido corretamente.

---

# 🛡️ Relatório Oficial do Squad (Preencham Aqui)

*(Instrução: Substituam os textos entre colchetes pelas informações do projeto de vocês)*

### 👥 Membros da Equipe
1. [Nome do Aluno 1]
2. [Nome do Aluno 2]
3. [Nome do Aluno 3]

### 🧠 Arquitetura Escolhida
* **Framework:** [Ex: TensorFlow/Keras ou Scikit-Learn]
* **Tipo de Modelo:** [Ex: Rede Neural Convolucional (CNN), Perceptron Multicamadas (MLP), Random Forest]
* **Camadas Ocultas:** [Ex: 2 camadas Densas de 128 neurônios, ou 1 camada Conv2D + Flatten]
* **Função de Ativação de Saída:** [Ex: Softmax para 64 classes]

### 📊 Desempenho no Treino
* **Acurácia Final de Treino:** [Ex: 85%]
* **Função de Loss Utilizada:** [Ex: Categorical Crossentropy]
* **Maior Dificuldade:** [Descrevam em 2 linhas o maior desafio que a equipe enfrentou. Ex: "A maior dificuldade foi converter as bandeiras do CSV num tensor NumPy sem quebrar a camada de Flatten."]

---
*Projeto desenvolvido para a disciplina de Fundamentos de IA - 2026.*