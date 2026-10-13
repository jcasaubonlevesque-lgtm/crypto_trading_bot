import SwiftUI

struct DashboardView: View {
    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 18) {
                    Text("AVANTOPS AI")
                        .font(.largeTitle)
                        .bold()
                    Text("AI-powered crypto trading intelligence")
                        .font(.subheadline)
                        .foregroundStyle(.secondary)

                    HStack {
                        MetricCard(title: "Portfolio", value: "$124,500")
                        MetricCard(title: "24h PnL", value: "+3.25%")
                    }

                    SignalCard(symbol: "BTCUSDT", action: "BUY", confidence: 88, reason: "Bullish setup")
                    SignalCard(symbol: "ETHUSDT", action: "SELL", confidence: 74, reason: "Bearish continuation")
                    SignalCard(symbol: "SOLUSDT", action: "HOLD", confidence: 53, reason: "Neutral")
                }
                .padding()
            }
            .navigationTitle("Dashboard")
        }
    }
}

struct MetricCard: View {
    let title: String
    let value: String

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(title)
                .font(.caption)
                .foregroundStyle(.secondary)
            Text(value)
                .font(.title3)
                .bold()
        }
        .frame(maxWidth: .infinity, minHeight: 90)
        .padding()
        .background(Color(.secondarySystemBackground))
        .cornerRadius(18)
    }
}

struct SignalCard: View {
    let symbol: String
    let action: String
    let confidence: Int
    let reason: String

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Text(symbol)
                    .font(.headline)
                Spacer()
                Text(action)
                    .bold()
                    .foregroundStyle(action == "BUY" ? .green : action == "SELL" ? .red : .orange)
            }
            Text("Confidence: \(confidence)%")
                .foregroundStyle(.secondary)
            Text(reason)
                .foregroundStyle(.secondary)
        }
        .padding()
        .frame(maxWidth: .infinity)
        .background(Color(.secondarySystemBackground))
        .cornerRadius(18)
    }
}

#Preview {
    DashboardView()
}
