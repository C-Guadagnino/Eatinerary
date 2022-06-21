// import { useState } from 'react';
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useToken } from './authApi';
import Nav from "./Nav"
import Login from "./users/Login"
import SignUp from "./users/SignUp"
import Logout from "./users/Logout"
import HomePage from "./HomePage"
import MySkeweredList from "./foodies/MySkeweredList"
import MySkeweredHistory from "./foodies/MySkeweredHistory"
import CreateReview from "./foodies/CreateReview"
// import Footer from "./Footer"
import './App.css';

function App() {
  const [token, login, logout, signup] = useToken();

  return (
    <BrowserRouter>
      <Nav token={token} />
      <div className='container-fluid p-0'>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route Path='users'>
            <Route path='login' element={<Login token={token} login={login} />} />
            <Route path='logout' element={<Logout logout={logout} />} />
            <Route
              path='signup'
              element={<SignUp token={token} signup={signup} />}
            />
          </Route>
            <Route path='mySkewered' element={<MySkeweredList />} />
            <Route path='mySkeweredHistory' element={<MySkeweredHistory />} />
            <Route path='review' element={<CreateReview />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
export default App;

