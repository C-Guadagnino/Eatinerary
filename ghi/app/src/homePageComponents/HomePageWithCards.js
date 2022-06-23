import React from "react";
import "./Box.css";
import { useState, useEffect } from 'react'
import axios from 'axios'
import { Card } from "react-bootstrap";

const HomePageWithCards = () => {
    //creating IP state
  const [ip, setIP] = useState('');
  const [eateries, setEateries] = useState([]);
  //creating function to load ip address from the API
  const getData = async () => {
    const res = await axios.get('http://ip-api.com/json/')
    console.log(res.data);
    setIP(res.data.city)
    const data = await axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/yelp/${res.data.city}/food/`)
    //Limit this request to 9 results because it takes a long time to populate the page
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
  }
  useEffect(() => {
    //passing getData method to the lifecycle method
    //if we get IP data send location to Yelp API
    getData()
  }, [])
    
  const renderCard = (card, index) => {
        return(
            <Card style={{ width: '18rem' }} key={index} className="box">
                <Card.Img variant="top" src={card.image_url} />
                <Card.Body>
                    <Card.Title>{card.name}</Card.Title>
                    <Card.Text>
                        {card.address1}, {card.city}, {card.state}, {card.zip_code}
                    </Card.Text>
                    {/* <Button variant="primary">Go somewhere</Button> */}
                </Card.Body>
            </Card>

        )
  }

  return (
    <>
      <div className="container my-5 py-3">
        <div className='p-5 text-center'>
            <h1 className='mb-3'>Eatinerary</h1>
            <h4 className='mb-3'>Local Eateries</h4>
          </div>
        </div>
        <div className="container">
          <div className="row justify-content-md-center m-5">
          {eateries.map(renderCard)}
          </div>
      </div>
    </>
  )
}

export default HomePageWithCards;