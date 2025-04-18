# Bot Telegram de Mensagens Agendadas

Um bot Telegram simples que envia mensagens agendadas em horários específicos, configurados através de variáveis de ambiente.

## 🚀 Funcionalidades

- Envio automático de mensagens em horários configuráveis
- Suporte ao fuso horário de São Paulo
- Logs de execução em arquivo
- Configuração via variáveis de ambiente

## 📋 Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd botTelegram
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente no arquivo `.env`:
```env
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id
SCHEDULE_HOUR=22
SCHEDULE_MINUTE=0
```

## ⚙️ Configuração

- `TELEGRAM_BOT_TOKEN`: Token do seu bot Telegram (obtido com o @BotFather)
- `TELEGRAM_CHAT_ID`: ID do chat onde as mensagens serão enviadas
- `SCHEDULE_HOUR`: Hora do envio (formato 24h)
- `SCHEDULE_MINUTE`: Minuto do envio

## 🚀 Executando o Bot

Para iniciar o bot, execute:
```bash
python main.py
```

O bot enviará mensagens no horário configurado, incluindo o horário atual de São Paulo.

## 📝 Logs

Os logs são salvos no arquivo `bot.log` com o seguinte formato:
```
[data] - [mensagem]
```

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 