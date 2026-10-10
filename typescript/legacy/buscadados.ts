import axios from 'axios';
import readline from 'readline';

async function searchWebData(url: string, data_type: string, file_type: string): Promise<string> {
  try {
    const response = await axios.get(`${url}?data_type=${data_type}&file_type=${file_type}`);
    return response.data;
  } catch (error) {
    console.error(error);
    return '';
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Digite a URL: ", url => {
  rl.question("Digite o tipo de dado: ", data_type => {
    rl.question("Digite o tipo de arquivo: ", file
