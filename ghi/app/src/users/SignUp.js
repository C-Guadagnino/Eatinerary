import React, { useState } from "react";
import { Navigate, NavLink } from "react-router-dom";
import {
  CardWrapper,
  CardHeader,
  CardHeading,
  CardBody,
  CardIcon,
  CardFieldset,
  CardInput,
  CardButton,
  CardLink,
} from "./Card";

function SignUp(props) {
  const {token, signup} = props;
  const [username, setUsername] = useState('');
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');
  const [password, setPassword] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  if (token) {
    return <Navigate to="/" />;
  }
  return (
    <CardWrapper>
      <CardHeader>
        <CardHeading>Sign up</CardHeading>
      </CardHeader>
      <CardBody>
        <CardFieldset>
          <CardInput onChange={e => setUsername(e.target.value)} value={username} placeholder="Username" type="text" required />
        </CardFieldset>

        <CardFieldset>
          <CardInput onChange={e => setFirstName(e.target.value)} value={first_name} placeholder="First Name" type="text" required />
        </CardFieldset>

        <CardFieldset>
          <CardInput onChange={e => setLastName(e.target.value)} value={last_name} placeholder="Last Name" type="text" required />
        </CardFieldset>

        <CardFieldset>
          <CardInput onChange={e => setEmail(e.target.value)} value={email} placeholder="Email" type="email" required />
        </CardFieldset>

        <CardFieldset>
          <CardInput onChange={e => setPhone(e.target.value)} value={phone} placeholder="Phone" type="text" required />
        </CardFieldset>

        <CardFieldset>
          <CardInput onChange={e => setPassword(e.target.value)} value={password} placeholder="Password" type="password" required />
          <CardIcon className="fa fa-eye" eye small />
        </CardFieldset>

        <CardFieldset>
          <CardButton onClick={() => signup(username, email, phone, password, first_name, last_name)} type="button">Create account</CardButton>
        </CardFieldset>
        <CardFieldset>
          <NavLink to="/login">
            <CardLink>I already have an account</CardLink>
          </NavLink>
        </CardFieldset>
      </CardBody>
    </CardWrapper>
  );
}

export default SignUp;

