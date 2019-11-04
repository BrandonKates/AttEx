import React from 'react';
import {Modal} from 'react-bootstrap'



export default class Grammars extends React.Component {

	constructor(props){
		super(props);
		this.grammar = this.decodeGrammar(props.grammar)
		this.options = props.options;
	};

	decodeGrammar(grammar){
		grammar = JSON.parse(grammar);
		console.log("Grammar:"+grammar['S'])
		this.test = grammar['S'][4]
	}


	render(){
		var data = {
			test : this.test,
			grammar : this.grammar
		}
		console.log("Grammars rendering")
		return (
			
            <div>
                {data& <GrammarContainer grammar={data.grammar} options={this.props.options} test = {data.test}/>}
            </div>       
            
		)
	}
}