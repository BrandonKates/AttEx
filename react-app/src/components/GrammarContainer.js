import React from 'react';
import SelectList from './SelectList/SelectList';


export default class GrammarContainer extends React.Component {
	constructor(props){
		super(props);
		this.grammar = props.grammar;
		this.options = props.options;
	}
	render(){
		console.log(this.props)
		return (
			<div id='grammar-container'>
				<SelectList options={this.options}></SelectList>
			</div>
		)
	}
}


// Select List for a dropdown with choices
// Regular Field Populator