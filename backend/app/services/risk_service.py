from app.services.strategy_service import StrategyEngine
from app.services.binance_service import BinanceService

class RiskManager:
    def __init__(self):
        self.strategy = StrategyEngine()
        self.binance = BinanceService()

    def position_size(self, balance_usdt: float, current_price: float, risk_percent: float = 1.0):
        risk_amount = balance_usdt * (risk_percent / 100)
        return risk_amount / current_price

    def evaluate_trade(self, entry_price: float, current_price: float, stop_loss_percent: float = 2.5, take_profit_percent: float = 5.0):
        variance = ((current_price - entry_price) / entry_price) * 100
        if variance <= -stop_loss_percent:
            return {"action": "SELL", "reason": "stop_loss", "variance": variance}
        if variance >= take_profit_percent:
            return {"action": "SELL", "reason": "take_profit", "variance": variance}
        return {"action": "HOLD", "reason": "normal", "variance": variance}
