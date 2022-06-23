import React from "react";
import { NavLink } from "react-router-dom";
import "./Nav.css";
import { useToken } from "./authApi";
import { useState, useEffect } from "react";
import App from "./App";
import skewerednobg from "./images/skewered.png"


export const loggedinLinks = [
  // foodies
  { name: "Skewered", path:"/mySkewered"},
  { name: "History", path: "/mySkeweredHistory"},
  { name: "Review", path: "/review"},
  { name: "ShowReview", path: "/showreview"},
  { name: "Skewered Eateries!", path: "/skewered"},
  // owners
  // eateries
  { name: "Logout", path: "/logout"},
]

export const loggedoutLinks = [
  { name: "Login", path: "/login" },
  { name: "Sign Up", path: "/signup" },
]

const classesIfLoggedIn = "navbar-nav";
const classesIfNotLoggedIn = "navbar-nav";


function Nav(props) {
    const links = props.token ? loggedinLinks : loggedoutLinks;
    return (
      <nav className='navbar navbar-expand-md fixed-top color-nav'>
        <div className='container-fluid'>
          <NavLink className='text-decoration-none' to='/'>
            <h2 className='navbar-brand text-uppercase fs-2'>
              <img src={ skewerednobg } height="60" alt="uh-oh"/>
              {/* What this is doing is creating a link back using the Eatinerary Button */}
            </h2>
          </NavLink>
          <div className='collapse navbar-collapse' id='navbarCollapse'>
            <ul
              className={props.token ? classesIfLoggedIn : classesIfNotLoggedIn}
            >
              {links.map((link, index) => (
                <NavLink key={index} to={link.path}>
                  <button className='btn button-39 me-3'>
                    {link.name}
                  </button>
                </NavLink>
              ))}
            </ul> 
          </div>
        </div>
      </nav>
    );
  }
  
  export default Nav;
  