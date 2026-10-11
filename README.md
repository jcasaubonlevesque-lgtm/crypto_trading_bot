# Crypto Trading Bot Premium

Bot de trading crypto orienté pro pour un usage en paper trading et en analyse avancée.

Fonctionnalités principales :
- API Binance
- stratégie EMA + MACD + RSI + ATR
- gestion du risque
- backtesting historique
- tableau de bord Streamlit
- logs détaillés
- alertes Telegram optionnelles

## Prérequis

- Python 3.10+
- Compte Binance (optionnel pour données publiques / tests)
- Clés API Binance si tu veux passer en mode réel ensuite

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Copie le fichier d'exemple et renseigne tes variables :

```bash
cp .env.example .env
```

Puis mets tes clés API Binance si tu veux aller plus loin.

## Lancer le bot

```bash
python main.py
```

## Lancer le dashboard

```bash
streamlit run app/dashboard.py
```

## Lancer un backtest

Tu peux utiliser une petite commande Python :

```python
from app.backtest import run_backtest

result = run_backtest(initial_balance=100.0, symbol="BTCUSDT")
print(result)
```

## Points importants

- Ce projet est conçu pour la recherche et l'apprentissage.
- Le mode par défaut est paper trading.
- N'utilise pas d'argent réel sans validation approfondie.
- Le système est extensible pour ajouter des alertes, des stratégies, ou des integrations de trading réel.
