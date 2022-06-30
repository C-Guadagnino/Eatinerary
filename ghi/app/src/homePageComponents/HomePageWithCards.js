import React from "react";
import "./Box.css";
import { useState, useEffect } from 'react'
import axios from 'axios'
import { Card } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import eatineraryheader from "./images/eatineraryheader.png"
import localeateries from "./images/localeateries.png"
import { FaInfo } from "react-icons/fa";
import { GiCupidonArrow } from "react-icons/gi";
import { GiMagnifyingGlass } from "react-icons/gi";
import { MdOutlineDangerous } from "react-icons/md";
import { BsArrow90DegUp } from "react-icons/bs";
import { GrPrevious } from "react-icons/gr";
import { GrNext } from "react-icons/gr";



const HomePageWithCards = (props) => {
  const navigate = useNavigate()
  //creating IP state
  const [eateries, setEateries] = useState([]);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1)
  console.log("PAGE NUMBER", page)
  useEffect(() => {
    //creating function to load ip address from the API
    const getData = async (res, tryNumber) => {
      if (tryNumber > 6) {
        setError("Could not find eateries. Please try again soon.")
        console.error("Could not find eateries");
        return;
      }
      const realEateries = await axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/city/filter/${res.data}/?page=${page}`)
      console.log(realEateries)
      //data.page = page number
      if (!realEateries.data.eateries.length) {
        setTimeout(() => getData(res, tryNumber + 1), 500);
        return;
      }
      let eateries = []
      for (let eatery of realEateries.data.eateries) {
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
    }

    //passing getData method to the lifecycle method
    //if we get IP data send location to Yelp API
    async function getCityAndData() {
      const res = await axios.get('https://ipapi.co/city/')
      axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/yelp/${res.data}/food/`)
      getData(res, 1);
    }

    getCityAndData();
  }, [page])

  function detailOnClick(eatery) {
    const eateryID = eatery.id
    navigate(`/eatery/${eateryID}`)
  }

  const [locationState, setLocation] = useState('')
  const [categoryState, setCategory] = useState('food')

  const handleLocationChange = (e) => {
    e.preventDefault();
    setLocation(e.target.value.toLowerCase());
  };

  const handleCategoryChange = (e) => {
    e.preventDefault();
    if (e.target.value === "") {
      setCategory("food")
    } else {
      setCategory(e.target.value.replaceAll(" ", "").toLowerCase());
    }
  };

  async function handleSearch() {
    // Keeping these consol.logs to keep track of these variables state
    console.log("State of the Location ----", locationState)
    console.log("State of the Category ----", categoryState)
    setPage(1)
    await axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/yelp/${locationState}/${categoryState}/`)
    const allEateries = await axios.get(`${process.env.REACT_APP_EATERIES_API}/api/eateries/filtered/${locationState}/${categoryState}/?page=${page}`)
    let eateries = []
    for (let eatery of allEateries.data.eateries) {
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
  }

  const skewerEatery = async (card) => {
    const currentID = card.id
    console.log(currentID)
    console.log(props.username)
    await axios.post(`${process.env.REACT_APP_FOODIES_API}/api/foodies/eateries/skewered/`,
      {
        eateryvo_import_href: `/api/eateries/${currentID}/`,
        foodie_vo: `${props.username}`,
        notes: ""
      })
  }



  const renderCard = (card, index) => {
    return (
      <Card style={{ width: '18rem' }} key={index} className="container mt-4 mb-4 mx-3 border-0">
        <Card.Img className="image-container mt-3" style={{ objectFit: "cover" }} src={card.image_url} />
        <Card.Body>
          <Card.Title>{card.eatery_name}</Card.Title>
          <Card.Text>
            {card.address1}, {card.city}, {card.state}, {card.zip_code}
          </Card.Text>
          <Button id="button-38" onClick={detailOnClick.bind(this, card)}> <FaInfo size="1.5em" /> </Button> <Button id="button-38" onClick={skewerEatery.bind(this, card)}> <GiCupidonArrow size="1.5em" /> </Button>
        </Card.Body>
      </Card>
    )
  }

  if (eateries.length !== 0) {
    return (
      <>
        <div className="container my-5 py-3">
          <div className='p-5 text-center'>
            <h1><img src={eatineraryheader} height="140" alt="uh-oh" /></h1>
            <img src={localeateries} height="35" alt="uh-oh" />
            <div className="mt-3">
              <form>
                <div className="innerform">
                  <div className="input-field">
                    <input className='m-1 mt-3 w-50' onChange={handleCategoryChange} id="search" type="text" placeholder="What are you hungry for?" />
                  </div>
                  <div className="input-field">
                    <input className='m-1 w-50' onChange={handleLocationChange} id="search" type="text" placeholder="What city are you in?" />
                  </div>
                  <div className="input-field third-wrap">
                    <Button id="button-40" onClick={() => handleSearch()}>< GiMagnifyingGlass size="1em" /> </Button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div className="container my-5 py-3">
          <div className="row justify-content-md-center m-5">
            {eateries.map(renderCard)}
          </div>
          <Button id="button-40" onClick={() => setPage(page - 1)}>< GrPrevious size="1em" /> </Button>
          <Button id="button-40" onClick={() => setPage(page + 1)}>< GrNext size="1em" /> </Button>
        </div>
      </>
    )
  } else if (error) {
    return (
      <>
        <li></li>
        <li></li>
        <li></li>
        <li className="list-nav-item"></li>
        <div className="alert alert-success" role="alert">
          < MdOutlineDangerous /> < BsArrow90DegUp />
          {error || "Please refresh the page and try again. The search terms are not valid."}
        </div>
      </>
    )
  } else {
    return (
      <div className="mt-5 pt-5">
        <h1 className="text-center">Loading your next culinary desires...</h1>
        <div className="text-center">
          <div className="spinner-border text-success" style={{ width: '3em', height: '3rem' }} role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    );
  }
}

export default HomePageWithCards;
