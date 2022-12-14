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
  const { token, signup } = props;
  const [isFoodie, setIsFoodie] = useState(false);
  const [username, setUsername] = useState('');
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');
  const [password, setPassword] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  if (token) {
    return <Navigate to='/' />;
  }
  var handleUserName = function (e) {
    const value = e.target.value;
    setUsername(value)
    props.setUN(value)
  }
  return (
    <div className="container mt-5 py-5">
      <CardWrapper>
        <CardHeader>
          <CardHeading>Welcome to Eatinerary!</CardHeading>
        </CardHeader>

        <CardBody>
          <CardFieldset>
            <CardBody> Foodie
              <CardInput onChange={e => setIsFoodie(e.target.checked)} checked={isFoodie} placeholder="Foodie?" type="checkbox" />
            </CardBody>
          </CardFieldset>
        </CardBody>

        <CardBody>
          <CardFieldset>
            <CardInput onChange={handleUserName} value={username} placeholder="Username" type="text" required />
          </CardFieldset>

          <CardFieldset>
            <CardInput onChange={e => setPassword(e.target.value)} value={password} placeholder="Password" type="password" required />
            <CardIcon className="fa fa-eye" eye small />
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
            <CardButton onClick={() => signup(username, password, first_name, last_name, email, phone)} type="button">Become A Member</CardButton>
          </CardFieldset>
          <CardFieldset>
            <NavLink to="/login">
              <CardLink>Sign in Here</CardLink>
            </NavLink>
          </CardFieldset>
        </CardBody>
      </CardWrapper>
    </div>
  );
}

export default SignUp;
