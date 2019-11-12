import React from 'react';
import {Modal, Button, Form, Col, Row} from 'react-bootstrap';
import SelectList from './SelectList/SelectList'

export default class SelectModal extends React.Component{
    constructor(props){
        super(props);
        this.grammar = JSON.parse(this.props.grammar)
        this.state = {
            show: false,
            selected: 0,
            history:[]
        } 
        this.answers = this.grammar["Q"]
        console.log(this.answers)
        this.handleClose=this.handleClose.bind(this)
        this.handleShow = this.handleShow.bind(this)
        this.handleChange=this.handleChange.bind(this)
        this.handleSave=this.handleSave.bind(this)
        this.getResult=this.getResult.bind(this)
        this.getLabelFromEntry = this.getLabelFromEntry.bind(this)
        this.convertListToOptions = this.convertListToOptions.bind(this)
    }
    handleClose() {
        this.setState({show:false});
    }
    
    handleShow() {
        this.setState({show:true});
    }
    handleChange(event){
        this.state.selected = event.target.value
        // console.log(this.state)
    }
    handleSave(event){
        this.setState({show:false});
        this.state.history.push(this.state.selected)
        // console.log(this.state);
    }

    getResult(){
        var res = this.state.history
        var listItems=res.map((entry, index)=>{
          
          return <div style={{display: 'flex', flexDirection: 'row'}} key = {index}> {this.getLabelFromEntry(entry, 'form')} </div>
          
        })
        return listItems
    }

    getLabelFromEntry(entry, method){
      var VAR = /^[A-Z]$/
      var test = this.grammar['Q']
      var index = parseInt(entry)-1
      var res = test[index]
      var objectsToRender = res.map((item, key)=> {
        if(VAR.exec(item)!==null){
          if(method === 'form'){
              var listItem = this.grammar[item]
              return (<SelectList options={this.convertListToOptions(listItem)} key={key}></SelectList>)
          }
          if(method === 'radio'){
            var str = ""
            var listItem = this.grammar[item]
            var toGrab =listItem.length>2?3:listItem.length
            for(var i = 0; i<toGrab;i = i+1){
              str+= listItem[i] + " / "
            }
            console.log("str: ", str)
            return (<label key = {key}> {str}  </label>)
          }
        }

        else{
          return <label key={key}>  {item}  </label>
        }
        });
      console.log(objectsToRender)
      return objectsToRender
    }
    convertListToOptions(items){
      return items.map(item => {
        return {value: item, label: item};
      })
    }
    

    render(){
        return (
          <div>
            <div>
              {this.getResult()}
            </div>
            
          <Button variant="primary" onClick={this.handleShow} > 
            Add Response
          </Button>
    
          <Modal show={this.state.show} onHide={this.handleClose}>
            <Modal.Header closeButton>
              <Modal.Title> Choose One type of question</Modal.Title>
            </Modal.Header>
            <Modal.Body>
            <Form.Group as={Row}>
            <Form.Label as="legend" column sm={2}>
                Radios
            </Form.Label>
            <Col sm={10}>
                <Form.Check
                type="radio"
                label={this.getLabelFromEntry("1", "radio")}
                name="selectgrammar"
                value="1"
                onChange={this.handleChange}
                id="1"
                />
                <Form.Check
                type="radio"
                label={this.getLabelFromEntry("2", "radio")}
                name="selectgrammar"
                value="2"
                onChange={this.handleChange}
                id="2"
                />
                <Form.Check
                type="radio"
                label={this.getLabelFromEntry("3", "radio")}
                name="selectgrammar"
                value="3"
                onChange={this.handleChange}
                id="3"
                />
                <Form.Check
                type="radio"
                label={this.getLabelFromEntry("4", "radio")}
                name="selectgrammar"
                value="4"
                onChange={this.handleChange}
                id="4"
                />
                <Form.Check
                type="radio"
                label={this.getLabelFromEntry("5", "radio")}
                name="selectgrammar"
                value="5"
                onChange={this.handleChange}
                id="5"
                />
            </Col>
            </Form.Group>
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={this.handleClose}>
                Close
              </Button>
              <Button variant="primary" onClick={this.handleSave}>
                Add
              </Button>
            </Modal.Footer>
          </Modal>
        </div>
      );
    }
}
