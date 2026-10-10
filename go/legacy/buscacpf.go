package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func searchWebData(url, searchTerm string) ([]string, error) {
	response, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer response.Body.Close()

	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		return nil, err
	}

	data := []string{}
	lines := strings.Split(string(body), "\n")

	for _, line := range lines {
		if strings.Contains(line, searchTerm) {
			data = append(data, line)
		}
	}

	return data, nil
}

func main() {
	// Insira a URL do site e o termo de busca desejado
	urlToSearch := "https://www.exemplo.com"
	searchTerm := "CPF"

	// Realizar a busca e imprimir os resultados
	searchResults, err := searchWebData(urlToSearch, searchTerm)
	if err != nil {
		fmt.Println("Erro ao buscar dados:", err)
		return
	}

	for _, result := range searchResults {
		fmt.Println(result)
	}
}
