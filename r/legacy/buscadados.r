searchWebData <- function(url, data_type, file_type) {
  response <- readLines(paste0(url, "?data_type=", data_type, "&file_type=", file_type))
  return(response)
}

cat("Digite a URL: ")
url <- readline()
cat("Digite o tipo de dado: ")
data_type <- readline()
cat("Digite o tipo de arquivo: ")
file_type <- readline()

result <- searchWebData(url, data_type, file_type)
cat(result, "\n")
