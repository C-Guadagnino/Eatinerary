import { useState } from 'react';
import './App.css';
import { useToken } from './authApi';

function App() {
  const [token, login, logout, signup] = useToken();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [isOwner, setIsOwner] = useState(false);
  const [isFoodie, setIsFoodie] = useState(false);
  const [error, setError] = useState(null);

  return (
    // <BrowserRouter>
    //   <Nav token={token} />
    //   <Routes>
    //     <Route path="" element={<Login token={token} login={login} />} />
    //   </Routes>
    // </BrowserRouter>
    <div>
      { error ? <div dangerouslySetInnerHTML={{__html: error}} /> : null }
      { token
      ? <div>
          <h1>Logout</h1>
          <div>{token}</div>
          <button onClick={logout}>Logout</button>
        </div>
      : <div>
          <h1>Login</h1>
          <div>
          <input type="checkbox" checked={isFoodie} onChange={e => setIsFoodie(e.target.checked)} />
            Is foodie
          </div>
          <div>
            <input type="checkbox" checked={isOwner} onChange={e => setIsOwner(e.target.checked)} />
            Is owner
          </div>
          <input type="text" onChange={e => setUsername(e.target.value)} value={username} placeholder="username" />
          <input type="email" onChange={e => setEmail(e.target.value)} value={email} placeholder="email" />
          <input type="phone" onChange={e => setPhone(e.target.value)} value={phone} placeholder="phone" />
          <input type="password" onChange={e => setPassword(e.target.value)} value={password} placeholder="password" />
          <button onClick={async () => setError(await login(username, password))}>Login</button>
          <button onClick={async () => setError(await signup(username, password, email, phone, isOwner, isFoodie))}>Sign up</button>
        </div>
      }
    </div>
  );
}

export default App;
