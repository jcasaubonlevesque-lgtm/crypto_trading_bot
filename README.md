# Crypto Trading Bot Pro

Bot de trading crypto en mode paper trading avec :
- API Binance
- stratégie EMA + MACD + RSI
- gestion du risque
- dashboard Streamlit
- backtesting

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Copie le fichier d'exemple et renseigne tes clés Binance si tu souhaites utiliser l'API réelle :

```bash
cp .env.example .env
```

## Lancer le bot

```bash
python main.py
```

## Lancer le dashboard

```bash
streamlit run app/dashboard.py
```

## Important

- Ce projet est destiné à des fins éducatives.
- Le mode par défaut est paper trading.
- N'utilise pas d'argent réel sans validation et tests approfondis.
