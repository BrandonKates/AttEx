import React from 'react';

export default function Icon(props){
  const classList = Array.isArray(props.className) ? props.className.join(" ") : props.className;
  return (
    <i id={props.id} className={classList}> </i>
    )
}