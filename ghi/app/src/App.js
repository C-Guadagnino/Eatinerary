import { useState } from 'react';
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useToken } from './authApi';
import Nav from "./Nav"
import Login from "./users/Login"
import SignUp from "./users/SignUp"
import Logout from "./users/Logout"
import EateryDetailPage from "./eatery-components/EateryDetailPage"
import MySkeweredList from "./foodies/MySkeweredList"
import MySkeweredHistory from "./foodies/MySkeweredHistory"
import CreateReview from "./foodies/CreateReview"
import ShowReview from "./foodies/ShowReview"
import HomePageWithCards from "./homePageComponents/HomePageWithCards"
import SpecialDateForm from "./foodies/SpecialDateForm"
import './App.css';



function App() {
  const [token, login, logout, signup, user] = useToken();
  const [userName, setUserName] = useState('');

  if (user && !userName) {
    setUserName(user.username)
  }

  // This is so we can track which and if a user is logged in and their sessions is current
  // console.log("userName is:", userName);
  // console.log("user is:", user)
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, '');
  return (
    <BrowserRouter basename={basename}>
      <Nav token={token} />
      <div className='container-fluid p-0'>
        <Routes>
          <Route path="/eatery/:eateryID" element={<EateryDetailPage username={userName} />} />
          <Route path="/" element={<HomePageWithCards username={userName} />} />
          <Route Path='users'>
            <Route path='login' element={<Login token={token} login={login} setUN={setUserName} />} />
            <Route path='logout' element={<Logout logout={logout} />} />
            <Route path='signup' element={<SignUp token={token} signup={signup} setUN={setUserName} />} />
          </Route>
          <Route path='specialdateform' element={<SpecialDateForm username={userName} />} />
          <Route path='myskewered' element={<MySkeweredList username={userName} />} />
          <Route path='myskeweredhistory' element={<MySkeweredHistory username={userName} />} />
          <Route path='review' element={<CreateReview username={userName} />} />
          <Route path='showreview' element={<ShowReview username={userName} />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
export default App;
