import { useNavigate } from 'react-router-dom'
import { yupResolver } from "@hookform/resolvers/yup"
import * as yup from "yup"
import { useForm } from "react-hook-form"
import { MdEmail, MdLock } from "react-icons/md";
import { api } from "../../server/api"




import { Input } from "../../components/Input/index"
import { Button } from "../../components/Button/index"
import { 
    Container,
    Wrapper,
    Column,
    Row,
    EsqueciText,
    CriarText,
    SubTitleLogin,
    TitleLogin,
} from "./styles"

const schema = yup.object({
    
    email: yup.string().min(1,'email não é valido').required('Campo obrigatório'),
                      // email('email não é valido').required('Campo obrigatório')
    password: yup.string().min(1,'No minimo 3 caracteres').required('Campo obrigatório'),
  }).required()


const Login = () => {
    const navigate = useNavigate();
    
    const { control, handleSubmit, formState: { errors },} = useForm({
        resolver: yupResolver(schema),
        mode: 'onChange'
    });
    
    const onSubmit = async formData => {
        try {
            const response = await api.post(`acoout/api/v1/login/`, {
                email: formData.email,
                password: formData.password
            });
            // Verifique se o status da resposta é 200 
            if (response.status === 200) {
                // Armazene o token (se a API retornar um) e redirecione
                localStorage.setItem('access_token', response.data.access);
                localStorage.setItem('refresh_token', response.data.refresh); 
                navigate('/home');
            } else {
                alert('Email ou senha está errado');
            }
        } catch (error) {
            console.error("Erro no login:", error);
            alert("Houve um erro, tente novamente");
        }
    };
    // navigate('/login')

    return (
        <>
          <Container>
           <Column> 
             <Wrapper>
                <TitleLogin>Faça seu cadastro</TitleLogin>
                <SubTitleLogin>Faça seu login</SubTitleLogin>
                <form  onSubmit={handleSubmit(onSubmit)}> 
                    <Input 
                        name="email" 
                        errorMessage={errors?.email?.message} 
                        control={control} 
                        placehotder="E-mail" 
                        leftIcon={<MdEmail />}
                    />
                    <Input 
                        name="password"
                        errorMessage={errors?.password?.message}
                        control={control} placehotder="Senha"
                        type="password" 
                        leftIcon={<MdLock />} 
                    />
                    <Button 
                        title="Entrar"
                        variant="secondary" 
                        type="submit" 
                    />
                </form>
                <Row>
                    <CriarText>Criar uma nova Senha</CriarText>
                    <EsqueciText>Esquici A senha</EsqueciText>
                </Row>
             </Wrapper>
          </Column>  
         </Container>
        </>)
}

export { Login };