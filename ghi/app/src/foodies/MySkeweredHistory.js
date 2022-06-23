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
        const foodie_username = this.props.username

        if (!foodie_username) {
            return
        }

        //list all skewered eateries endpoint
        const skeweredEateriesUrl = `http://localhost:8100/api/foodies/user/${foodie_username}/eateries/skewered/`;
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
                <div className="row mt-5 py-5">
                    <div className="col-md-6" id="sideNav">
                        <ul className="list-group list-group-flush">
                            <li className="list-nav-item">
                                <Link className='link' to="/mySkewered">My Skewered Eateries</Link>
                            </li>
                            <li className="list-nav-item">
                                <Link className='link' to="/review">Leave a Review</Link>
                            </li>
                            <li className="list-nav-item">
                                <Link className='link' to="/showreview">My Reviews</Link>
                            </li>
                        </ul>
                    </div>

                <div className="col-md-4 m-5" id="mySkeweredHistory">
                        <p id="skeweredHeading">My Skewered History</p>
                            <table className="table table-hover">
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
                                                    <td >{skeweredEatery.eatery.eatery_average_rating}</td>
                                                    <td >{skeweredEatery.eatery.eatery_price}</td>
                                                    <td >{skeweredEatery.notes}</td>
                                                </tr>
                                            )
                                        }
                                        return null
                                    })}
                                </tbody>
                            </table>
                        </div>
                    </div>

                        <div className="row p-3">
                            <div className="col-md-12" id="maps">
                            { this.state.selected?
                                <Iframe name={this.state.selected.eatery.eatery_name} city={this.state.selected.eatery.location_city} state={this.state.selected.eatery.location_state} latitude={this.state.selected.eatery.eatery_latitude} longitude={this.state.selected.eatery.eatery_longitude} />
                                 :null}
                            </div>
                        </div>
            </>
        );
    }
}

export default SkeweredHistory;
