import React from 'react';
import "./Foodies.css"

class SpecialDateForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            specialDate: '',
            occasion: '',
            repeats: false,
            frequency: ''
        };

        this.handleSpecialDateChange = this.handleSpecialDateChange.bind(this);
        this.handleOccasionChange = this.handleOccasionChange.bind(this);
        this.handleRepeatsChange = this.handleRepeatsChange.bind(this);
        this.handleFrequencyChange = this.handleFrequencyChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSpecialDateChange(event) {
        const value = event.target.value;
        this.setState({ specialDate: value })
    }

    handleOccasionChange(event) {
        const value = event.target.value;
        this.setState({ occasion: value })
    }


    handleRepeatsChange(event) {
        const value = event.target.checked;
        this.setState({ repeats: value })
    }

    handleFrequencyChange(event) {
        const value = event.target.value;
        this.setState({ frequency: value })
    }


    async handleSubmit(event) {
        event.preventDefault();
        const data = { ...this.state };
        data.special_date = data.specialDate
        data.foodie_vo = this.props.username
        delete data.specialDate
        data.has_passed = false




        const appointmentUrl = `${process.env.REACT_APP_FOODIES_API}/api/foodies/${this.props.username}/specialdates/`;
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };


        const response = await fetch(appointmentUrl, fetchConfig);

        if (response.ok) {
            const newAppointment = await response.json();

            const cleared = {
                specialDate: '',
                occasion: '',
                repeats: '',
                frequency: ''
            };
            this.setState(cleared);
        }
    }


    render() {
        return (
            <div className='container mt-5 py-5'>
                <div className="row" style={{ textAlign: 'left' }}>
                    <div className="offset-3 col-6">
                        <div className="shadow p-4 mt-4">
                            <h1>Add A Special Date</h1>
                            <form onSubmit={this.handleSubmit} id="create-shoe-form">
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleSpecialDateChange} value={this.state.specialDate} placeholder="specialDate" required type="date" name="specialDate" id="specialDate" className="form-control" />
                                    <label htmlFor="specialDate">Special Date</label>
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleOccasionChange} value={this.state.occasion} placeholder="occasion" required type="text" name="occasion" id="occasion" className="form-control" />
                                    <label htmlFor="occasion">Occasion</label>
                                </div>
                                <div className="form-check">
                                    <input onChange={this.handleRepeatsChange} value={this.state.repeats} placeholder="repeats" type="checkbox" name="repeats" id="repeats" className="form-check-input" />
                                    <label htmlFor="repeats" className="form-check-label" >Does this occasion repeat?</label>
                                </div>
                                <div className="mb-3">
                                    <select onChange={this.handleFrequencyChange} value={this.state.frequency} id="frequency" name="frequency" className="form-select">
                                        <option value="">How often?</option>
                                        <option key="0" value="Monthly">Monthly</option>
                                        <option key="1" value="Yearly">Yearly</option>
                                    </select>
                                </div>
                                <button className="button-38">Create</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default SpecialDateForm;