import React from 'react';
import {Link} from 'react-router-dom';
import './Foodies.css';

class SkeweredList extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            "skeweredEateries": [],
            "specialDates": [],
        };
        //this.handleSkeweredList = this.handleSkeweredListChange.bind(this);
    }

    async componentDidMount() {
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

    render() {
        return (
            <>
                <div className="container">

                    <div className="row p-3">
                        <div className="col-md-6" id="sideNav">
                            <ul className="list-group list-group-flush">
                                <li className="list-group-item">
                                    <Link to="/history">My Skewered History</Link>
                                </li>
                                <li className="list-group-item">
                                    <Link to="/Reviews">Reviews</Link>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div className="col-md-6" id="mySkeweredList">
                            <h1>My Skewered List</h1>
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
                                                <tr key={skeweredEatery.id}>
                                                    <td>{skeweredEatery.eatery.eatery_name}</td>
                                                    <td>{skeweredEatery.eatery.average_rating}</td>
                                                    <td>{skeweredEatery.eatery.price}</td>
                                                    <td>{skeweredEatery.notes}</td>
                                                </tr>
                                            )
                                        })}
                                    </tbody>
                                </table>
                        </div>
                        
                        <div className="row p-3">
                            <div className="col-md-6" id="specialDates">
                                <table className="table" id="specialDatesTable">
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

                </div>
            </>
        );
    }
}

export default SkeweredList;


