const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Déploiement réussi ! Ton app tourne sur Render 🚀');
});

app.listen(PORT, () => {
  console.log(`Serveur démarré sur le port ${PORT}`);
});
