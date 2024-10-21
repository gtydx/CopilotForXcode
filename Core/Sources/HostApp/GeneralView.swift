import ComposableArchitecture
import SwiftUI

struct GeneralView: View {
    let store: StoreOf<General>
    @StateObject private var viewModel = GitHubCopilotViewModel()
  
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 0) {
                generalView.padding(20)
                Divider()
                rightsView.padding(20)
            }
            .frame(maxWidth: .infinity)
        }
        .task {
            if isPreview { return }
            viewModel.checkStatus()
            await store.send(.appear).finish()
        }
    }

    private var generalView: some View {
        VStack(alignment: .leading, spacing: 30) {
            AppInfoView(viewModel: viewModel, store: store)
            GeneralSettingsView(store: store)
            CopilotConnectionView(viewModel: viewModel, store: store)
        }
    }

    private var rightsView: some View {
        Text("GitHub. All rights reserved.")
            .font(.caption2)
            .foregroundColor(.secondary.opacity(0.5))
    }
}

#Preview {
    GeneralView(store: .init(initialState: .init(), reducer: { General() }))
        .frame(width: 800, height: 600)
}
