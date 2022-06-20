import React from 'react';
import {Link} from 'react-router-dom';
import './Foodies.css';

class SkeweredHistory extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "skeweredEateries": [],
        };
        //this.handleSkeweredList = this.handleSkeweredListChange.bind(this);
    }

    async componentDidMount() {
        //list all skewered eateries endpoint
        const skeweredEateriesUrl = 'http://localhost:8100/api/skewered/';
        const skeweredEateriesResponse = await fetch(skeweredEateriesUrl);

        if(skeweredEateriesResponse.ok){
            const skeweredEateriesData = await skeweredEateriesResponse.json();

            this.setState({skeweredEateries: skeweredEateriesData.skewered_eateries})
        }
    }

    render() {
        return (
            <>
                <div className="container">

                    <div className="row p-3">
                        <div className="col-md-6" id="sideNav">
                            <ul className="list-group list-group-flush">
                                <li className="list-group-item">
                                    <Link to="/skewered">My Skewered List</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/Reviews">Reviews</Link>
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
                                                <tr key={skeweredEatery.id}>
                                                    <td >{skeweredEatery.eatery.eatery_name}</td>
                                                    <td >{skeweredEatery.eatery.average_rating}</td>
                                                    <td >{skeweredEatery.eatery.price}</td>
                                                    <td >{skeweredEatery.notes}</td>
                                                </tr>
                                            )
                                        }
                                    })}
                                </tbody>
                            </table>
                        </div>
                    </div>
            </>
        );
    }
}

export default SkeweredHistory;
