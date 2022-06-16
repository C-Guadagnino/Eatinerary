// import { useState } from 'react';
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useToken } from './authApi';
import Nav from "./Nav"
import Login from "./users/Login"
import SignUp from "./users/SignUp"
import Logout from "./users/Logout"
import HomePage from "./HomePage"
import Footer from "./Footer"
import './App.css';

function App() {
  const [token, login, logout, signup] = useToken();

  return (
    <BrowserRouter>
      <Nav token={token} />
      <div className='container-fluid p-0'>
        <Routes>
          <Route Path='users'>
            <Route path='login' element={<Login token={token} login={login} />} />
            <Route path='logout' element={<Logout logout={logout} />} />
            <Route
              path='signup'
              element={<SignUp token={token} signup={signup} />}
            />
          </Route>
        </Routes>
      </div>
      {/* <div className='footer-container'>
        <Footer />
      </div> */}
    </BrowserRouter>
  );
}
export default App;

