import axios from "axios";


export const api = axios.create({
    baseURL: 'http://localhost:8000', 
    timeout: 5000, // Adicione um timeout
});

// Interceptor para adicionar o token JWT às requisições
api.interceptors.request.use(config => {
    const token = localStorage.getItem('access_token');
    if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
}, error => {
    return Promise.reject(error);
});

// Interceptor para lidar com erros de autorização (401)
api.interceptors.response.use(response => {
    return response;
}, error => {
    if (error.response && error.response.status === 401) {
        // Token expirado ou inválido - Redirecionar para login ou atualizar token
    }
    return Promise.reject(error);
});

export const handleError = (error) => {
    console.error("Erro na requisição:", error);
};
