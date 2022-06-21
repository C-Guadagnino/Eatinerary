import React from 'react';
import {Link} from 'react-router-dom';
import './Foodies.css';
import Iframe from './GoogleMaps.js';

class SkeweredHistory extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "skeweredEateries": [],

        };
        //this.handleSkeweredList = this.handleSkeweredListChange.bind(this);
        this.selectEatery = this.selectEatery.bind(this);
    }

    async componentDidMount() {
        //list all skewered eateries endpoint
        const skeweredEateriesUrl = 'http://localhost:8100/api/foodies/eateries/skewered/';
        const skeweredEateriesResponse = await fetch(skeweredEateriesUrl);

        if(skeweredEateriesResponse.ok){
            const skeweredEateriesData = await skeweredEateriesResponse.json();

            this.setState({skeweredEateries: skeweredEateriesData.skewered_eateries})
        }
    }

    selectEatery(eatery) {
        console.log("is this selectEatery:", eatery);
        this.setState({
            "selected": eatery,
        })
    }

    render() {
        return (
            <>
                <div className="container">

                    <div className="row p-3">
                        <div className="col-md-6" id="sideNav">
                            <ul className="list-group list-group-flush">
                                <li className="list-group-item">
                                    <Link to="/mySkewered">My Skewered List</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/review">Reviews</Link>
                                </li>
                            </ul>
                        </div>
                    </div>

                <div className="col-md-6" id="mySkeweredList">
                        <h1>My Skewered History</h1>
                            <table className="table table-striped">
                                <thead>
                                    <tr>
                                        <th>Eatery Name</th>
                                        <th>Average Rating</th>
                                        <th>Price</th>
                                        <th>Notes</th>
                                        <th> </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {this.state.skeweredEateries.map(skeweredEatery => {

                                        if(skeweredEatery.has_visited === true){
                                    
                                            return (
                                                <tr onClick={() => this.selectEatery(skeweredEatery)} key={skeweredEatery.id}>
                                                    <td >{skeweredEatery.eatery.eatery_name}</td>
                                                    <td >{skeweredEatery.eatery.average_rating}</td>
                                                    <td >{skeweredEatery.eatery.price}</td>
                                                    <td >{skeweredEatery.notes}</td>
                                                </tr>
                                            )
                                        }
                                        return null
                                    })}
                                </tbody>
                            </table>
                        </div>

                        <div className="row p-3">
                            <div className="col-md-12" id="maps">
                                
                            { this.state.selected?
                                <Iframe name={this.state.selected.eatery.eatery_name} city={this.state.selected.eatery.location_city} state={this.state.selected.eatery.location_state} latitude={this.state.selected.eatery.eatery_latitude} longitude={this.state.selected.eatery.eatery_longitude} />
                                 :null}

                                {/* { this.state.selected?
                                <Iframe name={this.state.selected.eatery.eatery_name} latitude={this.state.selected.eatery.eatery_latitude} longitude={this.state.selected.eatery.eatery_longitude} />
                                 :null} */}
                    
                                {/* { this.state.selected?
                                <Iframe city={this.state.selected.eatery.location_city} state={this.state.selected.eatery.location_state} />
                                 :null} */}

                                {/* {this.state.skeweredEateries.map(skeweredEatery => {
                                    if(skeweredEatery.has_visited === true){

                                    return(
                                        <div className="myClassName" id="myId">
                                            <Iframe city={skeweredEatery.eatery.location_city} state={skeweredEatery.eatery.location_state} />
                                        </div>
                                    )
                                    }
                                })} */}
                            </div>
                        </div>


                    </div>
            </>
        );
    }
}

export default SkeweredHistory;
