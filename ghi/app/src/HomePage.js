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
  ImageWrapper
} from "./Card";



function HomePage() {
  //creating IP state
  const [ip, setIP] = useState('');
  const [eateries, setEateries] = useState([]);
  const [eateryColumns, setColumns] = useState([[],[],[]]);
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
    const eateryColumns = [[],[],[]]
    let i = 0
    for (let eatery of eateries){
      eateryColumns[i].push(eatery);
      i = i + 1;
      if (i > 2) {
          i = 0;
      }
    }
    setColumns(eateryColumns)
    console.log("EATERIES", eateries)
  }
  

  // function EateryColumn(eateries) {
  //   return (
  //       <div className="col">
  //           {eateries.map(eatery => {
  //               return (
  //                   <div key={eatery.name} className="card mb-3 shadow">
  //                       <img src={eatery.image_url} className="card-img-top" />
  //                       <div className="card-body">
  //                           <h3 className="card-title">{eatery.address1}</h3>
  //                           <h4 className="card-title">{eatery.city}</h4>
  //                           <h5 className="card-title">{eatery.state}</h5>
  //                           <h5 className="card-title">{eatery.zip_code}</h5>
  //                           {/* <h6 className="card-subtitle mb-2 text-muted">
  //                               {eatery.manufacturer.name}
  //                           </h6> */}
  //                       </div>
  //                   </div>
  //               );
  //           })}
  //       </div>
  //   );
  // }

  useEffect(() => {
    //passing getData method to the lifecycle method
    //if we get IP data send location to Yelp API
    getData()
  }, [])

    return (
      <>
      <CardHeader>
      <div className='p-5 text-center bg-light'>
        <h1 className='mb-3'>Heading</h1>
        <h2 className='mb-3'>Subheading</h2>
        {/* <div className="form">
            <i className="fa fa-search"></i>
            <input onChange={this.handleSearch} type="text" className="form-control form-input" placeholder="Search by VIN#"/>
            <span className="left-pan"><i className="fa fa-microphone"></i></span>
            </div> */}
        <a className='btn btn-primary' href='' role='button'>
          Call to action
        </a>
      </div>
      </CardHeader>
      <div className = "container text-light mt-4">
      <div className = "card-columns">
      {eateries.map(eatery => {
        return (
          <CardWrapper>
         <div key={eatery.id} className="card mb-3 shadow">

         <ImageWrapper>
      <img src={eatery.image_url} className="card-img-top" />
      </ImageWrapper>
      <div className="card-body">
      <CardHeader>
          <h2 className="card-title">{eatery.name}</h2>
  
          </CardHeader>
          <h4 className="card-subtitle mb-2 text-muted">
              {eatery.address1}, {eatery.city}, {eatery.state}, {eatery.zip_code}
          </h4>
      </div>
  </div>
      </CardWrapper>
          );
        })}
      </div>
      </div>
</>

      // <div className='App'> 
      //   <div className="row">
      //     <div className = "column">
      //         {eateries.map(eatery => {
      //       return (
      //         <CardWrapper>
      //         <CardHeader>
      //         <CardHeading>
      //         <p>
      //           {eatery.name}
      //         </p>
      //         </CardHeading>
      //       </CardHeader>
      //       <CardBody>
      //         {eatery.address1}, {eatery.city}, {eatery.state} {eatery.zip_code}
      //       </CardBody>
      //     </CardWrapper>
      //         );
      //       })}
      //       </div>
      //     </div>
      //   </div>
    );
  }

  export default HomePage;