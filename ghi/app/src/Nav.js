import React from "react";
import { NavLink } from "react-router-dom";
import "./Nav.css";
import { useToken } from "./authApi";
import { useState, useEffect } from "react";
import App from "./App";
import skewerednobg from "./images/skewered.png"

export const loggedinLinks = [
  // foodies
  { name: "My Skewered Eateries", path:"/mySkewered"},
  // { name: "History", path: "/mySkeweredHistory"},
  // { name: "Write a Review", path: "/review"},
  { name: "My Reviews", path: "/showreview"},
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
              <img src={ skewerednobg } height="50" alt="uh-oh"/>
              {/* What this is doing is creating a link back using the Eatinerary Button */}
            </h2>
          </NavLink>
          <div className='collapse navbar-collapse' id='navbarCollapse'>
            <ul
              className={props.token ? classesIfLoggedIn : classesIfNotLoggedIn}
            >
              {links.map((link, index) => (
                <NavLink key={index} to={link.path}>
                  <button className='btn button-39 mx-5'>
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
  