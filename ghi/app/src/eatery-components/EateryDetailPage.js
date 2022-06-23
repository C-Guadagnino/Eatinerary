import React, {useState, useEffect} from 'react';
import { Card } from "react-bootstrap";
import { ListGroup } from "react-bootstrap";
import {useParams} from 'react-router-dom';
// import Iframe from './GoogleMapsEatery.js';

function EateryDetailPage(){
  const [eateryData, setEateryData] = useState({});
  let { eateryID } = useParams();
  console.log("EATERY DATA", eateryID)
  async function getEateryDetails(){
    const eateryUrl = `http://localhost:8090/api/eateries/${eateryID}/`;
    const eateryResponse = await fetch(eateryUrl);

    if (eateryResponse.ok) {
      const eateryDataResponse = await eateryResponse.json();
      setEateryData(eateryDataResponse);
      console.log("eateryData", eateryDataResponse)
    }
  }
  useEffect(() => {
    getEateryDetails()
  },[])

  let categories_html = ''
  if (eateryData.categories) {
    categories_html = eateryData.categories.map(category => {
      // console.log(category.title)
      return (
        <li>{category.title}</li>
      )
    })
  }

  let tags_html = ''
  if (eateryData.tags) {
    tags_html = eateryData.tags.map(tag => {
      // console.log(tag.tag_name)
      return (
        <li>{tag.tag_name}</li>
      )
    })
  }

  let address_line1 = ''
  let address_line2 = ''
  if (eateryData.location) {
    address_line1 = <p>
      {eateryData.location.address1} {eateryData.location.address2} {eateryData.location.address3}
    </p>
    address_line2 = <p>
      {eateryData.location.city}, {eateryData.location.state} {eateryData.location.zip_code}
    </p>
  }

  let openhours_html = ''
  if (eateryData.open_hours) {
    openhours_html = eateryData.open_hours.map(openhours => {
      return (
        <tr>
          <td>{openhours.weekday}</td>
          <td>{openhours.start_time}</td>
          <td>{openhours.end_time}</td>
        </tr>
      )
    })
  }
  
  let image_address = ''
  if (eateryData.eatery_images) {
    image_address = eateryData.eatery_images[0].image_url
  }
  return (
    <div className="container my-5">
    <div className="container">
    
    <Card className="bg-dark text-light">
      <Card.Img style={{objectFit: "cover"}} className="img-rounded" height="300" src={image_address} alt="Card image" />
        <Card.ImgOverlay>
          <h1>{eateryData.eatery_name}</h1>
          <h3 >
          {address_line1} {address_line2}
          </h3>
        <Card.Text>
          {eateryData.price} - {eateryData.average_rating} STARS
          {categories_html}
          TAGS # {tags_html}
          </Card.Text>
      </Card.ImgOverlay>
    </Card>

      {/* <h1>{this.state.eateryData.eatery_name}</h1> */}
      {/* <p>{this.state.eateryData.average_rating} Stars, {this.state.eateryData.review_count} reviews</p>
      <p>{this.state.eateryData.price}</p> */}


      {/* <div className="col-md-6" id="skeweredMaps">
            <Iframe name={this.state.eateryData.eatery_name} city={this.state.eateryData.eatery.location_city} state={this.state.eateryData.eatery.location_state} latitude={this.state.eateryData.eatery.eatery_latitude} longitude={this.state.eateryData.eatery.eatery_longitude} />    
      </div> */}



      {/* <p>Categories</p>
      <ul>
        {categories_html}
      </ul>

      <p>Tags</p>
      <ul>
        {tags_html}
      </ul>

      <p>Address</p>
      {address_line1}
      {address_line2} */}


      <Card style={{ width: '18rem' }}>
        <ListGroup variant="flush">
          <ListGroup.Item>{openhours_html}</ListGroup.Item>
        </ListGroup>
      </Card>



    </div>
    </div>
  );
}

// class EateryDetailPage extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       eateryData: {}

//     };
//   }

  // async componentDidMount() {
  //   let { eateryID } = useParams();
  //   console.log("@@@@@@@@@@@@@@@", eateryID)
  //   const eateryUrl = "http://localhost:8090/api/eateries/1/";
  //   const eateryResponse = await fetch(eateryUrl);

  //   if (eateryResponse.ok) {
  //     const eateryData = await eateryResponse.json();
  //     this.setState({ eateryData: eateryData });
  //     console.log("eateryData", eateryData)
  //   }
  // }

  // render() {
  

  


export default EateryDetailPage;