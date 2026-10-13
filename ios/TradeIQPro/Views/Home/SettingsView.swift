import SwiftUI

struct SettingsView: View {
    var body: some View {
        NavigationStack {
            List {
                Section("Account") {
                    Text("Profile")
                    Text("Security")
                    Text("API Keys")
                }
                Section("Trading") {
                    Text("Risk Settings")
                    Text("Alerts")
                    Text("Strategy")
                }
                Section("Subscription") {
                    Text("Premium Plan")
                    Text("Billing")
                    Text("Support")
                }
            }
            .navigationTitle("Settings")
        }
    }
}

#Preview {
    SettingsView()
}
