import React from "react";
import {ContainerMenu, ListMenu , UlMenu, A} from './styles';


export const Menu = () => {
    return (
        <>
            <ContainerMenu>
                <UlMenu>
                    <ListMenu><A href='home'>Home</A></ListMenu>
                    <ListMenu><A href='compra'>Compra</A></ListMenu>
                    <ListMenu><A href='login'>Login</A></ListMenu>
                    <ListMenu><A href='Cadastro'>Cadastro</A></ListMenu>
                </UlMenu>
            </ContainerMenu>
        </>
    )
}