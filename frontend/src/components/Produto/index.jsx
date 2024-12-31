import React from "react";
import {CardContainer, Link, Image, Content, Title, Price } from "./styles";


export const ProductCard = ({ product }) => {
    return (
        <CardContainer>
            <Link href={`/produtos/${product._id}`}>
                <Image src={product.image} alt={product.name} />
                <Content>
                    <Title>{product.name}</Title>
                    <Price>${product.price}</Price>
    
                </Content>
            </Link>
        </CardContainer>
    );
};