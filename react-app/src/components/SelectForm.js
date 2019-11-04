import React from 'react';

export default class SelectForm extends React.Component {
    constructor(props) {
      super(props);
      this.getlist=this.getlist.bind(this)
      // console.log("props are", this.props.options.value)
      this.state = {value : this.props.userclass}
      this.handleChange = this.handleChange.bind(this)
      console.log(this.state)
    }
  
    // handleChange(event) {
    //   this.setState({value: event.target.value});
    // }
  
    // handleSubmit(event) {
    //   event.preventDefault();
    // }

    getlist(){
      var options = this.props.options
      var res = options.map((entry, index)=>
        <option value = {entry.value} key = {index}> {entry.label} </option>
      )
      return res
    }

    handleChange(e){
      this.props.handleChange(e.target.value)
    }
  
    render() {
      
      return (
        <React.Fragment>
        <form>
          <label>
            <select value={this.state.value} onChange={this.props.handleChange}>
              {this.getlist()}
            </select>
          </label>
        </form>
        </React.Fragment>
      );
    }
  }