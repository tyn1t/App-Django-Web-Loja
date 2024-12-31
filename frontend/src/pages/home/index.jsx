// import { useNavigate } from 'react-router-dom'
import React, { useState, useEffect } from 'react';

import { Header } from '../../components/Header'
import { ProductCard } from '../../components/Produto';
import { Container, ItemsContainer} from './styles';
import { Menu } from '../../components/Menu';
export const Home = () => {
    
    // const navigate = useNavigate();
    const [products, setProduct] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError]  = useState(null)

    //  Api Publica accs
    useEffect(() => {
        fetch('http://localhost:8000/loja/api/v1/product/')
        .then(response => {
            if(!response.ok){
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json()
        })
        .then(data => {
            setProduct(data)
            setLoading(false)
        })
        .catch(erro => {
            setError(erro)
            setLoading(false)
        })
       
    },[]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    
    return (
        <>
            <Header />
            <Container>
                <div>
                    <Menu />
                </div>
                <div>
                    <ItemsContainer>
                        {products.map(product => ( 
                            <ProductCard key={product._id} product={product} /> 
                        ))}
                    </ItemsContainer>
                </div>
            </Container>
        </>
    );
};

