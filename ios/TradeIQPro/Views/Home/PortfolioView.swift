import SwiftUI

struct PortfolioView: View {
    let positions = [
        ("BTCUSDT", "0.02", "$45,200", "+$420"),
        ("ETHUSDT", "0.50", "$2,550", "+$90"),
        ("SOLUSDT", "10.00", "$142", "+$18")
    ]

    var body: some View {
        NavigationStack {
            List {
                Section("Summary") {
                    Text("Total Value: $125,000")
                    Text("24h PnL: +3.25%")
                    Text("Win Rate: 62%")
                }

                Section("Positions") {
                    ForEach(positions, id: \ .0) { symbol, qty, price, pnl in
                        HStack {
                            Text(symbol)
                                .bold()
                            Spacer()
                            VStack(alignment: .trailing) {
                                Text(qty)
                                Text(pnl)
                                    .foregroundStyle(.green)
                            }
                        }
                    }
                }
            }
            .navigationTitle("Portfolio")
        }
    }
}

#Preview {
    PortfolioView()
}
