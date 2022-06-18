import React, { useState } from "react";
import { Navigate } from "react-router-dom";
import {
  CardWrapper,
  CardHeader,
  CardHeading,
  CardBody,
  CardIcon,
  CardFieldset,
  CardInput,
  CardButton,
} from "./Card";

function Login(props) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const { login, token } = props;


    if (token) {
        return <Navigate to='foodies/reviews' />;
    }

    return (
        <div className='App'>
          <CardWrapper>
            <CardHeader>
              <CardHeading>Sign in</CardHeading>
            </CardHeader>

            <CardFieldset>
                <CardInput
                  onChange={e => setPassword(e.target.value)}
                  value={password}
                  placeholder='Password'
                  type='password'
                  required
                />
                <CardIcon className='fa fa-eye' eye small />
              </CardFieldset>
            <CardBody>
              <CardFieldset>
                <CardInput
                  onChange={e => setUsername(e.target.value)}
                  value={username}
                  placeholder='Username'
                  type='text'
                  required
                />
              </CardFieldset>
    
              <CardFieldset>
                <CardInput
                  onChange={e => setPassword(e.target.value)}
                  value={password}
                  placeholder='Password'
                  type='password'
                  required
                />
                <CardIcon className='fa fa-eye' eye small />
              </CardFieldset>
              
              <CardFieldset>
                <CardButton onClick={() => login(username, password)} type='button'>
                  Sign Up
                </CardButton>
              </CardFieldset>
            </CardBody>
          </CardWrapper>
        </div>
      );
    }
    
    export default Login;
    