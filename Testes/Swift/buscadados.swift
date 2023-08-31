import Foundation

func searchWebData(url: String, data_type: String, file_type: String) -> String? {
    guard let url = URL(string: "\(url)?data_type=\(data_type)&file_type=\(file_type)") else { return nil }
    do {
        let response = try String(contentsOf: url)
        return response
    } catch {
        print(error.localizedDescription)
        return nil
    }
}

print("Digite a URL: ", terminator: "")
if let url = readLine(), !url.isEmpty {
    print("Digite o tipo de dado: ", terminator: "")
    if let data_type = readLine(), !data_type.isEmpty {
        print("Digite o tipo de arquivo: ", terminator: "")
        if let file_type = readLine(), !file_type.isEmpty {
            if let result = searchWebData(url: url, data_type: data_type, file_type: file_type) {
                print(result)
            }
        }
    }
}
