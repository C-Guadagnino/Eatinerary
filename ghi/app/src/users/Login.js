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
    return <Navigate to='/' />;
  }
  var handleUserName = function (e) {
    const value = e.target.value;
    setUsername(e.target.value)
    props.setUN(e.target.value)
  }
  return (
    <div className='container mt-5 py-5'>
      <CardWrapper>
        <CardHeader>
          <CardHeading>Sign in</CardHeading>
        </CardHeader>

        <CardBody>
          <CardFieldset>
            <CardInput
              onChange={handleUserName}
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
              Login
            </CardButton>
          </CardFieldset>
        </CardBody>
      </CardWrapper>
    </div>
  );
}

export default Login;
