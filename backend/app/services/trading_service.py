from typing import Dict, Any

from app.services.binance_service import BinanceService
from app.services.strategy_service import StrategyEngine
from app.services.risk_service import RiskManager


class TradingService:
    def __init__(self):
        self.binance = BinanceService()
        self.strategy = StrategyEngine()
        self.risk = RiskManager()

    def get_signal_for_symbol(self, symbol: str = "BTCUSDT") -> Dict[str, Any]:
        try:
            candles = self.binance.get_klines(symbol=symbol, interval="15m", limit=200)
            signal = self.strategy.generate_signal(candles)
            price = self.binance.get_price(symbol=symbol)
            signal["symbol"] = symbol
            signal["price"] = price
            return signal
        except Exception as exc:  # pragma: no cover - fallback safe behavior
            return {
                "symbol": symbol,
                "action": 0,
                "confidence": 0.0,
                "reason": f"Market data unavailable: {str(exc)}",
                "price": 0.0,
            }

    def get_portfolio_snapshot(self, balance_usdt: float = 100.0) -> Dict[str, Any]:
        demo_positions = [
            {"symbol": "BTCUSDT", "quantity": 0.02, "entry_price": 45000.0, "current_price": 47000.0, "pnl": 400.0, "pnl_percent": 4.2},
            {"symbol": "ETHUSDT", "quantity": 0.50, "entry_price": 2500.0, "current_price": 2600.0, "pnl": 50.0, "pnl_percent": 2.0},
        ]
        total_value = sum((p["quantity"] * p["current_price"]) for p in demo_positions) + balance_usdt
        pnl_24h = sum(p["pnl"] for p in demo_positions)
        return {
            "balance_usdt": balance_usdt,
            "total_value": total_value,
            "pnl_24h": pnl_24h,
            "pnl_24h_percent": 2.5,
            "positions": demo_positions,
        }
