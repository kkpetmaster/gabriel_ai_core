const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');

const app = express();
app.use(bodyParser.json());

app.post('/api/from-aiin', (req, res) => {
  const command = req.body.command;
  if (!command) return res.status(400).send('No command provided');

  exec(command, (error, stdout, stderr) => {
    res.json({ stdout, stderr, error: error ? error.message : null });
  });
});

app.listen(3000, () => {
  console.log('✅ Manus Agent Server running on port 3000');
});

app.get('/status', (req, res) => res.json({ status: 'ok', time: new Date().toISOString() }));
