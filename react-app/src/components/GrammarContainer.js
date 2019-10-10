import React from 'react';
import SelectList from './SelectList/SelectList';


export default class GrammarContainer extends React.Component {
	constructor(props){
		super(props);
		this.grammar = this.processGrammar(props.grammar)
		this.options = props.options;
	}

	processGrammar(grammar){
		console.log(grammar)
		grammar = JSON.parse(grammar);
		var VAR = /^[A-Z]$/
		var COORD = /^\([0-9], [0-9]\)$/;
		
		var test = grammar['S'][4]
		var objectsToRender = test.map((item)=> {
			if(VAR.exec(item)!==null){
				//item is a variable
				var listItem = grammar[item]
				console.log(listItem)
				return (<SelectList options={this.convertListToOptions(listItem)}></SelectList>)
			}
			else if(COORD.exec(item)!==null){
				//item is a coordinate
				return <p> {item} </p>
			}
			else{
				// item is a string
				//if (["?", "!", "."].includes(item)){
			//		return <div> item </div>
		//		}
				return <p> {item} </p>
			}
			});
		//for(var key in grammar){
		//	if(grammar.hasOwnProperty(key)){
		//		grammar[key]
		//	}	
		//}
		return objectsToRender;
	}
	convertListToOptions(items){
		return items.map(item => {
			return {value: item, label: item};
		})
	}

	render(){
		return (
			<div id='grammar-container'>
				{this.grammar}
			</div>
		)
	}
}


// Select List for a dropdown with choices
// Regular Field Populator

// For a VARIABLE: we want to link other dropdowns with the same variable