# llm-adaptation-banking-agent

Практическая работа по методам адаптации LLM (Prompting, RAG, Fine-Tuning) на примере создания банковского ИИ-ассистента.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pueraeternis/llm-adaptation-banking-agent/blob/main/notebooks/banking_agent.ipynb)

## Структура репозитория

```
├── data/
│   ├── banking_tariffs.txt   # Файл со знаниями для RAG
│   └── lora_dataset.jsonl    # Микро-датасет для Fine-Tuning (LoRA)
├── notebooks/
│   └── banking_agent.ipynb   # Основной Jupyter-ноутбук (Colab)
├── requirements.txt          # Зависимости Python
└── README.md
```

## Быстрый старт

### Google Colab

1. Откройте ноутбук по [ссылке на Colab](https://colab.research.google.com/github/pueraeternis/llm-adaptation-banking-agent/blob/main/notebooks/banking_agent.ipynb).
2. В меню выберите **Среда выполнения → Сменить среду выполнения → T4 GPU** (рекомендуется для Fine-Tuning).
3. Выполняйте ячейки по порядку.

### Локально

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/banking_agent.ipynb
```

## Содержание практики

| Этап | Метод | Данные |
|------|--------|--------|
| 1 | Prompt Engineering | Системный промпт в ноутбуке |
| 2 | RAG | `data/banking_tariffs.txt` |
| 3 | Fine-Tuning (LoRA) | `data/lora_dataset.jsonl` |

## Лицензия

Учебный проект OTUS.
