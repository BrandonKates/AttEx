import React, { Component } from 'react';


class Canvas extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: null,
            point: {x: null, y: null}
        }
    }
    componentDidMount() {
        this.canvas = this.refs.canvas;
        //console.log(this.props)
        this.newImageHeight = 0;
        this.ctx = this.canvas.getContext("2d");

        this.img = new Image();
        this.img.src = this.props.image.image;
        this.img.onload = () => {
            this.canvas.height = this.img.height;
            this.canvas.width = this.img.width;

            this.ctx.drawImage(this.img, 0, 0);
        }
        //console.log(this.canvas)
        this.showImage()
    }    
    componentDidUpdate(nextProps) {
        this.showImage()
    }

    showImage() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        this.ctx.globalAlpha = 1;
        this.ctx.drawImage(this.img, 0, 0);
        if(this.state.point.x)
            this.drawCircle(this.state.point)
    }

    getMousePos(e) {
        var rect = this.canvas.getBoundingClientRect();
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        };
    }

    render(){
        return (
            <div id="canvas-container">
                <canvas ref='canvas' className="canvas"
                    onMouseDown={this._mouseDown.bind(this)}
                    onMouseMove={this._mouseMove.bind(this)}
                    //onMouseUp={this._mouseUp.bind(this)}
                    //onContextMenu={this._contextMenu.bind(this)}
                    //onWheel={this._mouseWheel.bind(this)}
                    >
                </canvas>
            </div>
        )
    }
    _mouseDown(e){
        var pos = this.getMousePos(e);
        this.setState({point: pos})
        this.props.onChange(pos)
    }

    _mouseMove(e){
        var pos = this.getMousePos(e);
        //console.log(pos, this.state.point)
    }

    drawCircle(pos) {
        const x = pos.x;
        const y = pos.y;
        this.ctx.beginPath();
        this.ctx.fillStyle = "red";
        this.ctx.globalAlpha = 1;
        this.ctx.arc(x, y, 4, 0, 2 * Math.PI, true);
        this.ctx.fill();
    }
}

export default Canvas;