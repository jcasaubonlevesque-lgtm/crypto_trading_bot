import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            DashboardView()
                .tabItem { Label("Dashboard", systemImage: "chart.line.uptrend.xyaxis") }

            PortfolioView()
                .tabItem { Label("Portfolio", systemImage: "briefcase.fill") }

            SignalsView()
                .tabItem { Label("Signals", systemImage: "waveform.path.ecg") }

            SettingsView()
                .tabItem { Label("Settings", systemImage: "gearshape.fill") }
        }
        .tint(.purple)
    }
}

#Preview {
    ContentView()
}
