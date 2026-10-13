import SwiftUI

struct SignalsView: View {
    let signals = [
        ("BTCUSDT", "BUY", 88, "Bullish breakout"),
        ("ETHUSDT", "SELL", 72, "Momentum fading"),
        ("SOLUSDT", "HOLD", 52, "Neutral range")
    ]

    var body: some View {
        NavigationStack {
            List {
                ForEach(signals, id: \ .0) { symbol, signal, confidence, reason in
                    VStack(alignment: .leading, spacing: 6) {
                        HStack {
                            Text(symbol)
                                .font(.headline)
                            Spacer()
                            Text(signal)
                                .bold()
                                .foregroundStyle(signal == "BUY" ? .green : signal == "SELL" ? .red : .orange)
                        }
                        Text("Confidence: \(confidence)%")
                            .foregroundStyle(.secondary)
                        Text(reason)
                            .foregroundStyle(.secondary)
                    }
                    .padding(.vertical, 8)
                }
            }
            .navigationTitle("Signals")
        }
    }
}

#Preview {
    SignalsView()
}
