
# Auto Refino - Perfect World

## Visão Geral
Este projeto contém dois scripts em Python para automação e listagem de processos específicos do sistema:

1. **Script de Automação**: Realiza cliques em uma posição específica dentro de uma janela, com base no ID do processo (PID) e nas coordenadas da janela. 
2. **Script de Listagem de Processos**: Lista todos os processos em execução que correspondem ao executável `elementclient`.

A ideia é fazer um auto click por processo, para não ficar com o pc parado no aprimoramento do Perfect World

### Exemplo da aplicação:

Executar o `processo.py`

```
python processo.py
```

![image](https://github.com/user-attachments/assets/25282c66-0cca-4def-8555-c3c8d9bc716c)

Executar o `farm/1.py`

```
python farm/1.py
```

![Captura de tela 2024-11-11 200725](https://github.com/user-attachments/assets/63407c3e-f96c-4c3c-a46b-67e2eee46972)

##### Aplicação: 

![image](https://github.com/user-attachments/assets/15b45906-ec58-4547-ac3a-e519422831c3)

![image](https://github.com/user-attachments/assets/09d47d78-6d9e-4935-bee3-39f2497d5776)

### Nota:

> Use a configuração padrão do x e y para não precisar ajustar.. aplique a resolução 1760x990 e ajuste a aba de aprimoramento exatamente como está no exemplo da aplicação acima..

![image](https://github.com/user-attachments/assets/1c07b8e5-cd39-4f07-b818-e431628187d6)

### Pré-requisitos
- **Python** (recomendado 3.12 ou superior)
- **Bibliotecas Python**:
  - `psutil`: para interação com processos do sistema.
  - `pywin32`: para automação de cliques e manipulação de janelas no Windows.

Para instalar as bibliotecas necessárias:
```bash
pip install psutil pywin32
```

---

## Script de Automação

Pasta /farm/

>Arquivo: `1.py`

>Arquivo: `2.py`

>Arquivo: `3.py`

> ...

### Configuração
Altere as variáveis no script conforme necessário:
- **PID**: ID do processo da aplicação alvo.
- **x** e **y**: coordenadas do clique dentro da janela. 
- **clicks**: número de cliques a serem realizados.
- **delay**: intervalo entre os cliques em segundos.

Valores padrão:
```python
pid = 2492  # Altere para o ID do processo desejado
x = 315     # Coordenada X
y = 484     # Coordenada Y
clicks = 4500  # Número de cliques a serem realizados
delay = 1   # Tempo entre cliques em segundos
```

### Execução
Para executar o script:
```bash
python 1.py
```

> #### Ou qualquer script dentro da pasta /farm/

O script tentará localizar a janela do processo pelo PID e executar os cliques na posição especificada.

### Funções Principais
- **encontrar_janela_por_pid(pid)**: Localiza a janela visível com base no PID do processo.
- **click_in_window(hwnd, x, y, clicks, delay)**: Realiza os cliques na posição `(x, y)` da janela especificada.

### Observação
O script funciona apenas no Windows, pois utiliza a biblioteca `pywin32` para controle de janelas.

---

## Script de Listagem de Processos
Arquivo: `processo.py`

### Descrição
Este script lista todos os processos que correspondem ao nome `elementclient`, retornando seus nomes e IDs de processo (PID). É útil para identificar o PID do processo desejado antes de executar o script de cliques.

### Execução
Para listar os processos:
```bash
python processo.py
```

O script imprimirá os nomes e PIDs dos processos encontrados.

### Função Principal
- **listar_processos()**: Itera sobre os processos ativos e exibe informações dos processos que contêm o termo `elementclient` no nome.

---

## Exemplo de Uso
1. Execute `processo.py` para encontrar o PID do processo `elementclient`.
2. Insira o PID encontrado no script de automação de cliques (`farm/1.py`).
3. Execute `1.py` para iniciar os cliques automáticos na janela.

