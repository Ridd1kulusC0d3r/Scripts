require 'net/http'

def search_web_data(url, data_type, file_type)
    uri = URI("#{url}?data_type=#{data_type}&file_type=#{file_type}")
    response = Net::HTTP.get(uri)
    return response
end

print "Digite a URL: "
url = gets.chomp
print "Digite o tipo de dado: "
data_type = gets.chomp
print "Digite o tipo de arquivo: "
file_type = gets.chomp

result = search_web_data(url, data_type, file_type)
puts result
