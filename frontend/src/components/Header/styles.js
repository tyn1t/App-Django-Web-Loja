import styled from "styled-components";

export const HeaderContainer = styled.header`
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 90px;
  background-color: blue; 
  align-items: center;
`;

export const UserPicture = styled.img`
  width: 32px;
  height: 32px;
  border-radius: 22px;  
  border: 2px solid;    
`;

export const Row = styled.div`
  display: flex;
  flex-direction: row;
  margin-left: 35px;
  padding: 20px; 
  text-align: center;
  align-items: center;
`;

export const Input = styled.input`
  width: 600px; 
  height: 35px;
  background: white;
  border-radius: 8px;
  padding: 2px 5px;  
  margin: 0 12px;  
  border: 0;

  display: flex; 
  align-items: center; 

  font-size: 24px; 
  font-family: Georgia, 'Times New Roman', Times, serif;
`;

export const Menu = styled.a`
  font-family: 'Open Sans';
  font-style: normal; 
  font-size: 30px;    
  line-height: 25px; 
  color: white;
  margin-right: 12px;   
  margin-left: 30px;    
  text-decoration: none;

  &:hover {
    color: rgba(12, 100, 10, 0.1);
  }
`;