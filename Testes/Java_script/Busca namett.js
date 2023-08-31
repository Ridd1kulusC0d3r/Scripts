const axios = require('axios');

async function searchUsername(username) {
  try {
    const response = await axios.get(`https://api.twitter.com/2/users/by/username/${username}`, {
      headers: {
        Authorization: 'Bearer YOUR_TWITTER_API_KEY'
      }
    });

    const userData = response.data;
    return userData;
  } catch (error) {
    console.error('Erro ao buscar usuário:', error);
    return null;
  }
}

// Insira o nome de usuário que deseja pesquisar
const usernameToSearch = 'exemplo';
searchUsername(usernameToSearch)
  .then(userData => {
    if (userData) {
      console.log('Nome:', userData.data.name);
      console.log('Localização:', userData.data.location);
      console.log('Descrição:', userData.data.description);
    } else {
      console.log('Usuário não encontrado ou erro na busca.');
    }
  })
  .catch(error => {
    console.error('Erro na busca:', error);
  });
