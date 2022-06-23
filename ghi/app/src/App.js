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
// import Footer from "./Footer"
import './App.css';



function App() {
  const [token, login, logout, signup, user] = useToken();
  const [userName, setUserName] = useState('');

  if (user && !userName) {
    setUserName(user.username)
  }

  console.log("userName is:", userName);
  console.log("user is:", user)
  return (
    <BrowserRouter>
      <Nav token={token} />
      <div className='container-fluid p-0'>
        <Routes>
          {/* eatery detail page url will need to be dynamic and accept an eatery id value
          path = /eatery/1 */}
          <Route path="/eatery/:eateryID" element={<EateryDetailPage />} />
          <Route path="/" element={<HomePageWithCards />} />
          <Route Path='users'>
            <Route path='login' element={<Login token={token} login={login} setUN={setUserName} />} />
            <Route path='logout' element={<Logout logout={logout} />} />
            <Route path='signup' element={<SignUp token={token} signup={signup} />}/>
          </Route>
          <Route path='specialDateForm' element={<SpecialDateForm username={userName} />} />
          <Route path='mySkewered' element={<MySkeweredList username={userName} />} />
          <Route path='mySkeweredHistory' element={<MySkeweredHistory />} />
          <Route path='review' element={<CreateReview />} />
          <Route path='showreview' element={<ShowReview username={userName} />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
export default App;

