import {BrowserRouter as Router, Routes, Route } from 'react-router-dom'



import { Login } from './pages/Login/index';
import { Home } from './pages/home';

// App r
const  App = () => { 
  return (
    <Router>
      <Routes>
        <Route path="/acoout/api/v1/login/" element={<Login/>}/>
        <Route path='' element={<Home/>}/>
      </Routes>
    </Router>
   
  );
}

export default App;
