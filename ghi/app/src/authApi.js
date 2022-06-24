import { useEffect, useState } from "react";
let internalToken = null;

export function getToken() {
  return internalToken;
}

async function getTokenInternal() {
  const url = `${process.env.REACT_APP_ACCOUNT_API}/api/users/me/token/`;
  try {
    const response = await fetch(url, {
      credentials: 'include',
    });
    if (response.ok) {
      const data = await response.json();
      internalToken = data.token;
      return internalToken;
    }
  } catch (e) { }
  return false;
}


async function getCurrentUser() {
  const url = `${process.env.REACT_APP_ACCOUNT_API}/api/users/me/`;
  try {
    const response = await fetch(url, {
      credentials: 'include',
    });
    if (response.ok) {
      const data = await response.json();
      return data;
    }
  } catch (e) { }
  return false;
}


function handleErrorMessage(error) {
  if ("error" in error) {
    error = error.error;
    try {
      error = JSON.parse(error);
      if ("__all__" in error) {
        error = error.__all__
      }
    } catch { }
  }
  if (Array.isArray(error)) {
    error = error.join("<br>");
  } else if (typeof (error) === "object") {
    error = Object.entries(error).reduce((acc, x) => `${acc}<br>${x[0]}: ${x[1]}`, '');
  }
  return error;
}

export function useToken() {
  const [token, setToken] = useState(null);
  const [user, setUser] = useState(null);
  useEffect(() => {
    async function fetchToken() {
      const token = await getTokenInternal();
      setToken(token);
      const userData = await getCurrentUser();
      setUser(userData);
    }
    if (!token) {
      fetchToken();
    }
  }, [token]);

  async function logout() {
    if (token) {
      const url = `${process.env.REACT_APP_ACCOUNT_API}/api/token/refresh/logout/`;
      await fetch(url, { method: 'delete', credentials: 'include' });
      internalToken = null;
      setToken(null);
    }
  }

  async function login(username, password) {
    const url = `${process.env.REACT_APP_ACCOUNT_API}/login/`;
    const form = new FormData();
    form.append('username', username);
    form.append('password', password);
    const response = await fetch(url, {
      method: 'post',
      credentials: 'include',
      body: form,
    });
    if (response.ok) {
      const token = await getTokenInternal();
      setToken(token);
      return;
    }
    let error = await response.json();
    return handleErrorMessage(error);
  }

  async function signup(username, password, email, phone, first_name, last_name, is_owner, is_foodie) {
    const url = `${process.env.REACT_APP_ACCOUNT_API}/api/users/`;
    const response = await fetch(url, {
      method: 'post',
      body: JSON.stringify({ username, password, email, first_name, last_name, phone, is_owner, is_foodie }),
      headers: {
        'Content-Type': 'application/json',
      }
    });
    if (response.ok) {
      return await login(username, password);
    }
    return handleErrorMessage(await response.json());
  }

  return [token, login, logout, signup, user];
}
