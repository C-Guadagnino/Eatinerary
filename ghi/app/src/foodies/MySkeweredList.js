import React from 'react';
import {Link} from 'react-router-dom';
import Iframe from './GoogleMaps2.js';
import './Foodies.css';

class SkeweredList extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "skeweredEateries": [],
            "specialDates": [],
        };
        this.selectEatery = this.selectEatery.bind(this);
    }

    async componentDidMount() {
        //use this for "get all skewered eateries for specific user"
        //const skeweredEateriesUrl = 'http://localhost:8100/api/foodies/eateries/skeweredtest/2/';
        //list all skewered eateries endpoint
        const skeweredEateriesUrl = 'http://localhost:8100/api/foodies/eateries/skewered/';
        const skeweredEateriesResponse = await fetch(skeweredEateriesUrl);

        if(skeweredEateriesResponse.ok){
            const skeweredEateriesData = await skeweredEateriesResponse.json();

            this.setState({skeweredEateries: skeweredEateriesData.skewered_eateries})
        }

        //list all special dates endpoint
        const specialDatesUrl = 'http://localhost:8100/api/foodies/specialdates/';
        const specialDatesResponse = await fetch(specialDatesUrl);

        if(specialDatesResponse.ok){
            const specialDatesData = await specialDatesResponse.json();

            this.setState({specialDates: specialDatesData.special_dates})
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
                    <div className="row p-3">
                        <div className="col-md-6" id="sideNav">
                            <ul className="list-group list-group-flush">
                                <li className="list-group-item">
                                    <Link to="/mySkeweredHistory">My Skewered History</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/review">Reviews</Link>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div className="col-md-6" id="mySkeweredList">
                            <p id="skeweredHeading">My Skewered List</p>
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

                                            return (

                                                <tr onClick={() => this.selectEatery(skeweredEatery)} key={skeweredEatery.id}>
                                                    <td><button className='btn button-39'>{skeweredEatery.eatery.eatery_name}</button></td>
                                                    <td>{skeweredEatery.eatery.eatery_average_rating}</td>
                                                    <td>{skeweredEatery.eatery.eatery_price}</td>
                                                    <td>{skeweredEatery.notes}</td>
                                                </tr>
                                            )
                                        })}
                                    </tbody>
                                </table>
                        </div>
                        
                        <div className="row p-3">
                            <div className="col-md-6" id="skeweredMaps">
                            { this.state.selected?
                                <Iframe name={this.state.selected.eatery.eatery_name} city={this.state.selected.eatery.location_city} state={this.state.selected.eatery.location_state} latitude={this.state.selected.eatery.eatery_latitude} longitude={this.state.selected.eatery.eatery_longitude} />
                                 :null}
                            </div>

                            <div className="col-md-6" id="specialDates">
                                <p id="skeweredHeading">Special Dates</p>
                                <table className="table table-striped" id="specialDatesTable">
                                        <thead>
                                            <tr>
                                                <th>Occasion</th>
                                                <th>Special Date</th>
                                                <th>Has Passed</th>
                                                <th> </th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {this.state.specialDates.map(specialDate => {
                                                
                                                let date = Date.parse(specialDate.special_date)
                                                const d = new Date(date)

                                                let hasPassed = "";
                                                
                                                if (specialDate.has_passed === false){
                                                    hasPassed = "No";
                                                } else {
                                                    hasPassed = "Yes";
                                                }
                                                

                                                return (
                                                    <tr key={specialDate.id}>
                                                        <td>{specialDate.occasion}</td>
                                                        <td>{d.toLocaleString('en-US', {month:'long', day:'numeric', year:'numeric'})}</td>
                                                        <td>{hasPassed}</td>
                                                    </tr>
                                                )
                                            })}
                                        </tbody>
                                </table>
                            </div>
                        </div>

            </>
        );
    }
}

export default SkeweredList;


