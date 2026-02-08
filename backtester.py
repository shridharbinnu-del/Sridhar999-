class SupportResistanceDetector:
    def __init__(self, price_data):
        """Initialize with historical price data."""
        self.price_data = price_data

    def detect_support_resistance(self):
        """Detect support and resistance levels in the provided price data."""
        # For the sake of example, using a simple method to detect levels
        highs = [max(data) for data in self.price_data]
        lows = [min(data) for data in self.price_data]
        resistance = max(highs)
        support = min(lows)
        return support, resistance


class IntraDayBacktester:
    def __init__(self, price_data, strategy):
        """Initialize the backtester with price data and a trading strategy."""
        self.price_data = price_data
        self.strategy = strategy

    def run_backtest(self):
        """Run the backtest using the defined strategy and price data."""
        results = []
        # Here would implement the backtesting logic
        for data in self.price_data:
            # Execute strategy and store results
            outcome = self.strategy.execute(data)
            results.append(outcome)
        return results

# Usage:
# support_detector = SupportResistanceDetector(price_data)
# support, resistance = support_detector.detect_support_resistance()
# backtester = IntraDayBacktester(price_data, some_strategy)
# backtest_results = backtester.run_backtest()