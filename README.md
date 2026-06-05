# 📂 csv-structure-comparator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

> Utilitário para validar a consistência estrutural entre dois arquivos CSV — detectando colunas ausentes ou adicionadas em relação a um arquivo de referência.

---

## 📌 Descrição

Em pipelines de dados, é comum receber arquivos CSV de fontes externas que deveriam seguir uma estrutura predefinida. O **csv-structure-comparator** compara o conjunto de colunas de dois arquivos CSV e reporta:

- ✅ Se a estrutura é idêntica
- ❌ Quais colunas estão **faltando** no novo arquivo
- ➕ Quais colunas **extras** foram adicionadas

---

## 🗂️ Estrutura do Projeto

```
csv-structure-comparator/
├── compare_csv_structure.py   # Script principal
├── data/
│   ├── dados_modelo.csv       # Arquivo de referência (estrutura esperada)
│   └── dados_recebidos.csv    # Arquivo recebido para validação
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalação

**1. Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/csv-structure-comparator.git
cd csv-structure-comparator
```

**2. Instale as dependências:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Como usar

```python
from compare_csv_structure import compare_csv_structure

compare_csv_structure('data/dados_modelo.csv', 'data/dados_recebidos.csv')
```

Ou execute diretamente pelo terminal:

```bash
python compare_csv_structure.py
```

---

## 📋 Exemplo de output

**Caso os arquivos tenham a mesma estrutura:**

```
✅ Sucesso: A estrutura dos arquivos CSV é exatamente a mesma.
```

**Caso existam divergências:**

```
⚠️ Atenção: Foram encontradas divergências na estrutura!
❌ Colunas que estão faltando no novo arquivo: {'preco_unitario', 'data_vencimento'}
➕ Novas colunas que foram adicionadas: {'desconto_aplicado'}
```

---

## 📦 Dependências

```
pandas>=2.0.0
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👤 Autor

Feito por **Rafael** — [github.com/seu-usuario](https://github.com/seu-usuario)
