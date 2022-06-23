import React from 'react';

class AutoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            specialDate: '',
            occasion: '',
            hasPassed: '',
            repeats: '',
            frequency: [],
            foodieVO: []
        };

        this.handleSpecialDateChange = this.handleSpecialDateChange.bind(this);
        this.handleOccasionChange = this.handleOccasionChange.bind(this);
        this.handleHasPassedChange = this.handleHasPassedChange.bind(this);
        this.handleRepeatsChange = this.handleRepeatsChange.bind(this);
        this.handleFrequencyChange = this.handleFrequencyChange.bind(this);
        this.handleFoodieVoChange = this.handleFoodieVoChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSpecialDateChange(event) {
        const value = event.target.value;
        this.setState({specialDate: value})
    }

    handleOccasionChange(event) {
        const value = event.target.value;
        this.setState({occasion: value})
    }

    handleHasPassedChange(event) {
        const value = event.target.value;
        this.setState({hasPassed: value})
    }

    handleRepeatsChange(event) {
        const value = event.target.value;
        this.setState({repeats: value})
    }

    handleFrequencyChange(event) {
        const value = event.target.value;
        this.setState({frequency: value})
    }

    handleFoodieVoChange(event) {
        const value = event.target.value;
        this.setState({foodieVO: value})
    }

    async handleSubmit(event) {
        event.preventDefault();
        const data = {...this.state};
        delete data.models
        
        const appointmentUrl = `http://localhost:8100/api/foodies/${this.state.foodieVO}/specialdates/`;
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
            
            //         {
            //     "special_date": "2022-08-07",
            //     "occasion": "Anniversary3",
            //     "has_passed": false,
            //     "repeats": true,
            //     "frequency": "Yearly",
            //     "foodie_vo": "frank001"
            // }

            const cleared = {
                specialDate: '',
                occasion: '',
                hasPassed: '',
                repeats: '',
                frequency: [],
                foodieVO: []
                };
            this.setState(cleared);
        }
    }


    async componentDidMount() {

        const url = 'http://localhost:8100/api/foodies/';
        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            // console.log("data is: ", data);
          
            this.setState({foodieVO: data.username})
        }
    }

    render() {
        return(
            <div className="row">
                    <div className="offset-3 col-6">
                        <div className="shadow p-4 mt-4">
                            <h1>Create a new Automobile</h1>
                            <form onSubmit={this.handleSubmit} id="create-shoe-form">
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleColorChange} value={this.state.color} placeholder="color" required type="text" name="color" id="color" className="form-control" />
                                    <label htmlFor="color">Color</label>                     
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleYearChange} value={this.state.year} placeholder="year" required type="text" name="year" id="year" className="form-control" />
                                    <label htmlFor="year">Year</label>                     
                                </div>
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleVinChange} value={this.state.vin} placeholder="vin" required type="text" name="vin" id="vin" className="form-control" />
                                    <label htmlFor="reason">VIN (17 Characters)</label>                     
                                </div>
                                <div className="mb-3">
                                    <select onChange={this.handleModelChange} value={this.state.model_id} required id="model" name="model" className="form-select">
                                        <option value="">Choose the Vehicle</option>
                                        {this.state.models.map(model_id => {
                                            return (
                                                <option key={model_id.id} value={model_id.id}>{model_id.name}</option>
                                            );
                                        })}
                                    </select>
                                  </div>                    
                                <button className="btn btn-primary">Create</button>
                            </form>
                        </div>
                    </div>
                </div>
        );
    }
}

export default AutoForm;