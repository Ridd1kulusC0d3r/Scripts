const axios = require('axios');

async function searchWebData(url, data_type, file_type) {
    const response = await axios.get(`${url}?data_type=${data_type}&file_type=${file_type}`);
    return response.data;
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Digite a URL: ", url => {
    rl.question("Digite o tipo de dado: ", data_type => {
        rl.question("Digite o tipo de arquivo: ", file_type => {
            searchWebData(url, data_type, file_type)
                .then(result => {
                    console.log(result);
                    rl.close();
                })
                .catch(error => {
                    console.error(error);
                    rl.close();
                });
        });
    });
});
