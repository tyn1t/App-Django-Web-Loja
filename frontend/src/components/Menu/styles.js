import styled from "styled-components";


export const ContainerMenu = styled.div`
    width: 200px;
    height: 100vh;
    background-color: blue;
    padding: 20px;
`;


export const ListMenu = styled.li`
    color:azure;
    list-style: none;
    font-size: 25px;
    padding: 15px 0; 
    cursor: pointer; 

    &:hover {
        background-color: rgba(0, 0, 0, 0.1);
    }
`;

export const UlMenu = styled.ul`
    padding: 0;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
`;

export const A = styled.a`
    text-decoration: none;
    color: azure; 
    display: block;

    &:hover,
    &:focus { 
      color: aquamarine;
   }
`;