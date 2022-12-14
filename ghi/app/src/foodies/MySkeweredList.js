import React from 'react';
import { Link } from 'react-router-dom';
import Iframe from './GoogleMaps2.js';
import './Foodies.css';
import { FaHeart } from "react-icons/fa";


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
        // use this for "get all skewered eateries for specific user"
        const foodie_username = this.props.username

        if (!foodie_username) {
            return
        }
        // list all skewered eateries endpoint
        const skeweredEateriesUrl = `${process.env.REACT_APP_FOODIES_API}/api/foodies/user/${foodie_username}/eateries/skewered/`;
        const skeweredEateriesResponse = await fetch(skeweredEateriesUrl);

        if (skeweredEateriesResponse.ok) {
            const skeweredEateriesData = await skeweredEateriesResponse.json();

            this.setState({ skeweredEateries: skeweredEateriesData.skewered_eateries })
        }

        // list all special dates endpoint
        const specialDatesUrl = `${process.env.REACT_APP_FOODIES_API}/api/foodies/${foodie_username}/specialdates/`;
        const specialDatesResponse = await fetch(specialDatesUrl);

        if (specialDatesResponse.ok) {
            const specialDatesData = await specialDatesResponse.json();

            this.setState({ specialDates: specialDatesData.special_dates })
        }
    }

    selectEatery(eatery) {
        this.setState({
            "selected": eatery,
        })
    }

    async hasVisited(id) {
        const putURL = `${process.env.REACT_APP_FOODIES_API}/api/foodies/eateries/skewered/${id}/`;
        const fetchConfig = {
            method: "put",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ has_visited: true })
        };

        const response = await fetch(putURL, fetchConfig);
        if (response.ok) {
            window.location.reload();
        }
    };


    render() {
        return (
            <>
                <div className="row mt-5 py-5">
                    <div className="col-md-6" id="sideNav">
                        <ul className="list-group list-group-flush">
                            <li className="list-nav-item">
                                <Link className='link' to="/myskeweredhistory">My Skewered History</Link>
                            </li>
                            <li className="list-nav-item">
                                <Link className='link' to="/review">Leave a Review</Link>
                            </li>
                            <li className="list-nav-item">
                                <Link className='link' to="/showreview">My Reviews</Link>
                            </li>
                        </ul>
                    </div>


                    <div className="col-md-6 m-5" id="mySkeweredList">
                        <p id="skeweredHeading">My Skewered List</p>
                        <table className="table table-hover">
                            <thead>
                                <tr>
                                    <th>Eatery Name</th>
                                    <th>Average Rating</th>
                                    <th>Price</th>
                                    <th>I've Been Here</th>
                                </tr>
                            </thead>
                            <tbody>
                                {this.state.skeweredEateries.map(skeweredEatery => {

                                    let hasVisited = ''
                                    if (skeweredEatery.has_visited === true) {
                                        hasVisited = 'd-none'
                                    }
                                    return (

                                        <tr onClick={() => this.selectEatery(skeweredEatery)} key={skeweredEatery.id}>
                                            <td className={hasVisited}>{skeweredEatery.eatery.eatery_name}</td>
                                            <td className={hasVisited}>{skeweredEatery.eatery.eatery_average_rating}</td>
                                            <td className={hasVisited}>{skeweredEatery.eatery.eatery_price}</td>
                                            <td className={hasVisited}>
                                                <button onClick={() => this.hasVisited(skeweredEatery.id)} type="button" className='button-39' > <FaHeart size="1.5em" /> </button>
                                            </td>
                                        </tr>
                                    )
                                })}
                            </tbody>
                        </table>
                    </div>
                </div>

                <div className='container justify-content-md-center'>
                    <div className="row py-5">
                        <div className="col-md-4" id="specialDates">
                            <p id="skeweredHeading">Special Dates</p>
                            <table className="table">
                                <thead>
                                    <tr>
                                        <th>Occasion</th>
                                        <th>Special Date</th>
                                        <th> </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {this.state.specialDates.map(specialDate => {

                                        let date = Date.parse(specialDate.special_date)
                                        const d = new Date(date)

                                        return (
                                            <tr key={specialDate.id}>
                                                <td>{specialDate.occasion}</td>
                                                <td>{d.toLocaleString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}</td>
                                            </tr>
                                        )
                                    })}
                                </tbody>
                            </table>
                        </div>
                        <div className="col-md-4 mx-5 mt-0">
                            {this.state.selected ?
                                <Iframe name={this.state.selected.eatery.eatery_name.replaceAll('&', ' ')} city={this.state.selected.eatery.location_city} state={this.state.selected.eatery.location_state} latitude={this.state.selected.eatery.eatery_latitude} longitude={this.state.selected.eatery.eatery_longitude} />
                                : null}
                        </div>

                    </div>
                </div>
            </>
        );
    }
}

export default SkeweredList;

