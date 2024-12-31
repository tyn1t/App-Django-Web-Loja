import styled from "styled-components";



export const Container = styled.div`
      display: flex;
      flex-direction: row;
`

export const CardContainer = styled.div`
    width: 300px;
    border: 2px solid #000;
    border-radius: 10px;
    overflow: hidden;
    margin: 10px;
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
    background-color: #fff;
    transition: transform 0.2s ease;

    &:hover {
        transform: scale(1.05);
        box-shadow: 7px 7px 15px rgba(0, 0, 0, 0.3);
    }
`;

export const Image = styled.img`
    width: 100%;
    height: 200px; 
    object-fit: cover;
`;

export const Content = styled.div`
    padding: 16px;
`;

export const Title = styled.h3`
    margin-bottom: 8px;
    font-size: 1.2rem;
`;

export const Price = styled.p`
    font-weight: bold;
    margin-bottom: 8px;
`;

export const Link = styled.a`
   text-decoration: none;
   
`