import './App.css';
import {useState,useEffect} from 'react'
import axios from 'axios'

function HomePage() {
  //creating IP state
  const [ip, setIP] = useState('');

  //creating function to load ip address from the API
  const getData = async () => {
    const res = await axios.get('http://ip-api.com/json/')
    console.log(res.data);
    setIP(res.data.city)
  }

  // const getYelpData = async () => {
  //   const data = await axios.get('http://ip-api.com/json/')
  //   console.log(res.data);
  //   setIP(res.data.city)
  // }
  
  useEffect( () => {
    //passing getData method to the lifecycle method
    getData()

  }, [])

  return (
    <div className="App">
      <h2>Your Live in</h2>
      <h4>{ip}</h4>
    </div>
  );
}

export default HomePage;