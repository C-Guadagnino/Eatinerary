import './App.css';
import { useState, useEffect } from 'react'
import axios from 'axios'
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


function HomePage() {
  //creating IP state
  const [ip, setIP] = useState('');
  const [eateries, setEateries] = useState([]);
  //creating function to load ip address from the API
  const getData = async () => {
    const res = await axios.get('http://ip-api.com/json/')
    console.log(res.data);
    setIP(res.data.city)
    const data = await axios.get(`http://localhost:8090/api/yelp/${res.data.city}/all`)
    console.log("DATA.DATA", data.data);
    let eateries = []
    for (let eatery of data.data.eateries.businesses) {
      let eatery_dict = {
        "name": eatery.name,
        "image_url": eatery.image_url,
        "address1": eatery.location.address1,
        "city": eatery.location.city,
        "state": eatery.location.state,
        "zip_code": eatery.location.zip_code
      }
      eateries.push(eatery_dict)
    }
    setEateries(eateries)
    console.log("EATERIES", eateries)
  }



  useEffect(() => {
    //passing getData method to the lifecycle method
    //if we get IP data send location to Yelp API
    getData()
  }, [])

    return (
      <div className='App'>
          <CardWrapper>
            <CardHeader>
              <CardHeading>
              {eateries.map(eatery => {
            return (
              <p>
                {eatery.name}  
              </p>
              );
            })}
            </CardHeading>
            </CardHeader>
            <CardBody>
              Hello
            </CardBody>
          </CardWrapper>
        </div>

      // <div className="App">
      //   <h2>Your Live in</h2>

      //   <h4>{ip}</h4>
      // </div>
    );
  }

  export default HomePage;