// gabriel_client.js (템플릿)
const axios = require('axios');

async function main() {
  try {
    const response = await axios.get('http://localhost:3000/status');
    console.log('[Gabriel] Server Status:', response.data);
  } catch (err) {
    console.error('[Gabriel] Error communicating with server:', err.message);
  }
}

main();
