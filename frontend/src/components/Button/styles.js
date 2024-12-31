import  styled, { css } from "styled-components";


export const ButtonContainer = styled.button`
   background: #565656;
   border-radius: 22px;
   position: relative;

   color: #000000;
   padding: 2px 12px;
   font-size: large;
   min-width: 102px;
   width: 100%;

   ${({variant}) => variant !== "primary" && css`
       min-width: 167px;
       height: 33px;

       background: #E5E044;

       &:hover {
        opacity: 0.6;
        cursor: pointer;
       }
       &::after {
        content: '';
        position: absolute;
        border: 1px;
        top: -5px;
        left: -6px;
        width: calc(100% + 10px);
        height: calc(100% + 10px);
        border-radius: 22px;
       }

   `}
`