import styled from 'styled-components'


export const Container = styled.main`
    display: flex;
    flex-direction: row;
    
    width: 25%;
    max-width: 80%;
    margin-top: 120px;
    margin-left: 35%;
    margin-right: 50%;
    justify-content: space-between;
    align-items: center;
`

export const Wrapper = styled.div`
    max-width: 300px;
    border-radius: 2%;
    border: solid 1px gray;
    padding: 5%;
    text-align: center;
    position: absolute;
`
export const Column = styled.div`
    flex: 1;
    padding: 2%;
`

export const Row = styled.div`
    display: flex;
    flex-direction: row;
    justify-content:  space-between;
    align-items: center;
    margin-top: 20px;
    padding: 1%;
`


export const EsqueciText = styled.p`
    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 700;
    font-size: 14px;
   
    line-height: 19px;

    color:  #E5E044;
`
export const CriarText = styled.p`
    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 700;
    font-size: 14px;
    line-height: 19px;
  
    color:  #E23DD7;
`
export const SubTitleLogin = styled.p`
    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 400;
    font-size: 18px;
    margin-bottom: 35px;
    line-height: 25px;
    position: relative;

`

export const TitleLogin = styled.p`
    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 700;
    font-size: 32px;
    width: 320px;
    margin-bottom: 20px;
    line-height: 44px;
    position: relative;

`

export const Title = styled.h2`
    font-family: 'Open Sans';
    font-style: normal;
    font-weight: 700;
    font-size: 32px;
    width: 320px;
    margin-bottom: 20px;
    line-height: 44px;

    color:  #FFFFFF;
`