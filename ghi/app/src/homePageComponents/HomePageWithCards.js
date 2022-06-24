import React from "react";
import "./Box.css";
import { useState, useEffect } from 'react'
import axios from 'axios'
import { Card } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { NavLink, useNavigate } from "react-router-dom";
import EateryDetailPage from "../eatery-components/EateryDetailPage";
import eatineraryheader from "./images/eatineraryheader.png"
import localeateries from "./images/localeateries.png"
import { FaInfo } from "react-icons/fa";
import { GiCupidonArrow } from "react-icons/gi";


const HomePageWithCards = () => {
    //creating IP state
  const navigate = useNavigate()
  const [ip, setIP] = useState('');
  const [eateries, setEateries] = useState([]);
  // const [searchEateries, setFilteredResults] = useState([]);
  //creating function to load ip address from the API
  const getData = async () => {
    const res = await axios.get('http://ip-api.com/json/')
    // console.log("IP INFO", res.data.city);
    setIP(res.data.city)
    const data = await axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/yelp/${res.data.city}/food/`)
    //Limit this request to 9 results because it takes a long time to populate the page
    const realEateries = await axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/city/filter/${res.data.city}/`)
    // console.log("DATABASE EATERIES", realEateries.data);
    let eateries = []
    for (let eatery of realEateries.data) {
      // console.log("EATERIES", eatery)
      let eatery_dict = {
        "id": eatery.id,
        "eatery_name": eatery.eatery_name,
        "image_url": eatery.eatery_images[0].image_url,
        "address1": eatery.location.address1,
        "city": eatery.location.city,
        "state": eatery.location.state,
        "zip_code": eatery.location.zip_code
      }
      eateries.push(eatery_dict)
    }
    setEateries(eateries)
    // console.log("EATERIES", eateries)
  }
  useEffect(() => {
    //passing getData method to the lifecycle method
    //if we get IP data send location to Yelp API
    getData()
  }, [])
  // const getDetailPage = props => {
  //   const [eateryIdentifier, setEateryIdentifier] = useState(props)
  // }
  function detailOnClick(eatery) {
    const eateryID = eatery.id
    navigate(`/eatery/${eateryID}`)
  }

  const [locationState, setLocation] = useState('')
  const [categoryState, setCategory] = useState('food')
  const [searchInput, setSearchInput] = useState('');

  const handleLocationChange = (e) => {
    e.preventDefault();
    setLocation(e.target.value);
  };
  // .replaceAll(" ","+")
  const handleCategoryChange = (e) => {
    e.preventDefault();
    setCategory(e.target.value.replaceAll(" ",""));
  };

  async function handleSearch() {
    console.log("!!!!!", locationState)
    console.log("!!!!!", categoryState)
    const searchData = await axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/yelp/${locationState}/${categoryState}/`)
    // console.log("SEARCH DATA:", searchData.data.eateries.businesses)
    const allEateries = await axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/filtered/${locationState}/${categoryState}/`)
    // console.log("SEARCH DATA:", allEateries.data.eateries)
    // if (allEateries.data.eateries.length > 0) {
    //   const searchEateries = allEateries.data.eateries.filter((eatery) => {
    //   return eatery.name.match(locationState) ;
    // });
    // }
    // setFilteredResults(searchEateries)
    let eateries = []
    for (let eatery of allEateries.data) {
      // console.log("EATERIES", eatery)
      let eatery_dict = {
        "id": eatery.id,
        "eatery_name": eatery.eatery_name,
        "image_url": eatery.eatery_images[0].image_url,
        "address1": eatery.location.address1,
        "city": eatery.location.city,
        "state": eatery.location.state,
        "zip_code": eatery.location.zip_code
      }
      eateries.push(eatery_dict)
    }
    setEateries(eateries)
    // setState({filteredAppointments: searchData})  
  }

  const renderCard = (card, index) => {
    // console.log("CARD", card)
        return(

            // <Card border="success" style={{ width: '17rem' }} key={index} className="box">
            <Card style={{ width: '18rem' }} key={index} className="container mt-4 mb-4 mx-3 border-0">
                <Card.Img className="image-container mt-3" style={{objectFit: "cover"}} src={card.image_url} />


                <Card.Body>
                    <Card.Title>{card.eatery_name}</Card.Title>
                    <Card.Text>
                        {card.address1}, {card.city}, {card.state}, {card.zip_code}
                    </Card.Text>
      
                    <Button id="button-38" onClick={detailOnClick.bind(this,card)}> <FaInfo size="1.5em" /> </Button><Button id="button-38" onClick={detailOnClick.bind(this,card)}> <GiCupidonArrow size="1.5em" /> </Button>
                    {/* Revisit and look into bind documentation for more details - ANOTHER ALTERNATIVE:
                    () => detailOnClick(card) */}
                </Card.Body>
            </Card>
        )
  }

  return (
    <>
      <div className="container my-5 py-3">
        <div className='p-5 text-center'>
        <h1><img src={ eatineraryheader } height="140" alt="uh-oh"/></h1>
          <img src={ localeateries } height="35" alt="uh-oh"/>
            <p>  </p>
            <p> Search bar here </p>
          </div>
        </div>
        <div className="container">
          <div className="row justify-content-md-center m-5">
          {eateries.map(renderCard)}
          </div>
      </div>

      <form>
        <div className="innerform">
          <div className="input-field first-wrap">
            <input onChange={handleCategoryChange}id="search" type="text" placeholder="What type of cuisine are you looking for?"/>
          </div>
          <div className="input-field second-wrap">
            <input onChange={handleLocationChange}id="search" type="text" placeholder="What city are you looking in?"/>
          </div>
          <div className="input-field third-wrap">
            <button onClick={() => handleSearch()} className="btn-search" type="button">Search</button>
          </div>
        </div>
        </form>
        </>
  )
}

export default HomePageWithCards;