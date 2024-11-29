# Painel de Incêndios Florestais na Austrália

Este projeto utiliza **Dash** e **Plotly** para criar um painel interativo que visualiza dados históricos de incêndios florestais na Austrália. Ele permite selecionar diferentes regiões e anos para explorar dados, fornecendo insights sobre a área estimada de incêndios e ocorrências vegetativas ao longo do tempo.

## Funcionalidades
- **Seleção de Região**: Escolha entre as principais regiões da Austrália.
- **Seleção de Ano**: Visualize dados de um ano específico.
- **Gráficos Interativos**:
  - Gráfico de Rosca: Média mensal da área estimada de incêndios.
  - Gráfico de Barras: Média de ocorrências de incêndios vegetativos por mês.
- Interface limpa e intuitiva, com design responsivo.

## Tecnologias Utilizadas
- **Python**
- **Dash**: Para construção de aplicações web interativas.
- **Plotly**: Para geração de gráficos interativos.
- **Pandas**: Para manipulação de dados.

## Estrutura do Projeto
```plaintext
painel-incendios-australia/
│
├── app.py               # Código principal do painel
├── requirements.txt     # Lista de dependências
└── README.md            # Documentação do projeto
```

## Instalação e Execução

Siga os passos abaixo para clonar o repositório e executar o projeto localmente:

### Pré-requisitos
- Python 3.7 ou superior
- `pip` instalado

### 1. Clone o Repositório
Use o comando abaixo para clonar este repositório:
```bash
git clone https://github.com/samuel-c-santos/painel-incendios-australia.git
```

### 2. Navegue para o Diretório do Projeto
No terminal, vá até o diretório do projeto clonado:
```bash
cd painel-incendios-australia
```

### 3. Instale as Dependências
Execute o comando abaixo para instalar todas as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 4. Execute a Aplicação
Inicie o servidor local com o comando:
```bash
python app.py
```

Acesse o painel no seu navegador através do endereço:
```
http://127.0.0.1:8050/
```

## Pré-visualização
O painel consiste em gráficos que variam dinamicamente de acordo com os filtros de região e ano. Veja abaixo um exemplo de como o painel é exibido:

### Gráfico de Rosca
Visualize a **área estimada de incêndios** em cada mês:
![Gráfico de Rosca](https://via.placeholder.com/600x300?text=Gráfico+de+Rosca)

### Gráfico de Barras
Veja a **frequência de ocorrências vegetativas** por mês:
![Gráfico de Barras](https://via.placeholder.com/600x300?text=Gráfico+de+Barras)

## Contribuindo
Contribuições são bem-vindas! Siga os passos abaixo para colaborar:
1. Faça um fork do repositório.
2. Crie uma branch para sua feature/bugfix:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. Faça as alterações e faça commit:
   ```bash
   git commit -m "Descrição das mudanças"
   ```
4. Envie para sua branch:
   ```bash
   git push origin minha-nova-feature
   ```
5. Abra um pull request.

## Licença
Este projeto é licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato
Criado por **Samuel C. Santos**. Entre em contato via:
- [LinkedIn](https://www.linkedin.com/in/samuelsanto-amb/)
- [GitHub](https://github.com/samuel-c-santos)
```
