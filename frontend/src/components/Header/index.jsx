import React from "react";
import { HeaderContainer, Input, Menu, Row, UserPicture } from "./styles";

export const Header = () => {
    return (
        <nav>
            <HeaderContainer>
                <Row>
                    <UserPicture/>
             
                   <Input />
                </Row>
                <Row>
                   <Menu href='#'>
                      Melhores Produtcs
                   </Menu>
                   <Menu href='#'>
                      Livros +
                   </Menu>
                   <Menu href='#'>
                      Tv
                   </Menu>
                </Row>
            </HeaderContainer>
        </nav>
    )
}
