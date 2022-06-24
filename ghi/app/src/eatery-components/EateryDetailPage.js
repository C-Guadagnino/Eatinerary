import React, {useState, useEffect} from 'react';
import {Button} from "react-bootstrap"
import { Card } from "react-bootstrap";
import { ListGroup } from "react-bootstrap";
import {useParams} from 'react-router-dom';
import axios from 'axios'
import { GiCupidonArrow } from "react-icons/gi";
import forlater from "./images/forlater.png"
import Iframe from './GoogleMaps3.js';

function EateryDetailPage(props){
  const [eateryData, setEateryData] = useState({eatery_name:'',location:{}});
  let { eateryID } = useParams();
  // console.log("EATERY DATA", eateryID)
  async function getEateryDetails(){
    const eateryUrl = `http://localhost:8090/api/eateries/${eateryID}/`;
    const eateryResponse = await fetch(eateryUrl);

    if (eateryResponse.ok) {
      const eateryDataResponse = await eateryResponse.json();
      setEateryData(eateryDataResponse);
      // console.log("eateryData", eateryDataResponse)
    }
  }
  useEffect(() => {
    getEateryDetails()
  },[])

  console.log("EATERIES", eateryData)

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
  console.log("OPEN HOURS",openhours_html)
  
  let image_address = ''
  if (eateryData.eatery_images) {
    image_address = eateryData.eatery_images[0].image_url
  }
  console.log("EateryID",eateryID, "PROPS.USERNSME", props.username)
  const skewerEatery = async () => {
    await axios.post("http://localhost:8100/api/foodies/eateries/skewered/",
    {
    eateryvo_import_href: `/api/eateries/${eateryID}/`,
    foodie_vo: `${props.username}`,
    notes: ""
    })
  }
  return (
    <div className="container mt-5 py-5">
    
    <Card className="text-dark">
      <Card.Img className="card-style" style={{objectFit: "cover"}} height="300" src={image_address} alt="Card image" />
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
    <h6><img className='mt-3' src={ forlater } height="100" alt="uh-oh"/></h6>
    <Button id="button-38" onClick={() => skewerEatery()}><GiCupidonArrow size="4.5em" /></Button>
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

      <div className='container mb-5'>
        <div className='row'>
        <Card className='card border-0'>
          <ListGroup>
            <ListGroup.Item>{eateryData.phone}</ListGroup.Item>
            <h3 className='mx-4'> Hours of Operation </h3>
            <ListGroup.Item>{openhours_html}</ListGroup.Item>
          </ListGroup>
        </Card>
      </div>
      </div>
      
      <div className='containter mt-5'>
        <div className='row'>
          <div>
          <Iframe name={eateryData.eatery_name.replaceAll('&', ' ')} city={eateryData.location.city} state={eateryData.location.state} latitude={eateryData.latitude} longitude={eateryData.longitude} />
          </div>
        </div>
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