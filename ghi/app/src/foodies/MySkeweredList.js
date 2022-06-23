import React from 'react';
import * as jose from 'jose';
import { Link } from 'react-router-dom';
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
        this.getFoodieData()
    }

    componentDidUpdate(prevProps) {
        // if old username is not the same as the current username
        if (prevProps.username !== this.props.username) {
            this.getFoodieData()
        }
    }

    async getFoodieData() {
        //use this for "get all skewered eateries for specific user"
        //const skeweredEateriesUrl = 'http://localhost:8100/api/foodies/eateries/skeweredtest/2/';
        const foodie_username = this.props.username

        if (!foodie_username) {
            return
        }

        console.log("FOODIE_USERNAME", foodie_username)

        //list all skewered eateries endpoint
        const skeweredEateriesUrl = `http://localhost:8100/api/foodies/user/${foodie_username}/eateries/skewered/`;
        const skeweredEateriesResponse = await fetch(skeweredEateriesUrl);

        if (skeweredEateriesResponse.ok) {
            const skeweredEateriesData = await skeweredEateriesResponse.json();

            this.setState({ skeweredEateries: skeweredEateriesData.skewered_eateries })
            console.log('SKEWEREDEATERIESDATA INSIDE IF STATEMENT', skeweredEateriesData)
        }

        console.log('SKEWEREDEATERIESDATA', this.state.skeweredEateriesData)

        console.log("props are:", this.props);
        //const secretKey = `${process.env.REACT_APP_DJWTO_SIGNING_KEY}`;
        //console.log("secret key is:", secretKey);
        //console.log("token is:", this.props.token);
        //const { payload, protectedHeader } = await jose.jwtDecrypt(this.props.token, secretKey)

        //     //{
        // //issuer: 'urn:example:issuer',
        // //audience: 'urn:example:audience'
        // })

        //const jwe = 'eyJhbGciOiJSU0EtT0FFUC0yNTYiLCJlbmMiOiJBMjU2R0NNIn0.nyQ19eq9ogh9wA7fFtnI2oouzy5_8b5DeLkoRMfi2yijgfTs2zEnayCEofz_qhnL-nwszabd9qUeHv0-IwvhhJJS7GUJOU3ikiIe42qcIAFme1A_Fo9CTxw4XTOy-I5qanl8So91u6hwfyN1VxAqVLsSE7_23EC-gfGEg_5znew9PyXXsOIE-K_HH7IQowRrlZ1X_bM_Liu53RzDpLDvRz59mp3S8L56YqpM8FexFGTGpEaoTcEIst375qncYt3-79IVR7gZN1RWsWgjPatfvVbnh74PglQcATSf3UUhaW0OAKn6q7r3PDx6DIKQ35bgHQg5QopuN00eIfLQL2trGw.W3grIVj5HVuAb76X.6PcuDe5D6ttWFYyv0oqqdDXfI2R8wBg1F2Q80UUA_Gv8eEimNWfxIWdLxrjzgQGSvIhxmFKuLM0.a93_Ug3uZHuczj70Zavx8Q'

        //const { plaintext, protectedHeader } = await jose.compactDecrypt(this.props.token, secretKey)

        //console.log(protectedHeader)
        //console.log(new TextDecoder().decode(plaintext))

        //console.log(protectedHeader)
        //console.log(payload)


        //list all special dates endpoint
        const specialDatesUrl = `http://localhost:8100/api/foodies/${foodie_username}/specialdates/`;
        const specialDatesResponse = await fetch(specialDatesUrl);

        if (specialDatesResponse.ok) {
            const specialDatesData = await specialDatesResponse.json();

            this.setState({ specialDates: specialDatesData.special_dates })
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
                                <Link to="/review">Leave a Review</Link>
                            </li>
                            <li className="list-group-item">
                                <Link to="/showreview">My Reviews</Link>
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
                        {this.state.selected ?
                            <Iframe name={this.state.selected.eatery.eatery_name} city={this.state.selected.eatery.location_city} state={this.state.selected.eatery.location_state} latitude={this.state.selected.eatery.eatery_latitude} longitude={this.state.selected.eatery.eatery_longitude} />
                            : null}
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

                                    if (specialDate.has_passed === false) {
                                        hasPassed = "No";
                                    } else {
                                        hasPassed = "Yes";
                                    }


                                    return (
                                        <tr key={specialDate.id}>
                                            <td>{specialDate.occasion}</td>
                                            <td>{d.toLocaleString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}</td>
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


