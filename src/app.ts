import express from 'express';
import { json } from 'body-parser';
import { routes } from './routes'; // Asegúrate de crear este archivo para definir las rutas

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(json());

// Rutas
app.use('/api', routes); // Asegúrate de definir las rutas en el archivo correspondiente

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});