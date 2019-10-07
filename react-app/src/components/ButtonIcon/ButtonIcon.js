import React from 'react';
import Button from 'react-bootstrap/Button';
import Icon from './Icon';

export default function ButtonIcon(props){
  props.icon.id = props.button.id + '-icon';
  return (
    <Button {...props.button} onClick={props.onClick} onContextMenu={props.onContextMenu}>
      <Icon {...props.icon}></Icon>{props.button.textcontent}
    </Button>
    )
}